from calculator import Calculator
from testableCalculator import TestableCalculator
from returnerOutput import ReturnerOutput
from printerOutput import PrinterOutput

#shows testability principle using simplistic strategy (for teaching)


# non testable class
c = Calculator()

#add 
c.dodaj(10, 2)

#substract
c.odejmij(10, 2)

#we are checking if the class does what we expect
if(c.dodaj(10, 2) != c.dodaj(2,10) or c.dodaj(2,10) != 12):
	print "somethings wrong with adding"
	
if(c.dodaj(10, -10) != 0):
	print "something wrong with substracting"

# both the statements will print errors as the class does not return the values
# just prints them	
	
	
# for making things easier we can use simple helper functions
# almost identical ones are used by testing frameworks (assetEquas, assertTrue, assertFalse and so on...)
def assertEquals(expected, actual, message):
	if(expected != actual):
		print message

# creating two strategies
printer = PrinterOutput()
returner = ReturnerOutput()

# we can choose at object creation which stratego to use
tc = TestableCalculator(returner)

# classic unit test example
# we test the values we expect to be output
# and the values that the program will actually generate
# and when something goes wrong, print an error message
assertEquals("a + b = 12", tc.dodaj(10,2), "Addition error, should be 12")
assertEquals("a - b = 7", tc.odejmij(10,3), "Substraction error, should be 7")

