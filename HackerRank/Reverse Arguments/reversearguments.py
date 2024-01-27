
def reversed_args(f):
    
    def g(*args, **kwargs):
        return f(*args[::-1],**kwargs)
    
    return g
