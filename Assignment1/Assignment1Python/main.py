import sys
import time

def read_batch_lines(input_file):
	batch_lines = []

	while len(batch_lines) < 10:
		current_line = input_file.readline()
		if current_line:
			batch_lines.append(current_line)
		else:
			break

	return batch_lines


def reverse_batch_lines(batch_lines):
	return list(reversed(batch_lines))


def write_batch_lines(output_file, batch_lines):
	for line in batch_lines:
		output_file.write(line)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Provide exactly one argument for the name of the file to be processed")
		exit(1)

	input_file_path = sys.argv[1]
	output_file_path = 'result_' + input_file_path

	batch_lines = []

	start_time = time.time()

	with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
		while True:
			batch_lines = read_batch_lines(input_file)

			if len(batch_lines):
				batch_lines = reverse_batch_lines(batch_lines)
				write_batch_lines(output_file, batch_lines)
			else:
				break

	end_time = time.time()

	print('Execution time: %fs' % (end_time - start_time))
