# Building a better discount calculator to show Python journey along with reinforcing learning on abstraction

from abc import ABC, abstractmethod

class Product:
    """ Represents a product with a name and price """
    
    def __init__(self, name: str, price: float) -> None: # <-- Type hints
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"

class DiscountStrategy(ABC):
    """ Abstract base class defining the interface for all discount strategies """
    
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """ Check if the discount can be applied to the given product and user tier """
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        """ Calculate and return the discount price """
        pass
    
class PercentageDiscount(DiscountStrategy):
    """ Applies a percentage-based discount, capped at 70% """
    
    def __init__(self, percent: int) -> None:
        self.percent = percent
    
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        if self.percent <= 70:
            return True # <-- Only allow discounts up to 70%
        else:
            return False
    
    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    """ Applies a fixed amount dicsount, only when discount is less than 10% of price """
    
    def __init__(self, amount: int) -> None:
        self.amount = amount
    
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        if product.price * 0.9 > self.amount:
            return True # <-- Ensure the discount doesn't exceed 10% of the product price
        else:
            return False
    
    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount
    
class PremiumUserDiscount(DiscountStrategy):
    """ Applies a 20% discount exclusively for premium tier users """
    
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        if user_tier.lower() == 'premium':
            return True
        else:
            return False
        
    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8
    
class DiscountEngine:
    """ Returns the minimum price for user_tiers """
    
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies
        
    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]
        
        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)
        
        return min(prices)

# --- Usage Examples ---
if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'
    strategies = [PercentageDiscount(10), FixedAmountDiscount(5), PremiumUserDiscount()]
    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)
    
    print(f"Best price for {product.name} for {user_tier} user: ${best_price:.2f}")
    
# print(product)

# discount = PercentageDiscount(10)
# print(discount.apply_discount(product))

# fixed_discount = FixedAmountDiscount(5)
# print(fixed_discount.apply_discount(product))

