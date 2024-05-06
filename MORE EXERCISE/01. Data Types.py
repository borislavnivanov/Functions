# from multimethod import multimethod
# from multipledispatch import dispatch
from functools import singledispatch

input1 = input()
input2 = input()


# @multimethod
# @dispatch(int)
@singledispatch
def worker(n: int) -> int:
    return n * 2


# @multimethod
# @dispatch(float)
@worker.register(float)
def _(n: float) -> float:
    return f'{n * 1.5:.2f}'


# @multimethod
# @dispatch(str)
@worker.register(str)
def _(n: str) -> str:
    return f'${n}$'


if input1 == 'int':
    result = worker(int(input2))
elif input1 == 'real':
    result = worker(float(input2))
else:
    result = worker(input2)

print(result)
