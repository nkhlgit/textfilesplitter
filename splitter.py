import sys

def main(argv):
    input_file_name = argv[0]
    num_output_files = int(argv[1])
    with open(input_file_name, 'r', encoding="utf8") as f:
        for total_lines, l in enumerate(f):
            pass
    print(total_lines)
    # minus 1 becase to last file contain remender after diviion.
    lines_a_file = total_lines // (num_output_files - 1)

    in_file = open(input_file_name, 'r', encoding="utf8")
    k= 0
    while (k < num_output_files ):
        k += 1
        output_file_name = input_file_name + '_' + str(k)
        out_file = open(output_file_name, 'w', encoding="utf8")
        for m, line in enumerate(in_file):
            if (m < lines_a_file):
                out_file.write(line)
            else:
                out_file.write(line)
                break
        out_file.close()
    in_file.close()


if __name__ == "__main__":
     if len(sys.argv) != 3:
         print(" enter file name and number of output files in format:")
         sys.exit(0)

     main(sys.argv[1:])
