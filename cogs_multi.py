def costing_methods_m():

    p_list = []
    c_list = []

    ## Beginning Inventory
    bi = float(input('beginning inventory units: '))
    p_list.append(bi)
    bi_c = float(input('beginning inventory cost: '))
    c_list.append(bi_c)

    ## Revenue
    units_sold = float(input('How many units sold: '))
    units_sold_p = float(input('Price: '))
    revenue = units_sold * units_sold_p
    
    ## Beginning Inventory Total Cost
    bi_tc = bi * bi_c

    p1_u = float(input('purchase 1 units: '))
    p_list.append(p1_u)
    p1_c = float(input('purchase 1 cost: '))
    c_list.append(p1_c)

    p2_u = float(input('purchase 2 units: '))
    p_list.append(p2_u)
    p2_c = float(input('purchase 2 cost: '))
    c_list.append(p2_c)

    p3_u = float(input('purchase 3 units: '))
    p_list.append(p3_u)
    p3_c = float(input('purchase 3 cost: '))
    c_list.append(p3_c)

    p4_u = float(input('purchase 4 units: '))
    p_list.append(p4_u)
    p4_c = float(input('purchase 4 cost: '))
    c_list.append(p4_c)



    ## Goods Available for Sale
    goods_a = sum(p_list)
    print('\nGoods Available for Sale (units): ', goods_a)
    goods_a_c = bi_tc + (p1_u*p1_c) + (p2_u*p2_c) + (p3_u*p3_c) + (p4_u*p4_c)
    print('Goods Available for Sale (total cost): ', goods_a_c)





    ## COGS

    # FIFO
    
    cogs_fifo = 0
    out_fifo = 0
    i = 0
    while units_sold >= out_fifo:
        out_fifo += p_list[i]
        cogs_fifo += p_list[i]*c_list[i]
        i += 1
    
    i-=1

    cogs_fifo = (cogs_fifo - float(p_list[i]*c_list[i])) + (-1*(out_fifo - units_sold - float(p_list[i])))*(float(c_list[i]))
    

    
    '''    
    if diff_fifo >= 0:
        fifo_ei = (recent * recent_c) + (diff_fifo * first_c)
    if diff_fifo < 0:
        fifo_ei = ei * recent_c
    cogs_fifo = goods_a_c - fifo_ei
    print('\nEnding Inventory in FIFO: ', fifo_ei)
    print('COGS (FIFO): ', cogs_fifo)

    # LIFO
    diff_bi = bi - ei
    diff_first = first + diff_bi
    if diff_bi >= 0:
        lifo_ei = ei * bi_c
    if diff_bi < 0 and diff_first >= 0:
        lifo_ei = (bi * bi_c) + (first_c * (-1*diff_bi))
    if diff_first < 0:
        lifo_ei = (bi * bi_c) + (first_c * first) + (recent_c * (-1*diff_first))

    cogs_lifo = goods_a_c - lifo_ei
    print('\nEnding Inventory in LIFO: ', lifo_ei)
    print('COGS (LIFO): ', cogs_lifo)

    '''

    # Weighted Average
    cost_per_unit = goods_a_c / goods_a
    cogs_avg = units_sold * cost_per_unit

    print('\nRevenue: ',revenue)

    print('\nCOGS in FIFO: ',cogs_fifo)
    print('COGS (Average Costing): ', cogs_avg)

    ## Gross Profit 
    gross_p_fifo = revenue - cogs_fifo
    print('\nGross profit in FIFO: ', gross_p_fifo)

    ## Ending Inventory 
    ei_fifo = (out_fifo - units_sold)*c_list[i]
    print('Ending Inventory FIFO: ', ei_fifo)
    ei_avg = -1*(cost_per_unit * (units_sold-goods_a))
    print('Ending Inventory in Average Costing: ', ei_avg)
    

costing_methods_m()

