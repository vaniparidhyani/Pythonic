#!/usr/bin/python



#"Prime Factorization" is finding which prime numbers multiply together to make the original number.

''' Return an array containing prime numbers whose product is x
  Examples:
  primeFactorization(6) == [2,3]
  primeFactorization(5) == [5]
  primeFactorization(12) == [2,2,3]'''


def primeFactorization(x):
    
    factors = []
    i = 2
    
    if x > 0:
        
        while x > 1:
            while x % i == 0:
                factors.append(i)
                x = x/i
            i = i + 1
         
        return factors

def doTestsPass():
    testVals = [6, 5, 12, 1, -1]
    testAnswers = [[2, 3], [5], [2, 2, 3], [], None]
    for value, answer in zip(testVals, testAnswers):
        if primeFactorization(value) != answer:
            print ("Test failed for %d" % value)
            return False

    return True


if __name__ == "__main__":
    if doTestsPass():
        print ("All tests pass")
    else:
        print ("Not all tests pass")
