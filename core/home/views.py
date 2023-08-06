from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name':'Redoy Saha', 'age':23},
        {'name':'Nayon Saha', 'age':17},
        {'name':'Rajib Saha', 'age':14},
        {'name':'Antor Saha', 'age':18},
        {'name':'Istiak Ahmed', 'age':26}
    ]
    # for people in peoples:
    #     print(people)
    text = """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Amet possimus ducimus sit earum sequi molestias exercitationem vel quae necessitatibus laudantium similique totam saepe, quas eaque modi nisi magni quod temporibus?
        """

    return render(request,"home/index.html", context = {'page': 'Home', 'peoples': peoples, 'text': text})

def new_page(request):
    return HttpResponse("<h1>I am a new page in django</h1>")

def about(request):
        context = {'page' : 'About'}
        return render(request,"home/about.html", context)

def contact(request):
        context = {'page' : 'Contact'}
        return render(request,"home/contact.html", context)

    