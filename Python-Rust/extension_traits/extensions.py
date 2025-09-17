from abc import ABC, abstractmethod

# Base trait: like Rust's `Write`
class Write(ABC):
    @abstractmethod
    def write(self, data: str) -> None:
        pass


# Extension trait: like Rust's `WriteHtml`
class WriteHtml(Write):
    def write_html(self, s: str) -> None:
        # Default impl uses `write` from Write
        self.write(f"<html>{s}</html>")

class FileWriter(WriteHtml):
    def __init__(self):
        self.buffer = []

    def write(self, data: str) -> None:
        self.buffer.append(data)

f = FileWriter()
f.write_html("Hello ABC")
print(f.buffer)  # ['<html>Hello</html>']

# ----------------------------------------------------
# In Rust, you don’t need to opt in by subclassing — all Write types automatically get WriteHtml.
# Python can mimic this using mixin registration:
class WriteHtmlExt:
    def write_html(self, s: str) -> None:
        self.write(f"<html>{s}</html>")

# extend_with_html is like Rust’s impl<W: Write> WriteHtml for W.
def extend_with_html(cls):
    cls.write_html = WriteHtmlExt.write_html
    return cls

@extend_with_html
class FileWriter:
    def __init__(self):
        self.buffer = []
    def write(self, data: str) -> None:
        self.buffer.append(data)

f = FileWriter()
f.write_html("Hello Registration")   # works!
print(f.buffer)
