marks = int(input("marks:")) 

if(marks >= 90):
    print("A")
elif(marks >= 70 and marks < 90):
    print("B")
elif(marks >= 60 and marks < 70):
    print("C")
elif(marks >= 40 and marks < 60):
    print("D") 
else:
    print("fail")               