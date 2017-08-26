import time

name = raw_input ("Hi, What is your name?)
weight = raw_input("Quick question, How much do you weight?")
real_weight = raw_input("Mentirosa, How much do you really weight?")

print "Ok, lets see if i can't adjust that for you. Bear with me a moment"
time.sleep(2)
print "Gimme a moment please, I'm still crunching numbers"
time.sleep(2)

first_adjustment = int(real_weight) - 10
second_adjustment = int(real_weight) - 25

print " Ok %, I recalculated" % name
print "Is" first_adjustment "better?"

def print_menu():
    print "1. Menu Option 1"
    print "2. Menu Option 2"
