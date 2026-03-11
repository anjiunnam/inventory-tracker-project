class InventoryTracker:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity

    def display_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

    def checkStockLevel(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        return "Item not found"

    def alertLowStock(self, threshold=5):
        low_stock_items = []
        for item, quantity in self.items.items():
            if quantity < threshold:
                low_stock_items.append(item)
        return low_stock_items
