def sequential_map(*args):
    lst = args[-1]
    process_chain = func_chain(*args[:len(args)-1])
    return [process_chain(i) for i in lst]


def consensus_filter(*args):
    lst = args[-1]
    for func in args[:len(args) - 1]:
        lst = filter(func, lst)
    return list(lst)


def conditional_reduce(fun1, fun2, lst):
    f_lst = list(filter(fun1, lst))
    for i in range(1, len(f_lst)):
        f_lst[i] = fun2(f_lst[i-1], f_lst[i])
    return f_lst[-1]


def func_chain(*args):
    def constructed_function(x):  # :)
        for fun in args:
            x = fun(x)
        return x
    return lambda x: constructed_function(x)


def multiple_partial(*args, **kwargs):
    fun_list = []

    def kwargumenter(fun, **kwargs):
        return lambda *n_args, **n_kwargs: fun(*n_args, **kwargs, **n_kwargs)
    for fun in args:
        fun_list.append(kwargumenter(fun, **kwargs))
    return fun_list
