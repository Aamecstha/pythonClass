def multiplier(n):
    def times(a):
        return a*n
    return times

times3=multiplier(3)
print(times3(10))
del multiplier
print(times3(10))
