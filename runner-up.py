if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    ma = max(arr)
    counter=None
for i in arr:
    if ma==i:
        pass
    elif counter==None:
        counter= i
    elif i> counter:
        counter= i
print(counter)
