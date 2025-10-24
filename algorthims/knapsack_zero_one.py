from random import randint as rnd
import copy

N = 7 # number of items
MAX_WEIGHT = 15 # maximum weight
objects = [(10,2),(5,3),(15,5),(7,7),(6,1),(18,4),(6,1)]
# objects = None
epoch = 20

class Item:
    __slots__ = ("profit", "weight")
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        

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

def random_picker(items, max_weight):
    offset = max_weight
    bag = []
    items = [item for item in items if item.weight <= offset]
    while any(map(lambda x: True if x.weight <offset else False, items)):
        length = len(items) -1
        random_item = rnd(0, length)
        offset -= items[random_item].weight
        bag.append(items[random_item])
        items.remove(items[random_item])
        items = [item for item in items if item.weight <= offset]
    return bag  
    
    
def fitness(bag):
    total_profit = 0
    for item in bag:
        total_profit += item.profit
    return total_profit
        
    
if __name__ == "__main__":
    items = get_items(N, objects)
    best_profit = 0
    best_bag = []
    while epoch:
        new_bag = random_picker(items, MAX_WEIGHT)
        profit = fitness(new_bag)
        if best_profit<profit:
            best_profit = profit
            best_bag = copy.deepcopy(new_bag)
            print("best bag profit", best_profit)
            print("best bag weight", sum(map(lambda x: x.weight, best_bag)))
            print("-------------------------------")
        epoch -= 1