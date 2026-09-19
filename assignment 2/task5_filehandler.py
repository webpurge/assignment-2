from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):
    def read(self):
        print("Reading text file as plain text.")

    def write(self, data):
        print(f"Writing text data: {data}")


class BinaryFileHandler(FileHandler):
    def read(self):
        print("Reading binary file as bytes.")

    def write(self, data):
        print(f"Writing binary data: {data}")


if __name__ == "__main__":
    text_handler = TextFileHandler()
    text_handler.read()
    text_handler.write("Hello, world!")

    binary_handler = BinaryFileHandler()
    binary_handler.read()
    binary_handler.write(b"\x00\x01\x02")

    # FileHandler() would raise a TypeError since it has abstract methods
