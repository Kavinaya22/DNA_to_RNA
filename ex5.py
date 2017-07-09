name = 'kavinaya'
age = 12
height = 60
weight = 80
teeth = 'white'
hair = 'black'
eyes = 'brown'

print "Let's talk about %s" % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy for a 12 year old girl."
print "She has %s hair and %s eyes. She's so cute!" %(hair, eyes)
print "His teeth are mostly %s" % teeth

# tricky line  -   watch out!!
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight) 
