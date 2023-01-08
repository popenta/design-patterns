from typing import List, Protocol


class Subject(Protocol):
    name: str
    observers: List["Observer"] = []

    def attach(self, observer: "Observer") -> None:
        ...

    def detach(self, observer: "Observer") -> None:
        ...

    def notify(self) -> None:
        ...


class Observer(Protocol):
    name: str

    def update(self, subject: Subject) -> None:
        ...
