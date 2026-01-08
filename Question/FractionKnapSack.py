class Item:
    def __init__(self, name, qty, profit):
        self.name = name
        self.qty = qty
        self.profit = profit
        self.ratio = profit / qty
        
def calculateMaxProfit(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_profit = 0
    result = []
    
    for item in items:
        if capacity >= item.qty:
            capacity -= item.qty
            total_profit += item.profit
            result.append((item.name, item.qty))
        else:
            fraction = capacity / item.qty
            total_profit += item.profit * fraction
            result.append((item.name, capacity))
            break
        
    return total_profit, result

items = [
    Item('A', 10, 60),
    Item('B', 5, 90),
    Item('C', 15, 40),
    Item('D', 8, 50),
]

capacity = 20

total_profit, result = calculateMaxProfit(items)

print("Total profit:", total_profit)
print("Items:", result)