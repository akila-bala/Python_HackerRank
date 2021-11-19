if __name__ == '__main__':
    n = int(input())
lst=[]
lst2=[]
x=0
for i in range(n):
    lst.append(x)
    x=x+1
for i in range(n):
    print(lst[i]*lst[i])
