from django.http import HttpResponse, Http404
from .models import Voucher
from django.shortcuts import render
from django.template import loader
from django.db.models import Q

def index(request):
	voucher = Voucher.objects.filter()
	query = request.GET.get("q")
	is_main = 1
	
	if query:
		voucher = voucher.filter(
			Q(voucher_code__contains=query)
		).distinct()

		is_main = 0

		return render(request, 'main/index.html', {'voucher':voucher, 'is_main':is_main})
	else:
		return render(request, 'main/index.html', {'voucher':voucher, 'is_main':is_main})

	return render(request, 'main/index.html', {'voucher':voucher, 'is_main':is_main})