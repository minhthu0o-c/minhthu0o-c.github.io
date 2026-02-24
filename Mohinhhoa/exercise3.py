import turtle

wn = turtle.Screen()
wn.title("Simple Calculator - Component Architecture")
wn.bgcolor("white")
wn.setup(width=400, height=500)
wn.tracer(0)  

current_expression = ""
buttons = []  

display_pen = turtle.Turtle()
display_pen.hideturtle()
display_pen.penup()
display_pen.color("black")

def draw_group_a_display():
    display_pen.clear()
    display_pen.goto(-150, 180)
    display_pen.pendown()
    display_pen.pensize(3)
    for _ in range(2):
        display_pen.forward(300)
        display_pen.right(90)
        display_pen.forward(60)
        display_pen.right(90)
    display_pen.penup()
    display_pen.goto(140, 135) 
    text_to_show = current_expression if current_expression else "0"
    display_pen.write(text_to_show, align="right", font=("Courier", 30, "bold"))

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

def draw_button_component(text, x, y, color="#e0e0e0"):
    pen.goto(x, y)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(60)
        pen.right(90)
    pen.end_fill()
    pen.goto(x + 30, y - 50)
    pen.color("black")
    pen.write(text, align="center", font=("Arial", 20, "normal"))
    buttons.append({'text': text, 'x': x, 'y': y, 'w': 60, 'h': 60})

def create_group_b_numbers():
    start_x = -150
    start_y = 100
    draw_button_component('7', start_x, start_y)
    draw_button_component('8', start_x + 70, start_y)
    draw_button_component('9', start_x + 140, start_y)

    draw_button_component('4', start_x, start_y - 70)
    draw_button_component('5', start_x + 70, start_y - 70)
    draw_button_component('6', start_x + 140, start_y - 70)
    

    draw_button_component('1', start_x, start_y - 140)
    draw_button_component('2', start_x + 70, start_y - 140)
    draw_button_component('3', start_x + 140, start_y - 140)
    

    draw_button_component('0', start_x + 70, start_y - 210)

def create_group_c_operations():
    start_x = 70 # Cột bên phải
    start_y = 100
    
    ops_color = "lightblue"
    draw_button_component('/', start_x + 20, start_y, ops_color)
    draw_button_component('*', start_x + 20, start_y - 70, ops_color)
    draw_button_component('-', start_x + 20, start_y - 140, ops_color)
    draw_button_component('+', start_x + 20, start_y - 210, ops_color)

    draw_button_component('=', start_x - 50, start_y - 210, "orange") # Bên phải số 0
    draw_button_component('C', start_x - 190, start_y - 210, "pink")  # Bên trái số 0

def click_handler(x, y):
    global current_expression

    clicked_value = None
    for btn in buttons:
   
        if (btn['x'] <= x <= btn['x'] + 60) and (btn['y'] - 60 <= y <= btn['y']):
            clicked_value = btn['text']
            break
            
    if clicked_value:

        if clicked_value == '=':
            try:
                
                result = str(eval(current_expression))
                current_expression = result
            except:
                current_expression = "Error"
        elif clicked_value == 'C':
            current_expression = ""
        else:
            current_expression += clicked_value
            
        draw_group_a_display()


draw_group_a_display()


create_group_b_numbers()

create_group_c_operations()

wn.onscreenclick(click_handler)


wn.listen()
wn.mainloop()