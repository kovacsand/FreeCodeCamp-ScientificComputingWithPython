import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **contents):
    self.contents = []
    self.dictionary = contents
    for ball in contents:
      for amount in range(0, contents[ball]):
        self.contents.append(ball)  
  
  def draw(self, amount):
    if amount > len(self.contents):
      return self.contents
    drawn = []
    
    for i in range(amount):
      drawn.append(self.contents.pop(random.randrange(len(self.contents))))

    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  good_cases = 0
  
  for _ in range(num_experiments):
    drawn_balls = copy.deepcopy(hat).draw(num_balls_drawn)
    number_of_fulfilled_colours = 0
    
    for ball in expected_balls:
      number_of_fulfilled_colours += 1 if drawn_balls.count(ball) >= expected_balls[ball] else 0
    good_cases += 1 if number_of_fulfilled_colours == len(expected_balls) else 0

  return good_cases / num_experiments
