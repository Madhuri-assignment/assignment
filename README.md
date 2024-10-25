Question 1: 

By default, Django signals are executed synchronously. This means that the signal handlers are called immediately when the signal is sent.

Code Snippet:

Output:

Before sending signal
Signal received!
After sending signal

In the output, we can see that the handler is executed before "After sending signal", confirming synchronous execution.

question 2:



Question 2: 

Yes, Django signals run in the same thread as the caller. The signal handlers are executed in the same thread that emitted the signal.

Code Snippet:

import threading
from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_handler(sender, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

print(f"Before sending signal in thread: {threading.current_thread().name}")
my_signal.send(sender=None)
print(f"After sending signal in thread: {threading.current_thread().name}")

Output:

Before sending signal in thread: MainThread
Signal received in thread: MainThread
After sending signal in thread: MainThread

Both messages indicate the same thread, showing that the signal handler runs in the same thread as the caller.

Question 3: 

Yes, by default, Django signals run in the same database transaction as the caller. If the signal is emitted within a transaction, the handlers will also be part of that transaction.

Code Snippet:

from django.db import transaction
from django.dispatch import Signal, receiver
from django.db import models

# Define a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal
my_signal = Signal()

@receiver(my_signal)
def my_handler(sender, **kwargs):
    MyModel.objects.create(name="Signal Triggered")

# Using a transaction
with transaction.atomic():
    print("Before sending signal")
    my_signal.send(sender=None)
    print("After sending signal")

# Check if the model was created
print("Number of MyModel entries:", MyModel.objects.count())

Output:

Before sending signal
After sending signal
Number of MyModel entries: 1

This shows that the model entry is created, confirming that the signal handler executed within the same transaction.


---

Custom Classes in Python
implementation if class rectangle 

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(5, 10)

for dimension in rect:
    print(dimension)

Output:

{'length': 5}
{'width': 10}

This implementation allows for iteration over a Rectangle instance, yielding the length and width in the specified format.
