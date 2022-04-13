import random
import time


# Task 1
def measure_time(func):
    def inner_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return inner_func


# Task 2
def function_logging(func):
    def logger(*args, **kwargs):
        if not kwargs and not args:
            arg_str = 'no arguments'
        elif not kwargs:
            arg_str = f'positional arguments: {args}'
        elif not args:
            kw_str = [f"{i}={j}" for i, j in kwargs.items()]
            arg_str = f'keyword arguments: {", ".join(kw_str)}'
        else:
            kw_str = [f"{i}={j}" for i, j in kwargs.items()]
            arg_str = f'positional arguments: {args} and keyword arguments: {", ".join(kw_str)}'
        print(f'Function {func.__name__} is called with {arg_str}')
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} returns output of type {type(result).__name__}')
        return result
    return logger


# Task 3
def roulette_maker(probability=0.5, return_value="decorator's output"):
    def russian_roulette_decorator(func):
        def inner_func(*args, **kwargs):
            if random.random() <= probability:
                return return_value
            else:
                return func(*args, **kwargs)
        return inner_func
    return russian_roulette_decorator


# Task 4
def my_staticmethod(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


# Task 5
def my_dataclass(clss):
    class InnerClass:
        def __init__(self, *args, **kwargs):
            for annt in list(clss.__annotations__.keys()):
                setattr(self, annt, clss.__annotations__[annt])
            for attr, value in zip(list(clss.__annotations__.keys()), args):
                setattr(self, attr, value)
            for attr in list(clss.__annotations__.keys()):
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])

        def __repr__(self):
            arg_str = [f"{key}={value}" for key, value in self.__dict__.items()]
            return f'{clss.__name__}({", ".join(arg_str)})'
    return InnerClass


if __name__ == '__main__':
    # Examples:
    # Task 1
    @measure_time
    def time_consuming_func(a, b, f=2, g='func output'):
        time.sleep(a)
        time.sleep(b)
        time.sleep(f)
        return g

    print('Task 1. Example (exec time)')
    print(time_consuming_func(5, 0.5, f=1))  # 6.5XX

    # Task 2
    @function_logging
    def not_verbose_func(a, b, c, d=4, e='blabla'):
        return [a+b+c, d, e]

    print('Task 2. Example (function log)')
    print(not_verbose_func(1, 4, 6, d=2, e='wordword'))

    # Task 3
    @roulette_maker(probability=0.2, return_value='Ooups, your output was stolen!')
    def dice():
        return random.randint(1, 7)

    print('Task 3. Example (roulette decorator)')
    for _ in range(10):
        print(dice())

    # Task 4
    class MyClass:
        def __init__(self):
            self.arg1 = 'some value'

        @my_staticmethod
        def plus_one(a=3):
            return a + 1

    print('Task 4. Example (staticmethod parody)')
    print(MyClass.plus_one())
    print(MyClass.plus_one(5))

    # Task 5
    @my_dataclass
    class Student:
        name: str
        age: 3
        spec: str

    print('Task 5. Example (dataclass parody)')
    a = Student('Ann', spec='Bio')
    print(a)
    print(a.age)
