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


def sfCount(number):
    number = str(number).lower()
    # deleting neg. sign, not important for sig figs
    if ('-' in str(number)):     
        number = str(number).replace("-", "")
        isNegative = True 
    numb_list = list(str(number))

    if '.' in numb_list and 'e' not in numb_list:
        decimal_location = numb_list.index('.')
        numb_list[decimal_location]='0'
        return hasDecimal(numb_list,decimal_location)
    elif '.' not in numb_list:
        return noDecimal(numb_list)
    elif 'e' in numb_list:
        # exponential notation
        print("here!")
        return numb_list.index('e')-1
        #-1 for decimal place
    else:
        print("Something broke")

def hasDecimal(numb_list,decimal_location):

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

def noDecimal(numb_list):

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



def sfMult(number1,number2,operation):
        #return value with smallest sig figs
        sf1,sf2 = count_sigfigs(number1),count_sigfigs(number2)
        sigfig = min(sf1,sf2)
        evaluation = eval(number1+operation+number2)
        exp_string = "%.*e" %(sigfig-1,evaluation) 
        print("eval_str= ",exp_string)
        if "." in exp_string : 
            exp_string = exp_string.replace(".","")
        front_str,back_str = exp_string.split('e')
        exponent = int(back_str)
        print(front_str,back_str)
        if exponent == 0:
            print("no exponent")
            # no exponent, can truncate
            return front_str
        elif exponent > 0:
            print("pos. exponent")
            if exponent > len(front_str):
                print("exp>len(front_str") 
                # +1 for decimal place
                answer = front_str+(exponent-len(front_str)+1)*"0" 
            elif exponent < len(front_str):
                print("exp<len(front_str") 
                # have to add decimal back in
                answer = front_str[:1+exponent]+"."+front_str[1+exponent:]
            elif exponent == len(front_str):
                print("exp=len(front_str") 
                answer = front_str + "." 
        elif exponent < 0:
            print("neg. exp")
            answer =  "0." + (abs(exponent)-1)*"0" + front_str

        return answer

def sfAdd(number1,number2,operation):
        number1,number2 = str(number1).lower(),str(number2).lower()
        numb1,numb2 = number1,number2
        #return value with fewest decimal places 
        if "e" in number1: 
            numb1, _ = number1.split("e")
        if "e" in number2:
            numb2, _ = number2.split("e")
        if ("." in number1) and ("." in number2):
            temp1,temp2 = numb1.split("."),numb2.split(".")
            dec1,dec2 = len(temp1[-1]),len(temp2[-1])
            min_dec = min(dec1,dec2)
        else:
            min_dec=0
        # if this ^^ isn't met, then at least one number doesn't have a decimal
        evaluation = eval(number1+operation+number2)
        return "%.*f" %(min_dec,evaluation) 
        #return value with fewest decimal places
        


