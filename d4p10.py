str1=input("Enter the string_1: ")
str2=input("Enter the string_2: ")
new_str=""
l1=[]
l2=[]
if len(str1)!=len(str2):
    print("False")
else:
    if len(str1)==1:
        print(True)
    else:
        while str2 not in l2:
                    for i in str1:
                        l1.append(i)
        
                    for i in range(0,len(l1)-1,2):
                        [l1[i],l1[i+1]]=[l1[i+1],l1[i]]
                        for j in l1:
                            new_str+=l1[i]
                            l2.append(new_str)
                            print(l2)
                            str1=new_str
        
        
    
