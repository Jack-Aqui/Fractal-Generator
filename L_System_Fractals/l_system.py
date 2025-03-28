import turtle as t
from state import State
from state import Stack
class LSystem:
    """
    Represents an L-system with its axiom, rules, rewriting,
    and drawing methods.
    """
    def __init__(self, axiom, rules, angle, step, n=3,
    starting_pos=(-200, 0), starting_angle=0, color="blue"):
        # Initialize variables
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.step = step
        self.n = n
        self.starting_pos = starting_pos
        self.starting_angle = starting_angle
        self.color = color
        self.commands = self.axiom
        self.stack = Stack()
        
    
    def iterate(self):
        original_string = self.axiom
        # Iterate through string and replace it with the rules
        for i in range(self.n):
            new_string = ""
            for char in original_string:
                if isinstance(self.rules.get(char,char), str):
                    new_string += self.rules.get(char,char)
            original_string = new_string
            # Set the commands to the ruls
        self.commands = original_string

    def draw(self):
        # Initialize turtle setup
        t.speed(150)
        t.penup()
        t.goto(self.starting_pos)
        t.setheading(self.starting_angle)
        t.color(self.color)
        t.pendown()


        for command in self.commands:
            # Operations performed in response each command
            if command == 'F':
                t.pendown()
                t.forward(self.step)
            elif command == 'f':
                t.penup()
                t.forward(self.step)
                t.pendown()
            elif command == '+':
                t.left(self.angle)
            elif command == '-':
                t.right(self.angle)

            elif command == '[':
                state = State(t.xcor(), t.ycor(), t.heading())
                self.stack.push(state)
                # Saves state

            elif command == ']':
                    state = self.stack.pop()
                    t.penup()
                    t.goto(state.x, state.y)
                    t.setheading(state.angle)
                    t.pendown()
                # Applies State
                    
        t.done()

    def plot(self):
        self.iterate()
        self.draw()
        

def main():
    ls = LSystem(
        axiom="-L",
        rules={"L":"LF+RFR+FL-F-LFLFL-FRFR+",
               "R": "- LFLF+RFRFR+F+RF-LFL-FR"},
        angle=90,
        step=10,
        n=3,
        starting_pos=(-200, 0),
        starting_angle=90,
        color="blue"
        
    )
    ls.plot()

if __name__ == "__main__":
    main()