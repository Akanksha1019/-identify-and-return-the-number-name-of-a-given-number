
names = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4':'four', '5':'five',
         '6':'six', '7':'seven', '8':'eight', '9':'nine',
         '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
         '15': 'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen',
         '20': 'twenty', '30': 'thirty', '40':'forty', '50':'fifty',
         '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}
_thousand = 'thousand'
_hundred = 'hundred'
_and = 'and'

def number_name(num):
    num = str(num)
    if len(num) > 4:
        return -1
    elif len(num) == 4:
        if num[1:] != '000':
            return -1
        return names[num[0]] + " " + _thousand
    elif len(num) == 3:
        if num[1:] == '00': return names[num[0]] + " " + _hundred
        txt = names[num[0]] + " " + _hundred + " " + _and + " "
        if 10 <= int(num[1:]) <= 19 or num[-1] == '0':
            txt += names[num[1:]]
        else:
            txt += names[num[1]+'0'] + " " + names[num[-1]]
        return txt
    elif len(num) == 2:
        txt = ''
        if 10 <= int(num) <= 19 or num[1] == '0':
            txt += names[num]
        else:
            txt += names[num[0]+'0'] + " " + names[num[1]]
        return txt
    else:
        return names[num]

i = int(input())
print(number_name(i)) 
