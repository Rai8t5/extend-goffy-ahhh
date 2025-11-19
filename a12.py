def funta1(n):
    return n*(n+1)/2
print(funta1(4))
def funta2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
def funta3(n):
    sum=0
    for i in range(1, n+1):
     for j in range(1, n+1):
        sum += 1
    return sum