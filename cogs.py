def costing_methods():
    bi = float(input('beginning inventory units: '))
    bi_c = float(input('beginning inventory cost: '))
    first = float(input('first purchase units: '))
    first_c = float(input('first purchase cost: '))
    recent = float(input('most recent purchase units: '))
    recent_c = float(input('most recent purchase cost: '))
    ei = float(input('ending inventory units: '))
    
    ## Beginning Inventory Total Cost
    bi_tc = bi * bi_c
    print('\nBeginning Inventory Total Cost: ', bi_tc)

    ## Goods Available for Sale
    goods_a = bi + first + recent
    print('\nGoods Available for Sale (units): ', goods_a)
    goods_a_c = bi_tc + (first*first_c) + (recent*recent_c)
    print('Goods Available for Sale (total cost): ', goods_a_c)
    
    ## Sales
    sales = goods_a - ei
    print('\nTotal Sales (units): ', sales)
    purchase_sales = sales - bi
    print('Sales From Purchased Goods (units): ', purchase_sales)


    ## Ending Inventory 
    # FIFO
    diff_fifo = ei - recent 
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

    # Average Cost
    weighted_average_cost = goods_a_c / (bi + first + recent)
    avg_cost_ei = weighted_average_cost * ei

    cogs_avg = goods_a_c - avg_cost_ei
    print('\nEnding Inventory in Average Costing: ', avg_cost_ei)
    print('COGS (Average Costing): ', cogs_avg)



costing_methods()

