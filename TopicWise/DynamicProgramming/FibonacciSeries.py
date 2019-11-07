'''
Find the nᵗʰ Fibonacci Number.

'''

class Fibonacci:
    def FibonacciBottomUp(self,n):
        arr = [0,1]
        for i in range(2,n+1):
            arr.append(arr[i-2] + arr[i-1])
        return arr[n]
    
    def FibonacciTopDown(self,n):
        if n==0: return 0
        if n == 1: return 1
        return self.FibonacciTopDown(n-1) + self.FibonacciTopDown(n-2)

    def test(self):
        assert self.FibonacciBottomUp(10) == 55
        assert self.FibonacciTopDown(10) == 55
        assert self.FibonacciBottomUp(40) == 102334155

        print("All Tests Passed")


if __name__ == "__main__":
    f = Fibonacci()
    f.test()