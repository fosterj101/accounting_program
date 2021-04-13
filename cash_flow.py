import numpy as np 


def cash_flow_indirect(net_income):
    op_net_cash = 0.0
    invest_net_cash = 0.0
    fin_net_cash = 0.0

    # Operating Activities
    da_expense = float(input('Enter Depre. & Amort. Expense: '))
    print(da_expense)
    op_net_cash += da_expense


    ar_begin, ar_end = input('Enter Accounts Receivable Balance (ending beginning): ').split()
    ar_diff = float(ar_end) - float(ar_begin)
    print(ar_diff)
    op_net_cash = op_net_cash + ar_diff
    

    inv_begin, inv_end = input('Enter Inventory Balance (ending beginning): ').split()
    inv_diff = float(inv_end) - float(inv_begin)
    print(inv_diff)
    op_net_cash = op_net_cash + inv_diff

    pe_begin, pe_end = input('Enter Prepaid Expense Balance (ending beginning): ').split()
    pe_diff = float(pe_end) - float(pe_begin)
    print(pe_diff)
    op_net_cash = op_net_cash + pe_diff
    
    ap_begin, ap_end = input('Enter Accounts Payable Balance (ending beginning): ').split()
    ap_diff = float(ap_end) - float(ap_begin)
    print(-1*ap_diff)
    op_net_cash = op_net_cash - ap_diff

    #### Interest Payable

    dr_begin, dr_end = input('Enter Deferred Revenue Balance (ending beginning): ').split()
    dr_diff = float(dr_end) - float(dr_begin)
    print(-1*dr_diff)
    op_net_cash = op_net_cash - dr_diff

    tp_begin, tp_end = input('Enter Taxes Payable Balance (ending beginning): ').split()
    tp_diff = float(tp_end) - float(tp_begin)
    print(-1*tp_diff)
    op_net_cash = op_net_cash - tp_diff

    ip_begin, ip_end = input('Enter Interest Payable Balance (ending beginning): ').split()
    ip_diff = float(ip_end) - float(ip_begin)
    print(-1*ip_diff)
    op_net_cash = op_net_cash - ip_diff

    ol_begin, ol_end = input('Enter Other Current Liabilities Balance (ending beginning): ').split()
    ol_diff = float(ol_end) - float(ol_begin)
    print(-1*ol_diff)
    op_net_cash = op_net_cash - ol_diff

    ae_begin, ae_end = input('Enter Accrued Expenses Balance (ending beginning): ').split()
    ae_diff = float(ae_end) - float(ae_begin)
    print(-1*ae_diff)
    op_net_cash = op_net_cash - ae_diff
    
    print(op_net_cash)

    op = net_income + op_net_cash
    if op_net_cash > 0:
        print('Net cash provided by operating activities: ', op)
     
    if op_net_cash < 0:
        print('Net cash used by operating activities: ', op)

    

    # Investing Activities
    ppe_p = float(input('Enter purchase of PPE: '))
    print(-1*ppe_p)
    invest_net_cash = invest_net_cash - ppe_p

    ppe_d = float(input('Enter disposal of PPE: '))
    print(ppe_d)
    invest_net_cash = invest_net_cash + ppe_d

    short_p = float(input('Enter purchase of short-term investment: '))
    print(-1*short_p)
    invest_net_cash = invest_net_cash - short_p

    short_s = float(input('Enter sale of short-term investment: '))
    print(short_s)
    invest_net_cash = invest_net_cash + short_s

    long_p = float(input('Enter purchase of long-term investment: '))
    print(-1*long_p)
    invest_net_cash = invest_net_cash - long_p

    long_s = float(input('Enter sale of long-term investment: '))
    print(long_s)
    invest_net_cash = invest_net_cash + long_s
    

    invest_net_cash
    if invest_net_cash > 0:
        print('Net cash provided by investing activities: ', invest_net_cash)
    if invest_net_cash < 0:
        print('Net cash used by investing activities: ', invest_net_cash)

    

    # Financing Activities
  

    common_stock = float(input('Enter stock issued: '))
    print(common_stock)
    fin_net_cash += common_stock

    div = float(input('Enter dividends payed: '))
    print(div)
    fin_net_cash -= div

    stock = float(input('Enter repurchase of treasury stock: '))
    print(-1*stock)
    fin_net_cash -= stock

    if fin_net_cash > 0:
        print('Net cash provided by financing activities: ', fin_net_cash)
    if fin_net_cash < 0:
        print('Net cash used by financing activities: ', fin_net_cash)

    net_income += op_net_cash
    net_income += invest_net_cash
    net_income += fin_net_cash

    if net_income > 0:
        print('Net increase in cash and cash equivalent: ', net_income)
    if net_income < 0:
        print('Net decrease in cash and cash equivalent: ', net_income)
    
    c_equi = float(input('Enter cash and cash equivalents at beginning of period: '))
    net_income = net_income + c_equi
    print('Cash and cash equivalents at end of period: ',net_income)


cash_flow_indirect(100000)






