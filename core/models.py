from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



# IVA_CHOICES = (
# 	(0, '0%'),
# 	(10, '10%'),
# 	(16, '16%')
# )
class Item(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	proyecto = models.CharField(max_length=30)
	nombre = models.CharField(max_length=30)
	proveedor = models.CharField(max_length=30)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	unidad = models.IntegerField()
	# iva = models.IntegerField(required=True,choices=IVA_CHOICES)
	descripcion = models.CharField(max_length=255)
	slug = models.SlugField()
	image = models.ImageField(default="empty")


	def get_absolute_url(self):
		return reverse("core:item-detail", kwargs={
				'id': self.id
			})
	def __str__(self):
		return self.nombre

	def total(self):
		return self.precio * self.unidad


	def get_remove_from_cart_url(self):
		return reverse("core:remove-from-cart", kwargs={
			'id': self.id
		})
class Boleto(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=20)
	nombre_p = models.CharField(max_length=20)
	nombre_m = models.CharField(max_length=20)
	fecha_nacimiento = models.DateTimeField()
	travel_options = [
		('Internacional', 'Internacional'),
		('Nacional', 'Nacional')
	]
	viaje = models.CharField(max_length=20, choices=travel_options, default='Nacional')
	passport = models.CharField(max_length=16)
	linea_aerea = models.CharField(max_length=30)
	destino= models.CharField(max_length=30)
	fecha_salida = models.DateTimeField()
	fecha_regreso = models.DateTimeField()
	
	def get_absolute_url(self):
		return reverse("core:boleto-detail", kwargs={
				'id': self.id
			})
	

# class Order(models.Model):
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL,
# 									on_delete=models.CASCADE)
# 	ref_code = models.CharField(max_length=20, blank=True, null=True)
# 	items = models.ManyToManyField(Item)
# 	start_date = models.DateTimeField(auto_now_add=True)
# 	fecha = models.DateTimeField()
# 	ordenada= models.BooleanField(default=False)
# 	en_proceso = models.BooleanField(default=False)
# 	completada = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.user.username

# 	def get_total(self):
# 		total = 0
# 		for item in self.items.all():
# 			total += item.total()
# 		return total
