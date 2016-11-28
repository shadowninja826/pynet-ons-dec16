
def soda_funct(x, y, z=20):
   return x + y + z

my_list = [22, 16, 10]
my_dict = {
    'x': 13,
    'y': 23,
    'z': 9,
}

print 
return_val = soda_funct(*my_list)
print "Calling with *args: {}".format(return_val)

print
return_val = soda_funct(**my_dict)
print "Calling with **kwargs: {}".format(return_val)
print

