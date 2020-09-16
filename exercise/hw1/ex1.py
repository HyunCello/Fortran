print("hello, world!");


def palindromic(num):
    pri = 1
    for i in range(2,10000):
        if num % i == 0 and  num != i:
            print(num,"isn't prime")
            pri = 0
            break
            
    if pri != 0:
        print(num,"is prime")
        list = []
        while num != 0:
            list.append(num % 10)
            num = num/10
            num = int(num)
        rev = list
        list = list.reverse()
        print(list)
        print(rev)
        if rev == list:
            print("palindromic")
        else:
            print("not palindromic")
       
   
    return 0


if __name__ == "__main__":
    while True:
        print("Please insert number")
        num = int(input())
        palindromic(num)
