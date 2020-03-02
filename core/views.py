from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Item, Boleto
from django.shortcuts import redirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from .forms import ItemModelForm, BoletoModelForm
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView,
	View
	)
# Create your views here.


# @login_required
class ItemListView(LoginRequiredMixin, ListView):
		model = Item
		template_name = "item_list.html"

		def get_queryset(self):
			return Item.objects.filter(user=self.request.user)

class BoletoListView(LoginRequiredMixin, ListView):
		model = Boleto
		template_name = "boleto_list.html"

		def get_queryset(self):
			return Boleto.objects.filter(user=self.request.user)
		def get_context_data(self, **kwargs):
			context = super(BoletoListView, self).get_context_data(**kwargs)
			context['activate'] = 'list'
			return context	



def login_view(request,*args, **kwargs):
	if request.user.is_authenticated:
		return redirect("list/")

	else:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return render(request, "item_list.html", {})
				
			else:

				return render(request, "login.html", {})	
		else:
			return render(request, "login.html", {})

	

@login_required
def logout_view(request):
	logout(request)
	return render(request, "login.html", {})

# def home_view(request):

# 	return render(request, "home-page.html")
# class OrderDeleteView(DeleteView):
# 	template_name = '/order_delete.html'

# 	def get_object(self):	
# 		id_ = self.kwargs.get("id")
# 		return get_object_or_404(Item, id=id_)

# 	def get_success_url(self):
# 		return reverse('item:item-list')

# @login_required
class ItemDetailView(LoginRequiredMixin, DetailView):
	model = Item
	template_name = "item_detail.html"

	def get_object(self):	
		id = self.kwargs.get("id")
		return get_object_or_404(Item, id=id)

class BoletoDetailView(LoginRequiredMixin, DetailView):
	model = Boleto
	template_name = "boleto_detail.html"

	def get_object(self):	
		id = self.kwargs.get("id")
		return get_object_or_404(Boleto, id=id)	


# @login_required
class ItemUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'item_create.html'
	form_class = ItemModelForm
	queryset = Item.objects.all() # list of objects
	

	def get_object(self):	
		id = self.kwargs.get("id")
		return get_object_or_404(Item, id=id)

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

# @login_required
class ItemCreateView(LoginRequiredMixin, CreateView):
	template_name = 'item_create.html'
	form_class = ItemModelForm
	queryset = Item.objects.all() # list of objects

	def form_valid(self,form):
		form.instance.user = self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def get_context_data(self, **kwargs):
		context = super(ItemCreateView, self).get_context_data(**kwargs)
		context['activate'] = "create"
		return context

# class UploadFileView(CreateView):
#     form_class = UploadFileForm
#     success_url = 'listview'
#     template_name = 'textfrompdf/index.html'

#     def get_context_data(self, **kwargs):
#         kwargs['object_list'] = PdfFile.objects.order_by('id')
#         return super(UploadFileView, self).get_context_data(**kwargs)

# @login_required
class BoletoCreateView(LoginRequiredMixin,CreateView):
	template_name = 'boleto_create.html'
	form_class = BoletoModelForm
	queryset = Boleto.objects.all() # list of objects

	def form_valid(self,form):
		form.instance.user = self.request.user
		print(form.cleaned_data)
		return super().form_valid(form)
	def get_context_data(self, **kwargs):
		context = super(BoletoCreateView, self).get_context_data(**kwargs)
		context['activate'] = "boleto"
		return context

class ItemDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'item_delete.html'

	def get_object(self):	
		id_ = self.kwargs.get("id")
		return get_object_or_404(Item, id=id_)

	def get_success_url(self):
		return reverse('core:item-list')


# # @login_required
# def remove_from_cart(request, id):
# 	item = get_object_or_404(Item, id=id)
# 	order_qs = Order.objects.filter(
# 		user=request.user,
# 		completada=False
# 	)
# 	if order_qs.exists():
# 		order = order_qs[0]
# 		# check if the order item is in the order
# 		if order.items.filter(item__id=item.id).exists():
# 			order.items.remove(order_item)
# 			item.delete()
# 			messages.info(request, "This item was removed from your cart.")
# 			return redirect("core:order-summary")
# 		else:
# 			messages.info(request, "This item was not in your cart")
# 			return redirect("core:", id=id)
# 	else:
# 		messages.info(request, "You do not have an active order")

# 	return redirect("core:", id=id)


# def remove_single_item_from_cart(request, id):
# 	item = get_object_or_404(Item, id=id)
# 	order_qs = Order.objects.filter(
# 		user=request.user,
# 		ordenada=False
# 	)
# 	if order_qs.exists():
# 		order = order_qs[0]
# 		# check if the order item is in the order
# 		if order.items.filter(item__id=item.id).exists():
# 			if order_item.quantity > 1:
# 				order_item.quantity -= 1
# 				order_item.save()
# 			else:
# 				order.items.remove(order_item)
# 			messages.info(request, "This item quantity was updated.")
# 			return redirect("core:order-summary")
# 		else:
# 			messages.info(request, "This item was not in your cart")
# 			return redirect("core:product", id=id)
# 	else:
# 		messages.info(request, "You do not have an active order")
# 		return redirect("core:product", id=id)

# class OrderSummaryView(LoginRequiredMixin, View):
# 	def get(self, *args, **kwargs):
# 		try:
# 			order = Order.objects.get(user=self.request.user, completada=False)
# 			context = {
# 				'object': order
# 			}
# 			return render(self.request, 'order_summary.html', context)
# 		except ObjectDoesNotExist:
# 			messages.warning(self.request, "You do not have an active order")
# 			return redirect("/")

# @login_required
# def add_to_cart(request, id):
# 	item = get_object_or_404(Item, id=id)
# 	order_qs = Order.objects.filter(user=request.user, completada=False)
# 	if order_qs.exists():
# 		order = order_qs[0]
# 		# check if the order item is in the order
# 		order.items.add(item)
# 		messages.info(request, "This item was added to your cart.")
# 		return redirect("core:compra")

	# else:
	# 	ordered_date = timezone.now()
	# 	order = Order.objects.create(
	# 		user=request.user, ordered_date=ordered_date)
	# 	order.items.add(item)
	# 	messages.info(request, "This item was added to your cart.")
	# 	return redirect("core:compra")
