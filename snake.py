from turtle import Turtle

STARTING_POS = [(0, 0), (-40, 0), (-80, 0)]  # SET THE DEFAULT STARTING POSITIONS
MOVE_DIST = 5  # SET THE DEFAULT MOVING SPEED
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for each_pos in STARTING_POS:
            self.add_segment(each_pos)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())  # add after the position of the last segment

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):  # go from last segment to the first one
            new_x = self.snake[seg_num - 1].xcor()  # get the coordinates of the next to last segment
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DIST+len(self.snake)/2)  # move the head of the snake forward

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake:
            seg.goto(0, 1000)  # move the old snake out of screen

        self.snake.clear()  # delete the old snake
        self.create_snake()
        self.head = self.snake[0]
