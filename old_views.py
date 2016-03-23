# def detail_view(request, name):

# 	context = {}
# 	state = State.objects.get(name=name)
# 	context['state'] = state


# 	return render(request, 'detail_view.html', context)




# @csrf_exempt

# def get_post(request):

# 	get_state= request.GET.get('state', None)
# 	get_city= request.GET.get('city', None)

# 	print get_state
# 	print get_city

# 	city_state_string = ""
# 	states = State.objects.filter(name__startswith="%s" % get_state)
# 	for state in states:
# 		cities = state.city_set.filter(name__startswith="%s" % get_city)
# 		for city in cities:
# 			city_state_string+= "<b>%s</b> %s <br>" % (state, city.name)
# 	city_state_string+= """
# 		<form action="/get_post" method="GET">

# 		State:
# 		<br>
# 		<input type="text" name="state" >

# 		<br>

# 		City:
# 		<br>
# 		<input type="text" name="city" >

# 		<br>
# 		<br>

# 		<input type="submit" value="Submit">

# 		</form>
# 	"""
# 	response = city_state_string
# 	return HttpResponse(response)




# def first_view(request, starts_with):
	
# 	states = State.objects.all()
# 	text_string = ''
# 	for state in states:
# 		cities = state.city_set.filter(name__startswith="%s" % starts_with)
# 		for city in cities:
# 			text_string += "State: %s, City: %s <br>" % (state.name, city.name)
# 	return HttpResponse(text_string)


# class GetPost(View):

# 	def get(self, request, *args, **kwargs):
# 		city_state_string = """
# 			<form action="/get_post/" method="POST">
# 			State:
# 			<br>
# 			<input type="text" name="state" >
# 			<br>
# 			City:
# 			<br>
# 			<input type="text" name="city" >
# 			<br>
# 			<br>
# 			<input type="submit" value="Submit">	
# 			</form>
# 		"""

# 		response = city_state_string

# 		return HttpResponse(response)

# 	def post(self, request, *args, **kwargs):
# 		get_state= request.POST.get('state', None)
# 		get_city= request.POST.get('city', None)

# 		city_state_string = ""

# 		states = State.objects.filter(name__startswith="%s" % get_state)

# 		for state in states:
# 			cities = state.city_set.filter(name__startswith="%s" % get_city)
# 			for city in cities:
# 				city_state_string+= "<b>%s</b> %s <br>" % (state, city.name)

# 		city_state_string+= """
# 			<form action="/get_post/" method="POST">
# 			State:
# 			<br>
# 			<input type="text" name="state" >
# 			<br>
# 			City:
# 			<br>
# 			<input type="text" name="city" >
# 			<br>
# 			<br>
# 			<input type="submit" value="Submit">
# 			</form>
# 		"""

# 		response = city_state_string

# 		return HttpResponse(response)


# def state_detail(request, name):
# 	state = State.objects.get(name=name)
# 	cities = state.city_set.all()
# 	print cities

	
# 	text_string = '<h3> %s </h3>' % state.name
	
# 	for city in cities:
# 		print city
# 		try:
# 			text_string += '%s </br>' % city.name
# 		except Exception, e:
# 			print e	
# 	return HttpResponse(text_string)

# def state_list(request):
# 	states = State.objects.all()
# 	state_list = []
# 	for state in states:
# 		try:
# 			state_list.append("<a href='/state_detail/%s'>%s -- %s </a> <br>" % (state.name, state.name, state.statecapital.name))	
# 		except Exception, e:
# 			print e
# 	return HttpResponse(state_list)	