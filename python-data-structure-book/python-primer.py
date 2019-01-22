import random

def is_multiple(n, m):
    return True if (n % m) == 0 else False

def is_even(k):
    return True if k%2 == 0 else False

def minmax(data):
    min = data[0]
    max = data[0]
    for number in data:
        min = number if number < min else min
        max = number if number > max else max
    return min,max

def squaresTill(n):
    for number in range(1, n+1):
        yield (number, number*number)

def sumOfSquaresTill(n):
    sum =0
    for number, square in squaresTill(n):
        sum = sum + square
    
    return sum
def  sumOfSquaresOfOddNumberLessThan(n):
    sum = 0
    for number in range(1,n+1,2):
        sum = sum + (number*number)
    return sum

def  sumOfSquaresOfOddNumberLessThanUsingComprehension(n):
    Sum = sum([((number*number)) for number in range(1,n+1,2)])
    return Sum

if __name__ == "__main__":
    print("R-1.1 is_multiple(10,2): "+ str(is_multiple(10,2)))
    print("R-1.1 is_multiple(10,3): "+ str(is_multiple(10,3)))
    print("R-1.2 is_even(10): "+ str(is_even(10)))
    print("R-1.3 minmax([1,4,7,2,6,8,4]): " + str(minmax([1,4,7,2,6,8,4])))
    print("R-1.4 squaresTill(10): ",  end = " ")
    # USE OF GENERATOR
    for number, square in squaresTill(9):
        print( "[" +  str(number)+" - "+str(square) + "]", end = " ")
    print()

    print("R-1.5 sumOfSquaresTill(10): " + str(sumOfSquaresTill(10)))
    print("R-1.6 sumOfSquaresOfOddNumberLessThan(10): " + str(sumOfSquaresOfOddNumberLessThan(10)))
    print("R-1.7 sumOfSquaresOfOddNumberLessThanUsingComprehension(10): " + str(sumOfSquaresOfOddNumberLessThanUsingComprehension(10)))
    print("R-1.9 getArray [50,60,70,80]: ", [x for x in range(50,90,10)])
    print("R-1.10 getArray [8, 6, 4, 2, 0, −2, −4, −6, −8]: ", [x for x in range(8,-10,-2)])
    print("R-1.11 getArray [1, 2, 4, 8, 16, 32, 64, 128, 256]: ", [pow(2,x) for x in range(0,9)])
    
    print("R-1.12: ",random.choice([1,2,4,6,7,3]),random.randrange(10,999,2))
    arr = [1,2,3,4,5]
    print(
    """C-1.13 To Reverse an array we can use a for loop and loop backwards using range(len(arr),1,-1)
    and in the python function we can use arr[::-1] """, arr[::-1])
