def _findMaxInSequence(S):
    """Recusion Algorithm to Find Max in Array in O(n)"""
    if(len(S) == 1):
        return S[0]
    index = 0
    max = S[0]
    return findMaxInSequence(S,index+1,max)

def findMaxInSequence(S, index, max):
    max = S[index] if max < S[index] else max
    if len(S) > (index + 1):
        max = findMaxInSequence(S,index+1,max)
    return max

def power_in_log_n(x,n):
    if n == 0 :
        return 1
    else:
        partial = power_in_log_n(x,n // 2)
        result = partial * partial
        if n % 2 == 1:
            result = result * x
        return result        

if __name__ == "__main__":
    print("Max in Sequence [1,4,6,3,8,2,5]: ",_findMaxInSequence([1,4,6,3,8,2,5]))
    print("Fifth Power of 2: ",power_in_log_n(2,5))
