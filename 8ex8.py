# a variable containing formatters
formatter = "%r %r %r %r"

# print variable with different strings formatted
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# my own thang I'm curious about
varble = 1.09
print "python prints: %f" % varble

a = 10
b = 3.0
print "python prints: %f" % (a/b)
print "python prints: %.15f" % (a/b)
print "python prints: %.2f" % (a/b)
