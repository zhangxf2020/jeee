def other(fun):
    def weeper(num):
        i =[]
        while True:
            if num ==0:
                break
            elif num%2 ==0:
                fun(num)
                num -=1
    return weeper

@other
def student(num):
    conut = 0
    for i in range(num):
        if i <10:
            conut +=1
            print('{}正确,一共{}个'.format(i,conut))
        else:return


student(20)

