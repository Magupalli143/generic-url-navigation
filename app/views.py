from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,'sample.html')

def sample2(request):
    return render(request,'sample2.html')