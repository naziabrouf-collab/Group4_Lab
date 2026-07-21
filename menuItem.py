class MenuItem:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f}"
