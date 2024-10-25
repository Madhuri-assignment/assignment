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