from optparse import OptionParser

parser = OptionParser()
# set short tag "-c" and long tag "--color"
# "color" is the name of the variable where input is stored
# "red" is the default value if no input is given
parser.add_option("-c", "--color", dest="color", default="red",
                  help="select which color balls robot should seek")

# .parse_args() returns list whose first element
# is an object storing the user's options as its instace variables
print parser.parse_args()[0].color
# prints: red

