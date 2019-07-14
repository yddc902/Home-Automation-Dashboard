from django.shortcuts import render

# Create your views here.
def charts(request):
    return render(request, "chart_test.html")

def temp_charts(request, room):
    room = room.capitalize() #convert first letter of room to uppercase
    return render(request, "charts.html", {'room': room})

def all_temp_charts(request):
    return render(request, "charts_all.html", {'room': "All Temperature Charts"})

def temptest_charts(request, room):
    room = room.capitalize()
    return render(request, "charts_slidedown.html", {'room':room})
