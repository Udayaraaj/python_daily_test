letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
li=[]
val=input("Enter the digit: ")
if len(val)==2:
    for i in range(0, len(val)):
        new_val = letters[val[i]]
        li.append(new_val)
    for i in li[0]:
        for j in li[1]:
            print("\"", i + j, "\"", end=",")

if len(val)==1:
    for i in letters[val]:
        print("\"",i,"\"",end=',')


