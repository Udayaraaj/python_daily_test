prg3-

def checkone(num):
    sum=0
    while num>=1:
        rem = num % 10
        sum+= int(rem*rem)
        num=int(num/ 10)

    if sum == 1:
        print("True")
    else:
        checkone(sum)

val = int( input ("Enter the value: "))
checkone(val)