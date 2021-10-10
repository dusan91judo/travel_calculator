class BaseTravelCalculatorException(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class InvalidParams(BaseTravelCalculatorException):
    @classmethod
    def for_invalid_params(cls, message) -> 'InvalidParams':
        return cls(
            message=message
        )
