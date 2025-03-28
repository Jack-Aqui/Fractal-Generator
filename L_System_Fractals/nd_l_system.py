import random
from l_system import LSystem
from state import Stack
from state import State

class ND_LSystem(LSystem):
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
        # Same initial set up as original
        current_string = self.axiom
        for i in range(self.n):
            new_string = ""
            for char in current_string:
                if char in self.rules:
                    rule = self.select_rule(self.rules[char])
                    # Uses select_rule method to randomly choose rule to follow
                    new_string += rule
                else:
                    new_string += char
            current_string = new_string
        self.commands = current_string
        print(self.commands)

    def select_rule(self, rule_list):
        
        r = random.random()
        total_probability = 0.0
        for (probability, rule) in rule_list:
        # takes probability from and rule from list and determines if the rule will be used
            total_probability += probability
            if r < total_probability:
                return rule
        return rule_list[-1][1]
        # defaults to last rule if the r value exceeds the probability
    
  
if __name__ == "__main__":
    random.seed(42)

    nd_ls_1 = ND_LSystem(
        axiom="F",
        rules={"F": [(.33, "F[+F]F[-F]F"), (.33, "F[+F]F"), (.33, "F[-F]F")]},
        angle=25.7,
        step=10,
        n=4,
        starting_pos=(-200, 0),
        starting_angle=90,
        color="red"
    )
    nd_ls_1.plot()


