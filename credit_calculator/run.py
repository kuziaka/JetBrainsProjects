import argparse
from banking_functions import *

parser = argparse.ArgumentParser(description="")

parser.add_argument('-t', '--type')
parser.add_argument('-p', '--payment')
parser.add_argument('-pr', '--principal')
parser.add_argument('-per', '--periods')
parser.add_argument('-int', '--interest')


def list_args():
    args_ = []
    for i in vars(parser.parse_args()).values():
        args_.append(i)
    return args_


args = list_args()
type_ = args[0]
payment = args[1]
principal = args[2]
periods = args[3]
interest = args[4]

if any((list_args().count(None) > 1, type_ not in ('diff', 'annuity'),
        type_ == 'diff' and payment)):
    print('Incorrect parameters')
else:
    if type_ == 'diff' and not payment:
        differential_get_payment(int(principal), float(interest), int(periods))
    elif type_ == "annuity" and not payment:
        annuity_get_payment(int(principal), float(interest), int(periods))
    elif type_ == "annuity" and not principal:
        annuity_get_principal(int(payment), float(interest), int(periods))
    else:
        annuity_get_periods(int(payment), float(interest), int(principal))
