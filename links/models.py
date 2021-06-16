from django.db import models
from .utils import get_link_data
from twilio.rest import Client
from django.core.validators import URLValidator
# Create your models here.
class Link(models.Model):
    name=models.CharField(max_length=220,blank=True)
    url=models.TextField(validators=[URLValidator()])
    curr_price=models.FloatField(blank=True)
    old_price=models.FloatField(default=0)
    price_difference=models.FloatField(default=0)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class meta:
        ordering=('price_difference','-created')

    def save(self,*args,**kwargs):
        
        name,price= get_link_data(self.url)
        if self.curr_price:
            if price<self.curr_price:
                account_sid ='AC6c685dedb56b58d64159d5305a54ab05'
                auth_token = '5c7dbfaef7316f16cb7f13f9d98304ba'
                client = Client(account_sid, auth_token)

                message = client.messages \
                .create(
                     body=f"HI Rajnish Your Product {self.name} price dropped to Rs{price},Don't wait purchase Now",
                     from_='+15027836049',
                     to='+919670277969'
                 )

                print(message.sid)

            if self.curr_price!=price:
                diff=price-self.curr_price
                self.price_difference=diff
                self.old_price=self.curr_price
                self.curr_price=price

            
        else:
            self.curr_price=price
            self.old_price=0
            self.price_difference=0
        self.name=name
        super().save(*args,**kwargs)


