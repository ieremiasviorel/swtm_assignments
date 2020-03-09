const process = require('process');
const fs = require('fs');
const lineReader = require('line-reader');

if (process.argv.length != 3) {
	console.log('Provide exactly one argument for the name of the file to be processed');
	process.exit(1);
}

const inputFilePath = process.argv[2];
const outputFilePath = 'result_' + inputFilePath;
const outputWriter = fs.createWriteStream(outputFilePath);

console.time();

const batchLines = {
	linesBuffer: [],

	linesBufferFullListener: function(linesBuffer) {},
	
	getLines() {
		return this.linesBuffer;
	},
	
	appendLine(line) {
		this.linesBuffer.push(line);
		
		if (this.linesBuffer.length === 10) {
			this.linesBufferFullListener([...this.linesBuffer]);
			this.linesBuffer = [];
		}
	},

	noLinesLeft() {
		this.linesBufferFullListener(this.linesBuffer);
		console.timeEnd();
	},
	
	registerLinesBufferFullListener: function(listener) {
		this.linesBufferFullListener = listener;
	}

}

const reverseBatchLines = (batchLines) => {
	return batchLines.reverse();
}

const writeBatchLines = (batchLines) => {
	if (batchLines.length) {
		batchLines.forEach(line => outputWriter.write(line + '\n'));
	} else {
		outputWriter.end();
	}
}

const reverseAndWriteBatchLines = (batchLines) => {
	writeBatchLines(reverseBatchLines(batchLines))
}

batchLines.linesBuffer = [];
batchLines.registerLinesBufferFullListener(reverseAndWriteBatchLines);

lineReader.eachLine(inputFilePath, function(line, last) {
	batchLines.appendLine(line);

	if (last) {
		batchLines.noLinesLeft();
		return false;
	}
});
