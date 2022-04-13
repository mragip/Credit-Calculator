import math
import argparse

parser = argparse.ArgumentParser(description = "Credit Calculator")

parser.add_argument("--type", type=str, help = "payment type")
parser.add_argument("--principal", type=int, default=0, help = "loan principal")
parser.add_argument("--periods", type=int, default=0, help = "months of payment")
parser.add_argument("--interest",type=float, default=0, help = "interest rate")
parser.add_argument("--payment", type=int, default=0, help = "monthly payment")

args = parser.parse_args()

def diff_payment(principal, periods, interest):
    m = 1
    sumpay = 0

    if interest == 0:
        return "Incorrect parameters"
        
    else:
        while m != periods +1:
            diff = math.ceil(principal / periods + (interest / 1200) * (principal - (principal * (m - 1)) / periods))
            print(f"month {m}: payment is {diff}")
            m+=1
            sumpay+=diff
        overpay = sumpay - principal    
        return f"Overpayment = {overpay}"

def annu_payment(principal, periods, interest):
    interest = interest / 1200
    payment = math.ceil(principal * ((interest *(1 + interest) ** periods) / ((1 + interest)**periods - 1)))
    Overpayment = payment * periods - principal
    return f"Your annuity payment = {payment}!\nOverpayment = {Overpayment}!"

def principal_pay(payment, periods, interest):
    interest = interest / 1200
    principal = math.ceil(payment / ((interest *(1 + interest) ** periods) / ((1 + interest)**periods - 1)))    
    return f"Your loan principal = {principal}!"

def periods_pay(principal, payment, interest):
    interest = interest / 1200
    periods = math.ceil(math.log((payment / (payment - interest * principal)), (1 + interest)))
    Overpayment = periods * payment - principal
    
    if periods % 12 == 0:
        
        return f"It will take {int(periods / 12)} years to repay this loan!\nOverpayment = {Overpayment}!"
    else:
        year = int(periods // 12)
        rem_mon = math.ceil(periods - year * 12)
        return f"It will take {year} years and {rem_mon} months to repay this loan!\nOverpayment = {Overpayment}!"
                
if args.type == "diff":    
    if __name__ == "__main__":
        print(diff_payment(args.principal, args.periods, args.interest))

elif args.type == "annuity":
    if args.principal !=0 and args.periods !=0 and args.interest != 0:
        if __name__ == "__main__":
            print(annu_payment(args.principal, args.periods, args.interest))

    elif args.payment !=0 and args.periods !=0 and args.interest !=0:
        if __name__ == "__main__":
            print(principal_pay(args.payment, args.periods, args.interest))

    elif args.principal !=0 and args.payment !=0 and args.interest !=0:
        if __name__ == "__main__":
            print(periods_pay(args.principal, args.payment, args.interest))
    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters")
    
    
