from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import State, City
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.html import escape
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from main.forms import CitySearchForm, CreateCityForm, CityEditForm
from django.contrib.auth.decorators import login_required

# Creastatte your views here.
@login_required
def city_delete(request, pk):
	City.objects.get(pk=pk).delete()

	return redirect('/city_edit/')


@login_required
def city_edit(request, pk):
	request_context = RequestContext(request)
	context = {}
	city = City.objects.get(pk=pk)
	context['city'] = city

	form = CityEditForm(request.POST or None, instance=city)

	context['form'] = form
	if form.is_valid():
		form.save()
		return redirect('/city_search/')
	return render_to_response('city_edit.html', context, context_instance=request_context)

@login_required
def city_create(request):
	request_context = RequestContext(request)
	context = {}

	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()

			return render_to_response('city_create.html', context, context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response('city_create.html', context, context_instance=request_context)
	else:
		form = CreateCityForm()
		context['form'] = form
		return render_to_response('city_create.html', context, context_instance=request_context)		


def state_list(request):
	context = {}
	states = State.objects.all()
	context['states'] = states

	return render(request, 'state_list.html', context)

def state_detail(request, pk):
	context = {}
	state = State.objects.get(pk=pk)
	context['state'] = state
	return render(request, 'state_detail.html', context)

class StateListView(ListView):
	model = State
	template_name = "state_list.html"
	context_object_name = 'states'

class StateDetailView(DetailView):
	model = State
	template_name = "state_detail.html"
	context_object_name = 'state'
@login_required
def city_search(request):
	request_context = RequestContext(request)
	context = {}
	if request.method == 'POST':
		form = CitySearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state = form.cleaned_data['state']

			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)
			return render_to_response('city_search.html', context, context_instance=request_context)
		else :
			context['valid'] = form.errors
			return render_to_response('city_search.html', context, context_instance=request_context)
	else:
		form = CitySearchForm()
		context['form'] = form
		return render_to_response('city_search.html', context, context_instance=request_context)		

