def fibonacci_series(n):
    series = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    for i in range(2, n):
        next_num = series[i-1] + series[i-2]
        series.append(next_num)
    return series

print(fibonacci_series(10)) 
