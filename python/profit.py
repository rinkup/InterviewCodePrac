# Write a function max_profit(prices) that efficiently finds the two cities that maximize your profit (i.e. largest difference in prices).

# Input: A dictionary with cities as keys and prices as values Output: An array (or tuple) containing the names of the cities (min, max)

# Example
# prices = {'London': 72, 'New York': 70, 'Tokyo': 67, 'Miami': 62}

# max_profit(prices) # => ('Miami', 'London')



def max_profit(prices):
    return (min(prices, key=prices.get), max(prices, key=prices.get))
  


prices = {'London': 62, 'New York': 62, 'Tokyo': 62, 'Miami': 62}
print(max_profit(prices))