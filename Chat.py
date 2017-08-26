#initial prompting, basic raw_input to variable mapping
name = raw_input (" What is your name? ")
weight = raw_input (" How much do you weigh? ")
real_weight = raw_input (" No really, how much do you really weigh? ")
print " Hmm, ok lets see what I can do with that?"
# timing inserts pause for simulated thinking effect
import time
time.sleep(2)
print "Gimme a moment, I'm still crunching numbers"
time.sleep(2)

# variables for adjusting weight for us in function
honest_answer = int (real_weight) - 10
fudged_answer = int (real_weight) - 25

# this prompts user with basic menu and gives results
print "Ok %s, I recalculated," % name
print "Is %s better?" % (honest_answer)

def menu():
	menu = raw_input("1.) Yes \n2.) No\n")

	if menu == 1:
		moveforward()

	if menu == 2:
		recalculate()

	if raw_input != (1,2):
	 	print "That is not an option, Please choose 1 or 2"

def moveforward():
	print "Awesome, Lets move on then."

def recalculate():
	print "Picky, ok let's try again, is %s lbs better?" % (fudged_answer)

menu()
print "Alright so we've made some adjustments. Is this number any better?"
def menu():
	menu = raw_input("1.) Yes \n2.) No\n")

loop = True
while loop:
	if raw_input == 1:
		abouttime()

	elif raw_input == 2:
		letsmoveonagain()

	else:
		raw_input("That is not an option, Please input the numeral 1 or 2.")

	def abouttime():
		print "Geez, about time"

	def letsmoveonagain():
		print "Excellent, Glad I could find a number that works"
		time.sleep(3)
menu()

print ' Alright %s, so you "weigh" about %r. ' % (
name, honest_answer)

def menu():
	print ("are those numbers about right?")
	menu = raw_input("1.) Yes \n2.) No\n")

	if menu == 1:
		good()

	if menu == 2:
		bad()

def good():
	print ("Ok, based on those calculations I think you're pretty darned cool.")
	time.sleep(1)
	print "hope this made you smile"

def bad():
	print ("I am sorry if I offended you, I am going to leave now")

menu()
