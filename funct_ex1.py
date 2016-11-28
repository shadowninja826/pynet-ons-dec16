
def soda_funct(x, y, z=20):
    return x + y + z

print
return_val = soda_funct(10, 20, 30)
print "Calling with 3 positions arg: {}".format(return_val)

return_val = soda_funct(x=10, y=20)
print "Calling with 2 named arg: {}".format(return_val)

return_val = soda_funct(10, z=13, y=22)
print "Calling with one pos and 2 named: {}".format(return_val)

return_val = soda_funct(x='x', y='y', z='z')
print "Calling with 3 strings: {}".format(return_val)

return_val = soda_funct(x=['x'], y=['y'], z=['z'])
print "Calling with 3 list:{}".format(return_val)
