import numpy as np


def sig_figs(number): #requries number to be entered as a string

	if ('-' in number):	# deleting neg. sign, not important for sig figs and don't want to mess up character count
		number = number.replace("-", "")
	
	sigs = len(number)	# number of characters in string, max amount of sigfigs possible

	if ('.' in number):
		sigs -= 1
	i = 0 
	while i < len(number):
		if (number[i] != '.'):	
			if number[0] == '0':
				sigs -= 1
				number = number[1:]
				sig_figs(number)
			if number[-1] == '0':
				if ('.' not in number):
					sigs -= 1 
					number = number[:-1]
					sig_figs(number)
				else:
					break
			else:
				break
		i += 1
	return sigs
def new_func(number):
    # have to accurately calculate sig figs before calculations are done

        # non zero numbers are significant
        # zeroes between non zeroes are significant (101,202, etc)
        # zeroes before the first non-zero digits are not significant (0.001,020, etc)
        # zeroes after the decimal *and* after a non-zero digit are significant (3.200 == 4)
        # zeroes in front of a decimal are significant (100.)
        # zeroes after a non-zero without a decimal are not (1,200 == 2)
       isNegative = False 
	if ('-' in number):	# deleting neg. sign, not important for sig figs and don't want to mess up character count
		number = number.replace("-", "")
                isNegative = True 
        sigfigs = len(number)
        if ('.' is in number):
            decimalIndex = number.index('.')

        for range(sigfigs):
            # iterate over each digist and adjust number of sig figs accordingly




print 'sig_figs(100.00) ', sig_figs('100.00')
print 'sig_figs(-100.00) ',sig_figs('-100.00')
print 'sig_figs(1000) ',sig_figs("1000")
print 'sig_figs(010001) ',sig_figs('010001')
print 'sig_figs(01000.) ',sig_figs('01000.')
print 'sig_figs(01000.0) ',sig_figs('01000.0')
print 'sig_figs(0.002) ',sig_figs('0.002')
print 'sig_figs(0.0020) ',sig_figs('0.0020')
print 'sig_figs(0.00203) ',sig_figs('0.00203')
print 'sig_figs(1203450) ',sig_figs('1203450')



