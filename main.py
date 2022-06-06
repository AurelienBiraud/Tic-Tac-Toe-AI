import turtle

def other(piece):
   if piece == "x":
       return "o"
   else:
       return "x"

def is_win(state, piece):
   for row in state:
       if row == [piece] * 3:
           return True
   for j in range(3):
       threeinarow = True
       for i in range(3):
           if state[i][j] != piece:
               threeinarow = False
       if threeinarow:
           return True
   if state[0][0] == piece and state[1][1] == piece and state[2][2] == piece:
       return True
   if state[2][0] == piece and state[1][1] == piece and state[0][2] == piece:
       return True
   return False

def evaluation(state):
   if is_win(state, "x"):
       return 1
   if is_win(state, other("x")):
       return 0
   return 0.5


def copy(state):
   return [row.copy() for row in state]


def successor(state, piece):
   children = []
   for i in range(3):
       for j in range(3):
           if state[i][j] == "":
               child = copy(state)
               child[i][j] = piece
               children.append(child)
   return children

def value(state, piece, successor, evaluation, depth, maxdepth):
   if depth == maxdepth:
       return evaluation(state)
   child_values = []
   children = successor(state, piece)
   if len(children) == 0:
       return evaluation(state)
   for child in children:
       child_values.append(value(child, other(piece), successor, evaluation, depth + 1, maxdepth))
   if piece == "x":
       return max(child_values)
   else:
       return min(child_values)


def minimax(state, piece, successor, evaluation, maxdepth):
   child_values = []  
   children = successor(state, piece) 
   for child in children:
       child_values.append(
           value(child, other(piece), successor, evaluation, 0, maxdepth))  
   max_val = child_values[0] 
   max_child = children[0]
   for i in range(1, len(children)):
       if piece == "x":
           if child_values[i] > max_val: 
               max_val = child_values[i]
               max_child = children[i]
       else:
           if child_values[i] < max_val:  
               max_val = child_values[i]
               max_child = children[i]

   return max_child

def background():
   turtle.penup()
   turtle.goto((-100, 300))
   turtle.pendown()
   turtle.seth(270)
   turtle.forward(600)

   turtle.penup()
   turtle.goto((100, 300))
   turtle.pendown()
   turtle.seth(270)
   turtle.forward(600)

   turtle.penup()
   turtle.goto((-300, -100))
   turtle.pendown()
   turtle.seth(0)
   turtle.forward(600)

   turtle.penup()
   turtle.goto((-300, 100))
   turtle.pendown()
   turtle.seth(0)
   turtle.forward(600)

def placepiece(piece, x, y):
   if piece == "x":
       turtle.pu()
       turtle.goto((-200 + 200 * x, 200 - 200 * y))
       turtle.pendown()
       turtle.seth(45)
       turtle.forward(100)
       turtle.backward(200)
       turtle.forward(100)
       turtle.seth(135)
       turtle.forward(100)
       turtle.backward(200)
       turtle.forward(100)
   else:
       turtle.penup()
       turtle.goto((-200 + 200 * x, 200 - 200 * y))
       turtle.seth(0)
       turtle.forward(75)
       turtle.pendown()
       turtle.seth(90)
       turtle.circle(75)
   turtle.update()


grid = [["", "", ""],
        ["", "", ""],
        ["", "", ""]]
piece = "x"

difficulty = 1


def display():
   turtle.clear()
   background()
   for x in range(3):
       for y in range(3):
           if grid[y][x] != "":
               placepiece(grid[y][x], x, y)

   turtle.update()


canmove = True

def on_click(x, y):
   print(x, y)
   global canmove
   if canmove:
       canmove = False
       i, j = 0, 0
       if x < -100:
           i = 0
       elif x > 100:
           i = 2
       else:
           i = 1

       if y < -100:
           j = 2
       elif y > 100:
           j = 0
       else:
           j = 1
       global grid
       global piece
       if grid[j][i] == "":
           grid[j][i] = piece
           display()
           if is_win(grid, piece):
               turtle.penup()
               turtle.goto((0, 0))
               turtle.pendown()
               turtle.write("Winner Winner Chicken Dinner", align="center", font=("Arial", 50, "normal"))
               turtle.done()
           piece = other(piece)
           move = minimax(grid, piece, successor, evaluation, difficulty)
           grid = move
           display()
           if is_win(grid, piece):
               print("YA LUSE")
               exit(0)
           piece = other(piece)
       canmove = True

       pen = turtle.Turtle()
       pen.speed(0)
       pen.shape("square")
       pen.color("black")
       pen.penup()
       pen.hideturtle()
       pen.goto(0, 300)
       pen.write("Tic Tac Toe AI", align="center", font=("Courier", 24, "normal"))
       pen2 = turtle.Turtle()
       pen2.speed(0)
       pen2.shape("square")
       pen2.color("black")
       pen2.penup()
       pen2.hideturtle()
       pen2.goto(275, -320)
       pen2.write("By Aurelien Biraud", align="center", font=("Courier", 10, "normal"))
       pen2 = turtle.Turtle()
       pen2.speed(0)
       pen2.shape("square")
       pen2.color("blue")
       pen2.penup()
       pen2.hideturtle()
       pen2.goto(275, 320)
       pen2 = turtle.Turtle()
       pen2.speed(0)
       pen2.shape("square")
       pen2.color("red")
       pen2.penup()
       pen2.hideturtle()
       pen2.goto(-250, -320)

turtle.ht()
turtle.tracer(0, 0)
turtle.onscreenclick(on_click)

display()





