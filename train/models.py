from django.db import models
# Create your models here.
TIME_SLOT=(
    ('6:00 AM', '6:00 AM'),
    ('12:00 PM', '12:00 PM'),
    ('3:00 PM', '3:00 PM'),
    ('8:00 PM', '8:00 PM'),
)

DESTINATION=(
    ('Sylhet','Sylhet'),
    ('Sunamganj','Sunamganj'),
    ('Dhaka','Dhaka'),
    ('Chittagong','Chittagong'),
)

SEAT_TYPE=(
    ('AC', 'AC'),
    ('NON-AC', 'NON-AC'),
)

SEAT_NO=(
    ('A1','A1'),
    ('A2','A2'),
    ('A3','A3'),
    ('A4','A4'),
    ('A5','A5'),
)

class Station(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Train_list(models.Model):
    name = models.CharField(max_length=100)
    time= models.CharField(max_length=15, choices=TIME_SLOT, blank=True, null=True)
    seat= models.CharField(max_length=15, choices=SEAT_TYPE, blank=True, null=True)
    station= models.ManyToManyField(Station)
    seat_number = models.CharField(choices=SEAT_NO, max_length=5, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places = 2, blank=True, null=True)
    destination = models.CharField(max_length=200, choices= DESTINATION, blank=True, null=True)

    def __str__(self):
        return self.name