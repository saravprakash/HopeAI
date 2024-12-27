class multipleFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing") 

    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            msg=str(num)+ " is Even number"
        else:
            msg=str(num)+ " is Odd number"
        return msg

    def Elegible():
        gender=(input("Your Gender:"))
        age=int(input("Your Age:"))
        if(gender.lower()=="male" and age>20 ):
            msg="ELIGIBLE"
        elif(gender.lower()=="female" and age>17):
            msg="ELIGIBLE"
        elif(gender.lower()!="male" or gender.lower()!="female"):
            msg="Enter a valid gender"
        else:
            msg="NOT ELIGIBLE"
        return msg

    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject1="))
        sub3=int(input("Subject1="))
        sub4=int(input("Subject1="))
        sub5=int(input("Subject1="))
        total=sub1+sub2+sub3+sub4+sub5
        avg=total/5
        print("Total :", total)
        print("Percentage :", avg )

    def triangle():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        a= (h*b)/2
        print("Area of Triangle: ",a)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b2=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        p= h1+h2+b2
        print("Perimeter of Triangle: ",p)