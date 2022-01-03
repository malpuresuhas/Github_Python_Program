#Program to find cube of numbers
#taking input from user till how many numbers user want to print cube
rangeNo=int(input("enter upto which number you want to print cube\t"))

i = 1;
while i <= rangeNo:
    cubeNo = 0
    cubeNo = i * i * i
    print("cube of %d is ===>   %f"  %(i,cubeNo))
    i=i+1