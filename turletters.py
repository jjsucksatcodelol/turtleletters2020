import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

	
    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        #reset
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
    elif letter == "C":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.left(90)
        tur.fd(30)
        tur.pd()
        tur.left(90)
        tur.fd(20)
        #reset
        tur.pu()
        tur.right(90)
        tur.fd(10)
        tur.right(90)
        tur.fd(40)
    elif letter == "D":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.fd(30)
        tur.left(135)
        tur.fd(15)
        tur.left(45)
        tur.fd(11)
        tur.left(45)
        tur.fd(15)
        #reset
        tur.pu()
        tur.right(135)
        tur.fd(40)
    elif letter == "E":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        #letter
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.left(90)
        tur.fd(15)
        tur.pd()
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        #reset
        tur.pu()
        tur.left(90)
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
    elif letter == "F":
	tur.setheading(0)
        tur.pd()
        
        tur.fd(20)
        tur.bk(20)
        tur.right(90)
        tur.fd(20)
        
        tur.left(90)
        tur.fd(20)
        tur.bk(20)

        tur.right(90)
        tur.fd(20)

        tur.pu()
        tur.left(180)
        tur.fd(45)
        tur.right(90)
        tur.fd(55)
    elif letter == "G":
	tur.setheading(0)
        tur.right(180)
        
        tur.pd()
        tur.circle(20,180)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(10)

        tur.pu()
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(25)
        		
    elif letter == "H":
	tur.setheading(0)
        tur.right(90)
        tur.fd(7)

        tur.pd()

        tur.fd(40)
        tur.bk(20)

        tur.left(90)
        tur.fd(15)
        tur.right(90)
        tur.bk(20)
        tur.fd(40)

        tur.pu()
        tur.bk(45)
        tur.left(90)
        tur.fd(20)
	
    elif letter == "I":
	tur.setheading(0)
        tur.pd()

        tur.fd(20)
        tur.bk(30)
        tur.fd(15)
        tur.right(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(15)
        tur.bk(30)

        tur.pu()
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(40)
        
    elif letter == "J":
	tur.setheading(0)
        tur.pd()

        tur.fd(20)

        tur.fd(15)
        tur.bk(30)
        tur.fd(15)
        tur.right(90)
        tur.fd(30)
        tur.circle(-20,70)

        tur.pu()
        tur.right(110)
        tur.fd(50)
        tur.right(90)
        tur.fd(45)
        
    elif letter == "K":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.fd(30)
        tur.bk(15)
        tur.left(45)
        tur.fd(15)
        tur.bk(15)
        tur.left(90)
        tur.fd(15)
        #reset
        tur.pu()
        tur.left(45)
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.fd(15)
        tur.left(45)
        tur.fd(15)
        tur.left(90)
        tur.fd(15)
        tur.left(45)
        tur.fd(20)
        #reset
        tur.pu()
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
    elif letter == "V":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.left(30)
        tur.fd(30)
        tur.left(130)
        tur.fd(30)
        #reset
        tur.pu()
        tur.left(25)
        tur.fd(10)
        tur.right(90)
        tur.fd(15)
    elif letter == "W":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.left(10)
        tur.fd(30)
        tur.left(140)
        tur.fd(30)
        tur.right(130)
        tur.fd(30)
        tur.left(145)
        tur.fd(32)
        #reset
        tur.pu()
        tur.fd(10)
        tur.right(80)
        tur.fd(10)
    elif letter == "X":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.left(45)
        tur.fd(35)
        tur.pu()
        tur.right(135)
        tur.fd(30)
        tur.pd()
        tur.right(135)
        tur.fd(35)
        #reset
        tur.pu()
        tur.left(45)
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
    elif letter == "Y":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        #letter
        tur.left(45)
        tur.fd(10)
        tur.right(45)
        tur.fd(20)
        tur.bk(20)
        tur.left(135)
        tur.fd(10)
        #reset
        tur.pu()
        tur.left(45)
        tur.fd(20)
        tur.right(90)
        tur.fd(10)
    elif letter == "Z":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(15)
        tur.pd()
        #letter
        tur.left(90)
        tur.fd(25)
        tur.right(135)
        tur.fd(40)
        tur.left(135)
        tur.fd(25)
        #reset
        tur.pu()
        tur.left(90)
        tur.fd(40)
        tur.right(90)
        tur.fd(15)		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)
    turtleLetter("B",tur)
    turtleLetter("C",tur)
    turtleLetter("D",tur)
    turtleLetter("E",tur)
    turtleLetter("F",tur)
    turtleLetter("G",tur)
    turtleLetter("H",tur)
    turtleLetter("I",tur)
    turtleLetter("J",tur)
    turtleLetter("K",tur)
    turtleLetter("L",tur)
    turtleLetter("M",tur)
    turtleLetter("N",tur)
    turtleLetter("O",tur)
    turtleLetter("P",tur)
    turtleLetter("Q",tur)
    turtleLetter("R",tur)
    turtleLetter("S",tur)
    turtleLetter("T",tur)
    turtleLetter("U",tur)
    turtleLetter("V",tur)
    turtleLetter("W",tur)
    turtleLetter("X",tur)
    turtleLetter("Y",tur)
    turtleLetter("Z",tur)


    window.exitonclick()
