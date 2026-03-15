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
    
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent
    
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        if self.percent <= 70:
            return True
        else:
            return False
    
    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: int) -> None:
        self.amount = amount
    
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        if product.price * 0.9 > self.amount:
            return True
        else:
            return False
    
    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount

product = Product('Wireless Mouse', 50.0)
print(product)
discount = PercentageDiscount(10)
print(discount.apply_discount(product))