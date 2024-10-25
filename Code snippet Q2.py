import threading
from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_handler(sender, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

print(f"Before sending signal in thread: {threading.current_thread().name}")
my_signal.send(sender=None)
print(f"After sending signal in thread: {threading.current_thread().name}")