import inspect
import types

class OverloadedFunction:
    def __init__(self, name):
        self.name = name
        self.registry = {}

    def register(self, func):
        sig = inspect.signature(func)
        typesig = []

        for name, param in sig.parameters.items():
            if name == "self":
                continue
            if param.annotation is inspect.Parameter.empty:
                raise TypeError("All parameters must be type annotated")
            if not isinstance(param.annotation, type):
                raise TypeError("Annotations must be types")
            typesig.append(param.annotation)

        self.registry[tuple(typesig)] = func

    def __call__(self, *args):
        typesig = tuple(type(arg) for arg in args[1:])
        func = self.registry.get(typesig)

        if not func:
            raise TypeError(f"No matching overload for {typesig}")

        return func(*args)

    def __get__(self, instance, owner):
        return types.MethodType(self, instance) if instance else self


class OverloadDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            existing = self[key]
            if isinstance(existing, OverloadedFunction):
                existing.register(value)
            else:
                overloaded = OverloadedFunction(key)
                overloaded.register(existing)
                overloaded.register(value)
                super().__setitem__(key, overloaded)
        else:
            super().__setitem__(key, value)


class OverloadMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OverloadDict()

    def __new__(cls, name, bases, namespace):
        return super().__new__(cls, name, bases, dict(namespace))


class Calculator(metaclass=OverloadMeta):

    def add(self, x: int, y: int):
        return f"adding int :{x+y}"

    def add(self, x: str, y: str):
        return f"adding string :{x+y}"

    def add(self,a:int, b:int , c:int ):
        return f"adding 3 arguments: {a+b+c}"


calc= Calculator()
print(calc.add("Hello", "world"))
print(calc.add(5, 10))
print(calc.add(10,11,12))
