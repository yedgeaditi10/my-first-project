# Iterative approach to generate Fibonacci series
def fibonacci_series(n):
    series = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Generate subsequent numbers
    for i in range(2, n):
        next_num = series[i-1] + series[i-2]
        series.append(next_num)
    return series

# Example: Print the first 10 terms
print(fibonacci_series(10)) 
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
