from typing import List
from abstract_observer import Subject, Observer


class ConcreteSubject(Subject):
    def __init__(self, subject_name: str) -> None:
        print(f"{subject_name} created.")
        self.name = subject_name

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"{self.name}: Attached observer {observer.name}.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print(f"{self.name}: Detached observer {observer.name}.")
        self._observers.remove(observer)

    def notify(self) -> None:
        print(f"{self.name}: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print(f"New event from {self.name}.")
        self.notify()


class ConcreteObserver(Observer):
    def __init__(self, name: str) -> None:
        print(f"Observer {name} created.")
        self.name = name

    def update(self, subject: Subject) -> None:
        print(f"{self.name}: Reacted to the event from {subject.name}.")
