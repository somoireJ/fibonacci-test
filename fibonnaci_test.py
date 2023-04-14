import unittest

def fibonacci(n):
    """Generate the Fibonacci sequence up to n."""
    # initialize the sequence with the first two numbers
    fib_sequence = [0, 1]
    # generate subsequent numbers until reaching n
    while fib_sequence[-1] < n:
        # calculate the next number as the sum of the previous two
        next_number = fib_sequence[-1] + fib_sequence[-2]
        # add the next number to the sequence
        fib_sequence.append(next_number)
    return fib_sequence

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [0])
        self.assertEqual(fibonacci(1), [0, 1, 1])
        self.assertEqual(fibonacci(2), [0, 1, 1, 2])
        self.assertEqual(fibonacci(3), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(13), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci(21), [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(fibonacci(34), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    unittest.main()
    print("Tests complete.")
