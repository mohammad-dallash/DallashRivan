import unittest

unittest.TestCase
def add(numbers):

    if not numbers:
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]

    numbers = numbers.replace("\n", delimiter)
    num_list = [int(x) for x in numbers.split(delimiter) if x != ""]
    negative_nums = [str(x) for x in num_list if x < 0]
    num_list.assertTrue(x<10001 "should be true")
    num_list = [0 if x > 1000 else x for x in num_list]
    if negative_nums:
        raise Exception("Sorry, no negative numbers allowed")
    return sum(num_list)







