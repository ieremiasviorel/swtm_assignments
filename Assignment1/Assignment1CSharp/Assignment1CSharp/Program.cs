using System;
using System.Collections.Generic;
using System.IO;

namespace Assignment1CSharp
{
    class Program
    {
        static void Main(string[] args)
        {

            if (args.Length != 1)
            {
                Console.WriteLine("Provide exactly one argument for the name of the file to be processed");
                Environment.Exit(1);
            }

            string inputFilePath = args[0];
            string outputFilePath = "result_" + inputFilePath;

            StreamReader inputFile = new StreamReader(inputFilePath);
            StreamWriter outputFile = new StreamWriter(outputFilePath);

            List<string> batchLines;

            while (true)
            {
                batchLines = ReadBatchLines(inputFile);

                if (batchLines.Count > 0)
                {
                    WriteBatchLines(outputFile, ReverseBatchLines(batchLines));
                }
                else
                {
                    break;
                }
            }

            inputFile.Close();
            outputFile.Close();
        }

        static List<string> ReadBatchLines(StreamReader inputFile)
        {
            string currentLine;
            List<string> batchLines = new List<string>();

            while (batchLines.Count < 10 && (currentLine = inputFile.ReadLine()) != null)
            {
                batchLines.Add(currentLine);
            }

            return batchLines;
        }

        static List<string> ReverseBatchLines(List<String> batchLines)
        {
            batchLines.Reverse();
            return batchLines;
        }

        static void WriteBatchLines(StreamWriter outputFile, List<String> batchLines)
        {
            foreach (string line in batchLines)
            {
                outputFile.Write(line + "\n");
            }
        }
    }
}
