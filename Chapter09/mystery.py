def a_mystery_function_3(binary_string):
    """
    binary_string is a string that is at least 4 characters long with 1s and 0s with the rightmost character representing the 0th bit
    """
    binary_list=[int(i) for i in binary_string]
    binary_list.reverse()
    a,b,c=binary_list[0:3]
    return (a or b or not c) and \
            (a or b or c) and \
            (a or not b or c) and \
            (a or not b or not c) and \
            (not a or b or not c) and \
            (not a or b or c) and \
            (not a or not b or not c)


def a_mystery_function_2(binary_string):
    """
    binary_string is a string that is at least 4 characters long with 1s and 0s with the rightmost character representing the 0th bit
    """
    binary_list=[int(i) for i in binary_string]
    binary_list.reverse()
    a,b=binary_list[0:2]
    return a and not b