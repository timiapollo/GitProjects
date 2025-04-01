def fibonacci_sell_strategy(launch_price, buy_price, tokens, current_price):
    import numpy as np

    # Fibonacci Extension Levels
    fib_levels = [0.618, 0.786, 1.0, 1.272, 1.618]

    # Calculate price targets
    fib_prices = [launch_price * level for level in fib_levels]

    # Sell 20% of holdings at each level
    sell_percentage = 0.2  
    tokens_to_sell = tokens * sell_percentage  

    print(f"Initial Investment: ${buy_price * tokens:.2f}")
    print(f"Current Price: ${current_price:.4f}\n")
    
    print("Sell Strategy Based on Fibonacci Levels:")
    for i, price in enumerate(fib_prices):
        revenue = tokens_to_sell * price
        print(f"📍 Fib {fib_levels[i]:.3f} -> Sell {tokens_to_sell:.0f} tokens at ${price:.4f} each -> Revenue: ${revenue:.2f}")

    print("\n🔹 Hold the remaining 20% for further price action or moonshot moves.")

# Example Usage:
launch_price = 0.038   # Price at launch
buy_price = 0.01      # Price at your entry
tokens = 150000        # Total tokens bought
current_price = 0.038   # Current market price (example)

fibonacci_sell_strategy(launch_price, buy_price, tokens, current_price)
