from typing import Any, Callable, Type, TypeVar

T = TypeVar("T")


def singleton(class_: Type[T]) -> Callable[..., T]:
    instances = {}

    def getinstance(*args: Any, **kwargs: Any) -> T:
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
