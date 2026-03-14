# Building a better discount calculator to show Python journey along with reinforcing learning on abstraction

from abc import ABC, abstractmethod

class Product:
    def __init__(self, name: str, price: float) -> None: # <-- Type hints
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"

class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass
product = Product('Wireless Mouse', 50.0)
print(product)