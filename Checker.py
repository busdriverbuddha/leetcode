from typing import Any, Callable


class Checker:
    def __init__(self, testing_function: Callable, test_in_kwargs: list[dict[str, Any]], test_out: list[Any]):
        self.testing_function = testing_function
        self.test_in_kwargs = test_in_kwargs
        self.test_out = test_out

    def check(self):
        for i, (tik, to) in enumerate(zip(self.test_in_kwargs, self.test_out), 1):
            ans = self.testing_function(**tik)
            if ans == to:
                print(f"Case {i}: passed.")
            else:
                print(f"Case {i}: expected {to}; got {ans}.")
