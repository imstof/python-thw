import time

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a \"list\":
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

thin_cat = '''
I'll do another "list":
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print thin_cat

b=0
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s %d\r" % (i,b),
#		time.sleep(1)  # not sure why this breaks
		b+=1
	if b>=1000000:
		break

"""
while True:
	print "wait 5"
	time.sleep(5)
"""
