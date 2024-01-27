def log(descriptor):
    # Implement the decorator here
    def decorator(func):
        
        def wrapper(*args, **kwargs):
            descriptor.write(
                f'LOG: {func.__name__}({",".join([str(i) for i in args])})\n'
            )
            return func(*args, **kwargs)
        
        return wrapper
    return decorator
