import os
import pwd
# https://docs.python.org/2.6/library/os.html#module-os
# https://docs.python.org/2/library/pwd.html
print "I will now show you how to figure out who you are:  %i, %s" % (1, "Idiot")
print "This guy is: '%s'" % pwd.getpwuid(os.getuid())[0]
