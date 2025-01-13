

print(__name__)

from  script2 import *   # script2 codes comes/includes here..it also has __name__
# here __name__ is available 2 times..one actual main and other from import from specific script

# __name__ in current script is __main__
# for imported scripts here __name__ is their script name


# run specific main code when we run that specific script only