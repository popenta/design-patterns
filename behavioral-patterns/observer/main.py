from concrete_observer import ConcreteSubject, ConcreteObserver


def main() -> None:
    subject = ConcreteSubject("Observable")

    observer_a = ConcreteObserver("Observer_A")
    observer_b = ConcreteObserver("Observer_B")

    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.some_business_logic()

    subject.detach(observer_a)
    subject.detach(observer_b)


if __name__ == "__main__":
    main()
