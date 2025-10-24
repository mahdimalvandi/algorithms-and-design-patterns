N = 7 # number of items
MAX_WEIGHT = 15 # maximum weight
objects = [(10,2),(5,3),(15,5),(7,7),(6,1),(18,4),(3,1)]
# objects = None
epoch = 20

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.value = profit/weight
        
        
        
def get_items(n, input_items=None, verbos=0):
    items = []
    if input_items is None:
            for i in range(n):
                print(f"Items #{i+1}")
                item_profit = int(input("Enter Profit"))
                item_weight = int(input("Enter Weight"))
                items.append(Item(item_profit, item_weight))
    else :
        for item in input_items:
            items.append(Item(item[0], item[1]))
        
    if verbos:
        for item in items:
            print(f"item #{items.index(item)+1}: profit:{item.profit} weight:{item.weight}")

    return items


def get_best_item(items):
    best_item_value = 0
    best_item = None
    for item in items:
        if item.value > best_item_value:
            best_item_value = item.value
            best_item = item
    return best_item



if __name__ == "__main__":
    items = get_items(N, objects)

    bag = []
    offset = MAX_WEIGHT

    while True:
        best_item = get_best_item(items)
        if best_item.weight < offset:
            offset -= best_item.weight
            bag.append({"item": best_item, "real_profit": best_item.profit, "real_weight":best_item.weight})
            items.remove(best_item)

        else:
            profit = best_item.profit
            weight = best_item.weight
            real_profit = (profit * offset)/weight
            real_weight = offset
            offset = 0
            bag.append({"item": best_item, "real_profit": real_profit, "real_weight":real_weight})
            break

    profits = sum(map(lambda x: x["real_profit"], bag))
    for item in bag:
        print(f"profit:{item["real_profit"]} weight:{item["real_weight"]}")

    print(profits)