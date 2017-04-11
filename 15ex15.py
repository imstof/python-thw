from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file \"%r\":" % filename
print txt.read()

print "Type the filename again:"
#file_again = raw_input("8==> ")

#txt_again = open(file_again)

txt_again = open(raw_input("8==> "))

print 'The contents of "%s" are:\n%s' % (filename, txt_again.read())

print 'How many bytes to read?:'
size = raw_input("8==> ")
size = int(size)
print 'Size parameter "%d" does this:\n%s' % (size, txt_again.read(size))

txt.close()
txt_again.close()
