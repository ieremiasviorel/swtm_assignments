<?php
if ($argc != 2) {
	echo "Provide exactly one argument for the name of the file to be processed";
	exit(1);
}

$input_file_name = $argv[1];
$output_file_name = "result_" . $input_file_name;

$input_file = fopen($input_file_name, "r");
$output_file = fopen($output_file_name, "w");

while(true)  {
	$batch_lines = readBatchLines($input_file);
	
	if (count($batch_lines) > 0) {
		writeBatchLines($output_file, reverseBatchLines($batch_lines));
	} else {
		break;
	}
}

fclose($input_file);
fclose($output_file);

function readBatchLines($input_file) {
	$batch_lines = [];
	
	while(count($batch_lines) < 10 and !feof($input_file)) {
		$batch_lines[] = fgets($input_file);
	}
	
	return $batch_lines;
}

function reverseBatchLines($batch_lines) {
	return array_reverse($batch_lines);
}

function writeBatchLines($output_file, $batch_lines) {
	foreach($batch_lines as &$line) {
		fwrite($output_file, $line);
	}
}
?>