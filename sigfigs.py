import numpy as np


def sig_figs(number): #requries number to be entered as a string

	if ('-' in number):	# deleting neg. sign, not important for sig figs and don't want to mess up character count
		number = number.replace("-", "")
	
	sigs = len(number)	# number of characters in string, max amount of sigfigs possible

	if ('.' in number):
		sigs -= 1
	i = 0 #iteration variable
	while (i < len(number)):
		if (number[i] != '.'):	
			if number[0] == '0':
				sigs -= 1
				number = number[1:]
				sig_figs(number)
			if number[-1] == '0':
				if ('.' not in number):
					sigs -= 1 
#					if sigs == 1:
						#return 1
					number = number[:-1]
					sig_figs(number)
				else:
					break
			else:
				break
		i += 1
		#sig_figs(number)		
	return sigs

print 'sig_figs(100.00) ', sig_figs('100.00')
print 'sig_figs(-100.00) ',sig_figs('-100.00')
print 'sig_figs(1000) ',sig_figs("1000")
print 'sig_figs(1000) ',sig_figs('1000')
print 'sig_figs(010001) ',sig_figs('010001')
print 'sig_figs(01000.) ',sig_figs('01000.')
print 'sig_figs(01000.0) ',sig_figs('01000.0')
print 'sig_figs(0.002) ',sig_figs('0.002')
print 'sig_figs(0.0020) ',sig_figs('0.0020')
print 'sig_figs(0.00203) ',sig_figs('0.00203')
print 'sig_figs(1203450) ',sig_figs('1203450')



