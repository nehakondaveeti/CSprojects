# fib numbers code

def fib_memo(n,memo):
    if n==0 or n==1:
        return memo[n]
    else:
        # basically a loop to determine where it stops
        # so when n is less than the length of the stored memo, this will stop
        if n >= len(memo):
            f = fib_memo(n-1, memo)+fib_memo(n-2, memo)
            # storing it in memo
            memo.append(f)
            return f
        else:
            return memo[n]
def fib_rec(n):
    # beginning, want to feed everything to this
    if n==0 or n==1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def main():
    '''
    for i in range(50):
        print(i, " ", fib_rec(i))

main()
'''

memo = [0,1]
for i in range(500):
    print(i, " ", fib_memo(i,memo))

        
