from random import shuffle


class SortTest:

    @staticmethod
    def minimum_test(func):
        sample = [i for i in range(1000)]
        shuffle(sample)

        return SortTest.print_result("minimum_test", func.__name__, sorted(sample) == func(sample))

    @staticmethod
    def same_digits(func):
        sample = 2 * [i for i in range(10)]
        shuffle(sample)

        return SortTest.print_result("same_digits", func.__name__, sorted(sample) == func(sample))

    @staticmethod
    def test_all(func):
        SortTest.minimum_test(func)
        SortTest.same_digits(func)

    @staticmethod
    def print_result(test_name, sample_name, result, *details):
        print()
        print("SortTest {} | {} tested".format(test_name, sample_name))
        print("Test result: {}".format(result))
        print("Test details: ")
        if len(details) > 0:

            for i in range(len(details)):
                print("             " + details[i])
        else:
            print("             None")
        print()
