from turtle import *

speed(10)
bgcolor("black")
pencolor("blue")

def pattern():
  for i in range(5):
    forward(50)
    right(40)
  forward(50)
  left(40)
  for i in range(4):
    forward(50)
    right(40)
  forward(50)
  left(90)
  forward(50)

for count in range(30):
  pattern()

mainloop()
