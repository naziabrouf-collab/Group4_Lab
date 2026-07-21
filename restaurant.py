class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.order_list = []

    def add_menu_item(self, item: MenuItem):
        self.menu_items.append(item)

    def display_menu(self):
        print("\n--- RESTAURANT MENU ---")
        for index, item in enumerate(self.menu_items, start=1):
            print(f"{index}. {item}")

    def add_order(self, item_number: int) -> bool:
        if 1 <= item_number <= len(self.menu_items):
            selected_item = self.menu_items[item_number - 1]
            self.order_list.append(selected_item)
            print(f"--> Added '{selected_item.get_name()}' to your order.")
            return True
        else:
            print("Invalid item number. Please try again.")
            return False

    def calculate_total(self) -> float:
        return sum(item.get_price() for item in self.order_list)

    def display_order(self):
        print("YOUR ORDER SUMMARY: ")
        if not self.order_list:
            print("Your cart is empty.")
            return

        for index, item in enumerate(self.order_list, start=1):
            print(f"{index}. {item.get_name()} - ${item.get_price():.2f}")
        
        total = self.calculate_total()
        print(f"TOTAL PRICE: ${total:.2f}")

    def clear_order(self):
        self.order_list.clear()
