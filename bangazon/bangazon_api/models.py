from django.db import models

# This creates the model for Orders, which must be migrated subsequent to building the 
# payment_types model to satisfy its foreign key requirement. 

class Orders(models.Model): 
	payment_types_id = models.ForiegnKey("payment_types_id")

	def __int__(self): 
		return self.payment_types_id
