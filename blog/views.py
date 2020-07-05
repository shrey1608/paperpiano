from django.shortcuts import render,redirect

# Create your views here.

def home(request):
	if request.method=="POST":
		return redirect('next-p')
	return render(request,'blog/home.html')
	
def about(request):
	return render(request,'blog/about.html')

def printe(request):
	return render(request,'blog/print.html')

def playe(request):
	return render(request,'blog/play.html')
