
def lambdaMap(arr):
    ans = map(
    lambda x: [i**2 for i in x if i > 0]
, arr)
    return ans