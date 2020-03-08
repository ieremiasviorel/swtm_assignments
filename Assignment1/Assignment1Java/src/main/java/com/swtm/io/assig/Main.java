package com.swtm.io.assig;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Provide exactly one argument for the name of the file to be processed");
            System.exit(1);
        }

        String inputFilePath = args[0];
        String outputFilePath = "result_" + inputFilePath;
        List<String> batchLines;

        try (
                BufferedReader inputBufferedReader = new BufferedReader(new FileReader(inputFilePath));
                BufferedWriter outputBufferedWriter = new BufferedWriter(new FileWriter(outputFilePath))
        ) {
            while (true) {
                batchLines = readBatchLines(inputBufferedReader);

                if (batchLines.size() > 0) {
                    writeBatchLines(outputBufferedWriter, reverseBatchLines(batchLines));
                } else {
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static List<String> readBatchLines(BufferedReader inputBufferedReader) throws IOException {
        String currentLine;
        List<String> batchLines = new ArrayList<>(10);

        while (batchLines.size() < 10 && (currentLine = inputBufferedReader.readLine()) != null) {
            batchLines.add(currentLine);
        }

        return batchLines;
    }

    static List<String> reverseBatchLines(List<String> batchLines) {
        Collections.reverse(batchLines);

        return batchLines;
    }

    static void writeBatchLines(BufferedWriter outputBufferedWriter, List<String> batchLines) throws IOException {
        for (String line : batchLines) {
            outputBufferedWriter.write(line + "\n");
        }
    }
}
