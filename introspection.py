# introspection
# http://www.diveintopython.net/power_of_introspection/built_in_functions.html
f = 1
print "type of %i " % f + "is: "
print type(f)

print "Some stuff about %i " % f + "is: "
print dir(f)

lst = [1,2,2,3]

print type(lst)
print dir(lst)
print lst.pop()
print lst.pop()
