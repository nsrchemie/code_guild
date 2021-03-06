from nose.tools import assert_equal


class Test_list_primes(object):

    def test_list_primes(self):
        assert_equal(list_primes(1), [])
        assert_equal(list_primes(2), [2])
        assert_equal(list_primes(7), [2, 3, 5, 7])
        assert_equal(list_primes(9), list_primes(7))
        print('Success: test_list_primes')


def main():
    test = Test_list_primes()
    test.test_list_primes()


if __name__ == '__main__':
    main()
