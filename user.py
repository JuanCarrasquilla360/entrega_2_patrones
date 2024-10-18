from abc import ABC, abstractmethod


class User:
    def __init__(self, firstname, lastname, username, password):
        self._firstname = firstname
        self._lastname = lastname
        self._username = username
        self._password = password

    def get_firstname(self):
        return self._firstname

    def get_username(self):
        return self._username

    def set_password(self, password):
        self._password = password


class OrganizationalComponent(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def get_child(self, index):
        pass


class Employee(OrganizationalComponent):
    def __init__(self, user: User):
        self.user = user

    def get_name(self):
        return self.user.get_firstname()

    def add(self, component):
        raise NotImplementedError("Operación no soportada")

    def remove(self, component):
        raise NotImplementedError("Operación no soportada")

    def get_child(self, index):
        raise NotImplementedError("Operación no soportada")

    def set_password(self, password):
        self.user.set_password(password)


class Department(OrganizationalComponent):
    def __init__(self, name):
        self.name = name
        self.components = []

    def get_name(self):
        return self.name

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def get_child(self, index):
        return self.components[index]


class UserAdapter(User):
    def __init__(self, employee: Employee):
        self.employee = employee
        super().__init__(firstname=employee.get_name(), lastname="", username="", password="")

    def get_firstname(self):
        return self.employee.get_name()

    def set_password(self, password):
        self.employee.set_password(password)
