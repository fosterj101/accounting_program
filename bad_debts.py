import numpy as np 

def net_receivables():
    ar = float(input('Enter Accounts Receivables Balance: '))
    q1 = input('Allowance for Doubtful Accounts Credit or Debit (c/d): ')
    if q1 == 'c':
        ada = float(input('Enter Allowance for Doubtful Accounts Credit: '))
    if q1 == 'd':
        ada = float(input('Enter Allowance for Doubtful Accounts Debit: '))
        ada = -1*ada
    w_off = float(input('Enter Amount Written off: '))

    nr = (ar - w_off) - (ada - 80)
    print('Net Receivables is: ',nr)

net_receivables()

