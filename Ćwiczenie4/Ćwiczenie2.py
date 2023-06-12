def limit_range(min_value, max_value):
    def decorator(func):
        def wrapper(value):
            if value < min_value:
                value = min_value
            elif value > max_value:
                value = max_value
            return func(value)
        return wrapper
    return decorator

@limit_range(0, 10)
def process_value(value):
    print("Processed value:", value)

process_value(5)
process_value(-2)
process_value(15)
