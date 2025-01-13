# module =  a file containg code that u wnat to include in your programme.
#  use 'import' to include a module
# useful to breakup large prog into reusable seperate files.

# here create example.py module and import here

print(help("modules"))  # to show all modules
print(help("math"))   # to see math module info

import example as ex

print(ex.my_var)

print(ex.square(4))

print(ex.cube(4))