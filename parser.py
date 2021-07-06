import sys
import re
import gzip


def main(argv):
    sep = argv[2] if len(argv) == 3 else ';'
    pattern = re.compile(r'(\w+\s+\d+\s+\d{2}:\d{2}:\d{2}) (\w+) ([\w.]+): (\d+\/\w+\/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}) (\d+\.\d+\.\d+\.\d+) - ((?:[\S\\]+)(?: \S+ [\S]+)?) "(\d+)" (\d+\.\d+) (\d+\.\d+) (\d+) "(.*)" "(.*)" - upstream_responce: (\d+\.\d+|-)')
    with gzip.open(argv[0], 'r') as fin, open(argv[1], 'w') as fout:
        for line in fin.readlines():
            match = pattern.match(line.decode().replace(sep, ','))
            if match:
                fout.write(f'{match.group(1)}{sep}{match.group(2)}{sep}{match.group(3)}{sep}{match.group(4)}{sep}{match.group(5)}{sep}{match.group(6)}{sep}{match.group(7)}{sep}{match.group(8)}{sep}{match.group(9)}{sep}{match.group(10)}{sep}{match.group(11)}{sep}{match.group(12)}{sep}{match.group(13)}\n')
            else:
                print(f'Failed to parse line: {line}')


if __name__ == '__main__':
    main(sys.argv[1:])
