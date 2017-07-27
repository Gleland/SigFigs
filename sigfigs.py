###################
# Garrett Thompson
# garrett.leland.thompson@gmail.com
# Sig fig calculator
# github.com/Gleland/SigFigs
###################


######################################
# Rules for Significant Figures
# non zero numbers are significant
# zeroes between non zeroes are significant
# zeroes before first non-zero digits are not significant
# zeroes after decimal *and* after a non-zero digit are significant
# zeroes in front of a decimal are significant (100.)
# zeroes after a non-zero without a decimal are not (1,200 == 2)
######################################


def count_sigfigs(number):

    # deleting neg. sign, not important for sig figs
    if ('-' in str(number)):     
        number = str(number).replace("-", "")
        isNegative = True 
    numb_list = list(str(number))

    if '.' in numb_list:
        decimal_location = numb_list.index('.')
        numb_list[decimal_location]='0'
        return has_decimal(numb_list,decimal_location)
    if '.' not in numb_list:
        return no_decimal(numb_list)
    else:
        print("Something broke")

def has_decimal(numb_list,decimal_location):

    for index,digit in enumerate(numb_list):
        if  digit !='0': 
            first_non_zero_location = index
            # First nonzero found, no need to keep iterating
            break
    if first_non_zero_location < decimal_location:
        # first non zero before decimal, all digits after are signficant
        #number of digits after 1st nonzero and excluding the decimal point.
        return len(numb_list)-first_non_zero_location-1

    if first_non_zero_location > decimal_location:
        # anything after the first NZ is significant
        return len(numb_list) - first_non_zero_location 

def no_decimal(numb_list):

    for index,digit in enumerate(numb_list):
        if  digit !='0': 
            first_non_zero_location = index
            # First nonzero found, no need to keep iterating
            break

    for index, digit in reversed(list(enumerate(numb_list))):
        if digit !='0':
            last_non_zero_location = index
            break

    #calculate number of digits between non zeros, inclusive
    return last_non_zero_location - first_non_zero_location + 1





test_list2=['100.0','-100.0','1000','01000.','01000.0','0.002','0.0020','0.00203','1203450']
test_list=['5420','-0.006700','0.06540','009009','90090']
for test in test_list: 
    print(repr(test),count_sigfigs(test))
for test in test_list2: 
    print(repr(test),count_sigfigs(test))
