# -*- coging: utf-8 -*-

name = 'Robert'
age = 24
height = 191  # centimeters
weight = 90  # kilograms
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print 'Let\'s talk about %s' % name
print "He's %d centimeters tall." % height
print "He's %f kilograms heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)


print "He's weight in pounds is %f" % (weight / 0.45359237)
print "He's height in inches is %f" % (height / 2.54)
