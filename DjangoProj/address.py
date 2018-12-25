from django.shortcuts import render_to_response

address=[
    {'name':'Jay','address':'nus'},
    {'name':'Ray','address':'astar'}
]

def index(request):
    return render_to_response('address.html',{'address':address})