name = 'Christophe Ehnstrom'
age = 26 # liez
height = 74.0 # inches
weight = 190.0 # lbs. (gotta fix that)
eyes = 'Brown'
teeth = 'Yellow' # ish
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s because of the coffee." % teeth

print "If I (for some weird reason) add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

cm_height = height*2.54
kg_weight = weight*0.453592

print "His height in centimeters is %r." % cm_height
print "His weight in kilograms is %r." % kg_weight
print "His Body Mass Index is %r." % (kg_weight/(cm_height**1.0))

