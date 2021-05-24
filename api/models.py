from django.db import models

# Create your models here.
class Restaurante(models.Model):
    id = models.TextField(max_length=256, primary_key=True)
    rating = models.IntegerField()
    name = models.TextField()
    site = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()

    def serialize(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "name": self.name,
            "site": self.site,
            "email": self.email,
            "phone": self.phone,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "lat": self.lat,
            "lng": self.lng
        }