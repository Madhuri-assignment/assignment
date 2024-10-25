from django.dispatch import Signal, receiver

# Define a simple signal
my_signal = Signal()

# Signal handler
@receiver(my_signal)
def my_handler(sender, **kwargs):
    print("Signal received!")

# Emit the signal
print("Before sending signal")
my_signal.send(sender=None)
print("After sending signal")