#Python program to print hollow rectangle
#accept width and breadth from user
width=int(input("Enter Width\t"))
breadth=int(input("Enter breadth \t"))
for i in range(0,breadth):
    for j in range(0,width):
        if (i==0 or j ==0 or i==breadth or j==width):
             print(" *",end="")
        else:
             print(" ",end="*")
    print()