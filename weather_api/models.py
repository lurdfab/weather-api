from django.db import models


DESCRIPTIONS = (
    (0, "Sunny"),
    (1, "Rain"),
    (2, "Cloudy"),
    (3, "Snow")
)

#model to describe the weather
class Description(models.Model):
    weather_description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.created_at) #we converted this to string since the best thing to return is a string and we don't have it here

