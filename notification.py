from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class BasicNotification(Notification):
    def send(self):
        return "Enviando notificación básica"

class NotificationDecorator(Notification):
    def __init__(self, notification):
        self._notification = notification

    @abstractmethod
    def send(self):
        pass

class SoundDecorator(NotificationDecorator):
    def send(self):
        return f"{self._notification.send()} con sonido"

class VibrationDecorator(NotificationDecorator):
    def send(self):
        return f"{self._notification.send()} con vibración"

# Ejemplo de uso
if __name__ == "__main__":
    basic_notification = BasicNotification()
    print(basic_notification.send())

    sound_notification = SoundDecorator(basic_notification)
    print(sound_notification.send())

    vibration_notification = VibrationDecorator(basic_notification)
    print(vibration_notification.send())

    sound_and_vibration = VibrationDecorator(SoundDecorator(basic_notification))
    print(sound_and_vibration.send())