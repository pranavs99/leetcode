def maxProfit(self, prices: List[int]) -> int:
    # since we can make as many transactions as we like,
    # all strictly increasing sublists are optimal transactions,
    # so we keep adding each strictly increasing sublist's range
    # to total_profit
    
    # limit for list
    n_days = len(prices)
    
    # keeping track of profits
    total_profit = 0
    curr_profit = 0
    
    # keeping track of last-observed price so that we can determine
    # when there's a price decrease (which means we need to cut off
    # the current sublist)
    last_price = prices[0]
    
    i = 1
    while i < n_days:
        # decrease in price means cut off current sublist, add the
        # collected curr_profit to total_profit, and reset curr_profit
        if prices[i] < last_price:
            total_profit += curr_profit
            curr_profit = 0
        # anything else means keep proceeding with the current sublist
        else:
            curr_profit += (prices[i] - last_price)
            
        last_price = prices[i]
        i += 1
    
    # edge case:
    # if we reach the end of the list without hitting a price decrease,
    # then we need to add curr_profit to total_profit just to make sure
    # we've taken care of the last transaction
    total_profit += curr_profit
    
    return total_profit