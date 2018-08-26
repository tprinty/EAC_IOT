import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)   # Set pin 10 to be an output pin and set initial value to low (off)


# Alphabets and their relative Morse Symbols
# Assigning all this in a Python Dictionary : Code_Symbol
Code_Symbol = {'A': '.-', 'B': '-...', 'C': '-.-.', 
 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I': '..',
 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---',
 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..',
 
 '0': '-----', '1': '.----', '2': '..---',
 '3': '...--', '4': '....-', '5': '.....',
 '6': '-....', '7': '--...', '8': '---..',
 '9': '----.' 
 }



def main():
	while 1:
	 input_msg = raw_input('Enter your Message: ')
	 for char in input_msg:
		if char == " ":
			sleep(.5)
		else:
			code = Code_Symbol[char.upper()]
       			for c in code:
				print "Code is "+ c
				if c == ".":
					GPIO.output(8, GPIO.HIGH)
					sleep(.2)
       					GPIO.output(8, GPIO.LOW)
				if c == "-":
					GPIO.output(10, GPIO.HIGH)
					sleep(.2)
					GPIO.output(10, GPIO.LOW)
				sleep(.3)


if __name__ == "__main__":
 main()
