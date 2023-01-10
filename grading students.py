if __name__ == '__main__':
    a=int(input())
    l=[]
    for j in range(a):
        grade=int(input())
        if grade >= 38 and grade <= 100:
            if (5-(grade%5)) < 3:
               
                grade+=(5-(grade%5))
                l.append(grade)
            else:
                l.append(grade)
        else:
             l.append(grade)
    for k in l: print(k)
