# 📁 Discount Calculator V2
> A redesigned discount system using abstraction, the strategy design pattern, and type hints, built to show Python progression from the original Discount Calculator.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This project is a deliberate revisit of the earlier Discount Calculator, rebuilt from scratch using advanced OOP concepts. Where the original used a single function with `if/elif` validation, this version uses an abstract base class to define a discount interface, three interchangeable strategy classes that implement it, and a `DiscountEngine` that finds the best available price across all strategies. It was built to practice abstraction, the Strategy design pattern, and type hints.

## 🧠 What I Learned

- **Abstract Base Classes with `ABC` and `@abstractmethod`** — Using from `abc import ABC`, `abstractmethod` to define a `DiscountStrategy` interface that all discount types must implement, making the contract between classes explicit and enforced
- **The Strategy design pattern** — Encapsulating each discount rule (`PercentageDiscount`, `FixedAmountDiscount`, `PremiumUserDiscount`) as its own class, making them interchangeable and independently extendable without modifying existing code
- **Type hints** — Annotating function signatures with `str`, `float`, `int`, and `list[DiscountStrategy]` to make the code self-documenting and easier to reason about
- **`if __name__ == '__main__'`** — Structuring the entry point so the module can be safely imported without running the demo automatically
- **Finding the best value with `min()`** — Collecting all applicable discounted prices into a list and using `min()` to select the best one, rather than manually comparing values
- **Docstrings on every class** — Writing clear `"""docstrings"""` on each class and method to document their purpose and contract

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |
| `abc` | Defining the abstract base class and enforcing the interface |

## 💡 How It Works

Each discount type is its own class implementing two methods from `DiscountStrategy`:

- `is_applicable(product, user_tier)` — Returns `True` if the discount can be applied
- `apply_discount(product)` — Returns the discounted price

`DiscountEngine` takes a list of strategies, filters for applicable ones, collects all discounted prices, and returns the lowest.

| Strategy | Rule |
|----------|------|
| `PercentageDiscount` | Applies a % discount, capped at 70% max |
| `FixedAmountDiscount` | Deducts a fixed amount, only if it stays within 10% of the price |
| `PremiumUserDiscount` | Applies 20% off exclusively for `premium` tier users |

**Example Output:**

```
Best price for Wireless Mouse for Premium user: $40.00
```

## 🚀 Future Improvements

- [ ]  Add a `BundleDiscount` strategy that applies when multiple items are purchased together
- [ ]  Allow strategies to be added or removed from the engine at runtime
- [ ]  Return a full breakdown of which strategies were applicable and what each price would have been
- [ ]  Write unit tests with `pytest` to validate each strategy independently

## 📂 Project Structure
```
advanced-discount-calculator/
│
├── DiscountCalculatorV2.py    # Product, strategy classes, DiscountEngine, and demo
└── README.md
```

*Part of my Python learning journey 🐍 — a deliberate revisit of an earlier project using abstraction, the Strategy pattern, and type hints*
