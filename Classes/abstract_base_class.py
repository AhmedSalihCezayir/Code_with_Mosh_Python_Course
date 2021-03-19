from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# To make this class abstract, we should derive it from ABC class.
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # To define a common interface for all streams, we need to use a decorator.
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


# If we dont implement abstract methods, this class will also be abstract class.
# So, we should implement the read() method.
class MemoryStream(Stream):
    pass
