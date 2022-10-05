from collections import defaultdict
from pprint import pprint

deals = {
    "deal_a": 1, 
    "deal_b": 2, 
    "deal_c": 2, 
    "deal_d": 3,
    "deal_e": 2
}

investors = {
    "investor_a": 1,
    "investor_b": 4,
    "investor_c": 3,
    "investor_d": 2,
    "investor_e": 1
}


def buy(deals, investors):
    print()
    print({"deals_available": deals})
    print({"investors": investors})
    print()

    purchases = defaultdict(dict)

    for inv_name in investors:
        for deal_name in deals.copy():
            if investors[inv_name] == 0:
                # print('investor has', investors[inv_name], 'money, moving on to next investor!') 
                break
            if investors[inv_name] < deals[deal_name]:
                # print('inv_name:', inv_name, 'inv_left_funds', investors[inv_name], 'not enough for deal:', deals[deal_name] )
                continue
            else:
                print(inv_name, 'with available funds', investors[inv_name], 'buys', deal_name, 'for', deals[deal_name])
                # update purchases
                purchases[inv_name][deal_name] = deals[deal_name]
                
                # update money left for current investor after purchase
                investors[inv_name] = investors[inv_name] - deals[deal_name]

                # remove purchased deals (using deals.copy() above)
                del deals[deal_name]
                
    print()
    return { "purchases_made": dict(purchases), "deals_updated": deals, "investors_updated": investors }


pprint(buy(deals, investors))
