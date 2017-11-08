# CMPSC-121-Programs
The collection of python programs 

#Purpose:extimate credit card payments and inteseted giving yearly interest rate
#        for the credit card and new charges
#Input: yearly interest rate for the credit card as a percentage and new charges
#       and new payment 
#Output: total interest paid,minimum payment due and new current balance of
#        the user enter a payment.A credit will be output if the the user pays
#        more than the current balance
#Process: Ask the user o enter a yearly intesert rate for the credit card as
#         percentage also check the validity of the input
#         calculate and outputs the monthly interest on the previous balance
#         Ask the user to enter a new charges and check the validity
#         Calculate and outputs the current balance using
#         current balance= previous balance+monthly interest +new charges
#         calculate and output the minimum payment due using
#         minimum payment=7.5%*current balance or $10.00
#         Ask the user to enter a paymeny greater than or equal to the minimun
#         payment.
#         calculate the balance for the next month by subracting payment from
#         current balance.
#         output the total interest paid and if the user paid more than the current
#         balance, the output a credit.
#         repeat the loop for the second month until the payment is clear


def main():
    yearly=float(input("What is the yearly interest rate fot the credit card?"))
    while yearly<1 or yearly>30:
            print("Please enter a valid yearly interest greater than 1% and\
less than 30%")
            yearly=float(input("What is the yearly interest rate fot the credit card?"))

    monthly=yearly/12
    prebalance=0.00
    totalint=0

    
    while prebalance>=0.00:
        
       
        interest=float(format(prebalance*monthly/100, '.2f'))
        
        inte=roundn(interest)#function call
        
        print('The balance from the previous month was $',format(prebalance,'.2f'),sep='')
        print("There was $",format(inte,'.2f')," in interest applied to yout account last month",sep='')
        
        newcharge=int(input("What were the total charges for this month"))
        while newcharge<0:
            print('You cannot have a negtive charge!')
            newcharge=int(input("What were the total charges for this month"))
            
        curbalance=prebalance+inte+newcharge
        
        print("Your current balance is $",format(curbalance,'.2f'),sep='')
        if curbalance<10:  
            minimum=curbalance
        elif curbalance>10 and curbalance*0.075<=10:
            minimum=10
        elif curbalance>10 and curbalance*0.075>10:
            minimum=curbalance*0.075

        minimx=float(format(minimum, '.2f'))
            
        minp=roundn(minimx)# function call
        
        print("The minumum payment for this month is $",format(minp,'.2f'),sep='')
        payment=float(input("How much would you like to pay this month?"))
        while payment<minimum:
                print("Please make a payment greater or equal to minimum payment")
                payment=float(input("How much would you like to pay this month?"))

        totalint=totalint+inte
        
        
        prebalance=curbalance-payment
        
        if prebalance<=0:
            print("Your account has been paid off! You paid a total of $",format(totalint,'.2f'),'in interest')

        credit=prebalance*-1
         
        if credit>0:
            print('and you have a credit of $',format(credit,'.2f'),sep='')

#function to round amounts to the current cent
#input: interest and the minimum payment passed by function call
#output: the interest and the minimu payment rounded to current cent returned to function call
#processing: determin the integer amount of the entered number mutiplied by 100 and plus 0.5
#            multiply the integer by 0.01 and return the value
def roundn(value):
        roundr=value*100+0.5
        roundr2=int(roundr)
        roundr3=roundr2*0.01
        roundr4=float(format(roundr3,'.2f'))
        return roundr4
            

main()
              
