from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]
        # self.xcor = self.head.xcor()
        # self.ycor = self.head.ycor()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body = Turtle("square")
        self.body_segments.append(body)
        body.pen(pendown=False, pencolor="white", fillcolor="white")
        body.goto(position)

    def extend(self):
        self.add_segment(self.body_segments[-1].position())
        # for i in range(len(self.body_segments)):
        #     self.body_segments[i].color("red")
        #     self.body_segments[i-1].color("white")

    def move(self):
        for body_item in range(len(self.body_segments)-1, 0, -1):
            self.body_segments[body_item].goto(self.body_segments[body_item-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def coordinate(self):
        # return self.head.xcor()
        return self.head.pos()

    def change_xside(self):
        self.head.setpos(-self.head.xcor(), self.head.ycor())

    def change_yside(self):
        self.head.setpos(self.head.xcor(), -self.head.ycor())

    def left(self):
        self.head.left(90)

    def right(self):
        self.head.right(90)
