'''
Project Name: Turtle Patterns II 
Author: Julianna Fotheringham
Due Date: 04/10/2021
Course: CS1400-001

This program asks you to choose between options 1, 2, and 3and then draws you a picture based off the number you chose"
'''
# (1) put your import statements here 
from turtle import *

def main():
    '''
    Program starts here. 
    '''
    user_choice = int(input("Pick a number between 1 and 3 for a surprise!" ))
    if user_choice == 1:
        WIDTH = 1000
        HEIGHT = 1000

        
        setup(width= WIDTH, height = HEIGHT)
        bgcolor("light blue")
        speed = 0

    #how to draw buttefly code
        def butterfly():
            """draws butterfly for option 1"""
        
            pensize(2)
            
            color("orangered" ,"orange")
            begin_fill()
            right(90)
            forward(175 *.75)
            circle(-50 *.75, 180)
            left(120)
            circle(-50 *.75, 180)
            forward(175*.75)
            end_fill()
            
            
            
            color("light coral" ,"tomato")
            begin_fill()
            left(150)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()
            
            color("light coral" ,"tomato")
            begin_fill()
            left(120)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()
            
            
            color("orangered" ,"orange")
            begin_fill()
            left(150)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()

            #antenas
            begin_fill()
            right(10)
            forward(200*.75)
            begin_fill()
            circle(10 *.75,360)
            end_fill()
            backward(200 *.75)
            left(25)
            forward(200*.75)
            begin_fill()
            circle(10 *.75,360)
            end_fill()
            



            #THIs is FOR ONE HEART IN OUR CLOVER
        def clover():
            """ draws clover for option 1 """
            pensize(2)
            color("dark green" , "green")
            begin_fill()
            right(90)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            #last heart in our clover <3
            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()
            color("dark green" , "green")
                
            begin_fill()
            right(200)
            forward(300/5)
            left(90)
            forward(10/5)
            left(90)
            forward(300/5)
            left(90)
            forward(10/5)
            end_fill()
                
                
                
                
                #butterfly placement
        penup()
        goto(-250,150)
        pendown()
        right(45)
        butterfly()



    #CLOVER PLACEMENT
        penup()
        goto(-75,-200)
        pendown()
        clover()

        penup()
        goto(-25,-100)
        pendown()
        clover()

        penup()
        goto(20,-250)
        pendown()
        clover()


        penup()
        goto(-400,-200)
        pendown()
        clover()

        penup()
        goto(400,-150)
        pendown()
        clover()

        penup()
        goto(250,-175)
        pendown()
        clover()

        penup()
        goto(200,-300)
        pendown()
        clover()

        penup()
        goto(-250,-100)
        pendown()
        clover()
        
        penup()
        goto(400,400)
        color("yellow", "gold1")
        begin_fill()
        pendown()
        circle(200,360)
        end_fill()



    #LUCKY U

        penup()
        goto(100, 175)
        color("magenta")
        begin_fill()
        pendown()
        write("Lucky You", move= False, align = "left", font=("Apple Chancery", 80, "normal"))
        end_fill()

    elif user_choice == 2:
        WIDTH = 1000
        HEIGHT = 1000

        
        setup(width= WIDTH, height = HEIGHT)
        bgcolor("light blue")
        speed = 0

    #how to draw buttefly code
        def butterfly():
            """draws butterfly for option 2"""
            pensize(2)
            
            color("pink" ,"hot pink")
            begin_fill()
            right(90)
            forward(175 *.75)
            circle(-50 *.75, 180)
            left(120)
            circle(-50 *.75, 180)
            forward(175*.75)
            end_fill()
            
            
            
            color("purple" ,"orchid")
            begin_fill()
            left(150)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()
            
            color("purple" ,"orchid")
            begin_fill()
            left(120)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()
            
            
            color("pink" ,"hot pink")
            begin_fill()
            left(150)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()

            #antenas
            begin_fill()
            right(10)
            forward(200*.75)
            begin_fill()
            circle(10 *.75,360)
            end_fill()
            backward(200 *.75)
            left(25)
            forward(200*.75)
            begin_fill()
            circle(10 *.75,360)
            end_fill()
            



            #THIs is FOR ONE HEART IN OUR CLOVER
        def clover():
            """draws clover for option 2"""
            pensize(2)
            color("dark green" , "green")
            begin_fill()
            right(90)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            #last heart in our clover <3
            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()
            color("dark green" , "green")
                
            begin_fill()
            right(200)
            forward(300/5)
            left(90)
            forward(10/5)
            left(90)
            forward(300/5)
            left(90)
            forward(10/5)
            end_fill()
                
                
                
                
                #butterfly placement
        penup()
        goto(-250,150)
        pendown()
        right(45)
        butterfly()



    #CLOVER PLACEMENT
        penup()
        goto(-75,-200)
        pendown()
        clover()

        penup()
        goto(-25,-100)
        pendown()
        clover()

        penup()
        goto(20,-250)
        pendown()
        clover()


        penup()
        goto(-400,-200)
        pendown()
        clover()

        penup()
        goto(400,-150)
        pendown()
        clover()

        penup()
        goto(250,-175)
        pendown()
        clover()

        penup()
        goto(200,-300)
        pendown()
        clover()

        penup()
        goto(-250,-100)
        pendown()
        clover()
        
        penup()
        goto(400,400)
        color("yellow", "gold1")
        begin_fill()
        pendown()
        circle(200,360)
        end_fill()



    #LUCKY U

        penup()
        goto(100, 175)
        color("magenta")
        begin_fill()
        pendown()
        write("Lucky You", move= False, align = "left", font=("Apple Chancery", 80, "normal"))
        end_fill()
        
        





    elif user_choice == 3:
        WIDTH = 1000
        HEIGHT = 1000

        
        setup(width= WIDTH, height = HEIGHT)
        bgcolor("light blue")
        speed = 0

    #how to draw buttefly code
        def butterfly():
            """ draws butterfly for option 3 """
        
            pensize(2)
            
            color("cyan4" ,"DarkSeaGreen")
            begin_fill()
            right(90)
            forward(175 *.75)
            circle(-50 *.75, 180)
            left(120)
            circle(-50 *.75, 180)
            forward(175*.75)
            end_fill()
            
            
            
            color("DarkOliveGreen2" ,"CadetBlue3")
            begin_fill()
            left(150)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()
            
            color("DarkOliveGreen2" ,"CadetBlue3")
            begin_fill()
            left(120)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()
            
            
            color("cyan4" ,"DarkSeaGreen")
            begin_fill()
            left(150)
            forward(175*.75)
            circle(-50*.75, 180)
            left(120)
            circle(-50*.75, 180)
            forward(175*.75)
            end_fill()

            #antenas
            begin_fill()
            right(10)
            forward(200*.75)
            begin_fill()
            circle(10 *.75,360)
            end_fill()
            backward(200 *.75)
            left(25)
            forward(200*.75)
            begin_fill()
            circle(10 *.75,360)
            end_fill()
            



            #THIs is FOR ONE HEART IN OUR CLOVER
        def clover():
            """ draws clover for option 3"""
            pensize(2)
            color("dark green" , "green")
            begin_fill()
            right(90)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()

            #last heart in our clover <3
            color("dark green" , "green")
            begin_fill()
            left(150)
            forward(175/5)
            circle(-50/5, 180)
            left(120)
            circle(-50/5, 180)
            forward(175/5)
            end_fill()
            color("dark green" , "green")
                
            begin_fill()
            right(200)
            forward(300/5)
            left(90)
            forward(10/5)
            left(90)
            forward(300/5)
            left(90)
            forward(10/5)
            end_fill()
                
                
                
                
                #butterfly placement
        penup()
        goto(-250,150)
        pendown()
        right(45)
        butterfly()



    #CLOVER PLACEMENT
        penup()
        goto(-75,-200)
        pendown()
        clover()

        penup()
        goto(-25,-100)
        pendown()
        clover()

        penup()
        goto(20,-250)
        pendown()
        clover()


        penup()
        goto(-400,-200)
        pendown()
        clover()

        penup()
        goto(400,-150)
        pendown()
        clover()

        penup()
        goto(250,-175)
        pendown()
        clover()

        penup()
        goto(200,-300)
        pendown()
        clover()

        penup()
        goto(-250,-100)
        pendown()
        clover()
        
        
        penup()
        goto(400,400)
        color("yellow", "gold1")
        begin_fill()
        pendown()
        circle(200,360)
        end_fill()
        



    #LUCKY U

        penup()
        goto(100, 175)
        color("magenta")
        begin_fill()
        pendown()
        write("Lucky You", move= False, align = "left", font=("Apple Chancery", 80, "normal"))
        end_fill()
        
    elif user_choice != 1 or 2 or 3:
        print("Please choose an option between 1, 2, and 3 to see your surprise!")


if __name__ == "__main__":
    main()
    










1
