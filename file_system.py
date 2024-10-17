from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

class Folder(FileSystemComponent):
    def __init__(self, name):
        self._name = name
        self._children = []

    def get_name(self):
        return self._name

    def get_size(self):
        return sum(child.get_size() for child in self._children)

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

# Ejemplo de uso
if __name__ == "__main__":
    root = Folder("Root")
    
    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    
    subfolder = Folder("Subfolder")
    file3 = File("file3.txt", 300)
    
    root.add(file1)
    root.add(file2)
    root.add(subfolder)
    subfolder.add(file3)

    print(f"Tamaño total de {root.get_name()}: {root.get_size()} bytes")
    print(f"Tamaño de {subfolder.get_name()}: {subfolder.get_size()} bytes")