def stream_basics():
    with open('./test.txt', encoding='utf-8') as stream:
        print(stream.name)

        print(stream.mode)

        print(stream.encoding)

        print(stream.read())
        print(stream.read())

        # move pointer to 0th byte
        stream.seek(0)

        # read 16 chars
        print(stream.read(16))

        print(stream.read(1))
        print(stream.read(1))

        # current byte index pointer
        print(stream.tell())

def read_line():
    print('lines:')
    with open('./test.txt', encoding='utf-8') as stream:
        line_count = 1
        for line in stream:
            print('{:>4} {}'.format(str(line_count), line.rstrip()))
            line_count += 1


if __name__ == '__main__':
    read_line()