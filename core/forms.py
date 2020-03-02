from django import forms
from .models import Item, Boleto
from django.forms import DateTimeField
from .widgets import XDSoftDateTimePickerInput


class ItemModelForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ('image','slug','user')

class BoletoModelForm(forms.ModelForm):
	class Meta:
		model = Boleto
		widgets = {
			'fecha_regreso': XDSoftDateTimePickerInput(),
			'fecha_salida': XDSoftDateTimePickerInput(),
			'fecha_nacimiento': XDSoftDateTimePickerInput()
		}
		exclude = ('user',)



	
	
	# def clean_title(self, *args,**kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if not "CFE" in title:
	# 		raise forms.ValidationError("this is not a valid title")
	# 	else:
	# 		return title
	# def clean_email(self, *args,**kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	if not email.endswith("edu") in title:
	# 		raise forms.ValidationError("this is not a valid title")
	# 	else:
	# 		return title



# class CouponForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Promo code',
#         'aria-label': 'Recipient\'s username',
#         'aria-describedby': 'basic-addon2'
#     }))