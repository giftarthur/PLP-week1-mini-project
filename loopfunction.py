#Anything entered through input() comes in a string
#so we convert n to interger from string at the dame time
n = int(input("Enter a number:"))
print("The square table is as given below")
print("Number Square")
i = 1
while i<=n:
    print(i,"   ", i**2) #I have added 4 spaces in " " to space i and i**2 where i**2 is the square of i
    i +=1