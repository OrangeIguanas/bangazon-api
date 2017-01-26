from django.db import models


class Orders(models.Model): 
	payment_types_id = models.ForiegnKey("payment_types_id")

	def __int__(self): 
		return self.payment_types_id
