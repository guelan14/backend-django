from django.shortcuts import render, HttpResponse

html_base="""
<h1>My web</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de </a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
</ul>
"""

# Create your views here.
def home(request): 
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")
    
def portfolio(request): 
    return render(request, "core/portfolio.html")

def contact(request): 
    return render(request, "core/contact.html")