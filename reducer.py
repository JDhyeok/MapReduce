import sys


def fileParser(path='mapped_output.txt'):
    """ File 2 Word Dictionary Function

    Params:
    path (String) : File's path

    Returns:
    List : Returning word list

    """
    inFp = open(path, 'r')

    result = []

    for inStr in inFp:
        tmp_lst = inStr.strip().split()
        result.append(tmp_lst[0])

    return result


def reducer(data):
    """ Reducer Function

    Params:
    data (List) : Word dictionary generated from mapper

    Returns:
    Dict : Returning reduced word dictionary

    """
    result = {}

    for word in data:
        result[word] = result.get(word, 0) + 1

    return result


def writeOutput(data, name='final_output.txt'):
    """ Write The Result of Mapper

    Params:
    data (Dict) : Reduced data
    name (String) : Name of output file

    Returns:
    None

    """
    if name[-4:] != '.txt':
        name += '.txt'

    with open(name, 'w') as outFp:
        for key, val in data.items():
            outFp.write(key + ' ' + str(val) + '\n')

    outFp.close()


if __name__ == '__main__':
    args = sys.argv

    if len(args) < 2:
        reduced_data = reducer(fileParser())
    else:
        reduced_data = reducer(fileParser(args[1]))

    writeOutput(reduced_data)
