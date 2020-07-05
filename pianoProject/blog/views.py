from django.shortcuts import render,redirect

# Create your views here.

def home(request):
	if request.method=="POST":
		return redirect('next-p')
	return render(request,'blog/home.html')

def nextp(request):
	return render(request,'blog/nextpage.html')

def about(request):
	return render(request,'blog/about.html')
