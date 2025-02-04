lenght1 = float(input("Enter the first rectangles lenght:"))
width1 = float(input("enter the first rectangles width: "))

lenght2 = float(input("now enter the second rectangles lenght:"))
width2 = float(input("and the second rectangles width please: "))

area1 = lenght1 * width1
area2 = lenght2 * width2

if area1 > area2:
    print("The first rectangle has an area of" +str (area1) + " is bigger than the second " +str(area2))
elif area2 > area1:
    print("The second rectangle "+str(area2) +" has a bigger than the first "+str(area1))
else:
    print("The rectangles have the same area, hooray! "+str(area1) +" = "+str(area2))