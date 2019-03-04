"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Chloe Rife.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
charlie=rg.SimpleTurtle('turtle')
charlie.pen = rg.Pen('red', 5)
charlie.speed=20
for k in range(40):
    charlie.forward(k*5)
    charlie.right(44)
    charlie.forward(k/2)
    charlie.right(44)
randy=rg.SimpleTurtle('turtle')
randy.pen = rg.Pen('blue', 5)
randy.speed=20
randy.right(90)
for k in range(40):
    randy.forward(k*5)
    randy.right(44)
    randy.forward(k/2)
    randy.right(44)

window.close_on_mouse_click()