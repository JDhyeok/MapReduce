import re
import sys


def fileParser(path):
    """ File 2 Word List Function

    Params:
    path (String) : File's path

    Returns:
    List : Returning word list from file

    """
    inFp = open(path, 'r')

    result = []

    for inStr in inFp:
        inStr = re.sub(
            '[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', inStr).lower()
        result.extend(inStr.split())

    inFp.close()
    return result


def mapper(data):
    """ Mapper Function

    Params:
    data (List) : File's path

    Returns:
    List : Returning word list from file

    """
    result = []

    for word in data:
        result.append([word, 1])

    return result


def writeOutput(data, name='mapped_output.txt'):
    """ Write The Result of Mapper

    Params:
    data (List) : Mapped data
    name (String) : Name of output file

    Returns:
    None

    """
    if name[-4:] != '.txt':
        name += '.txt'

    with open(name, 'w') as outFp:
        for info in data:
            outFp.write(info[0] + ' ' + str(info[1]) + '\n')

    outFp.close()


if __name__ == '__main__':

    args = sys.argv
    path = args[1]

    mapped_data = mapper(fileParser(path))

    if len(args) > 2:
        writeOutput(mapped_data, args[2])
    else:
        writeOutput(mapped_data)
