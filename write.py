import os
import csv
import re
def csv1():
    line_count = 0
    with open('daftar-nama.txt', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        next(csv_reader)
        row = ''
        for i in range(1, 20):
            for row in csv_reader:
                if line_count == 0:
                    print(f' {", ".join(row)}')
                    ++line_count
                else:

                    line_count += 1
def read_reverse_order_2(file_name):

    with open(file_name, 'r') as read_obj:

        next(read_obj)
        next(read_obj)
        lines = read_obj.readlines()

        lines = [line.strip() for line in lines]


        lines = reversed(lines)

        return lines
def read_reverse_order(file_name):

    with open(file_name, 'rb') as read_obj:


        read_obj.seek(0, os.SEEK_END)



        pointer_location = read_obj.tell()
        pointer_location=20

        buffer = bytearray()

        while pointer_location >= 0:

            read_obj.seek(pointer_location)

            pointer_location = pointer_location -1
            new_byte = read_obj.read(1)
            if new_byte == b'\n':
                yield buffer.decode()[::-1]
                buffer = bytearray()
            else:
                buffer.extend(new_byte)
        if len(buffer) > 0:
            yield buffer.decode()[::-1]

def main():


    lines_in_reverse_order = read_reverse_order_2('daftar-nama.txt')


    for line in lines_in_reverse_order:

        print(line)

    with open('4210191027_ImamBIladi.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=" ")
        #
        for line in read_reverse_order_2('daftar-nama.txt'):

            csv_writer.writerow(line)

if __name__ == '__main__':
  # csv1()
   main()




