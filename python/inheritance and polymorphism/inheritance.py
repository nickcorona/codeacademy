class Bin:
    pass


class RecyclingBin(Bin):
    pass


issubclass(ZeroDivisionError, Exception)


class KitchenException(Exception):
    """
    Exception that gets thrown when a kitchen appliance isn't working
    """


class MicrowaveException(KitchenException):
    """
    Exception for when the microwave stops working
    """


class RefrigeratorException(KitchenException):
    """
    Exception for when the refrigerator stops working
    """
