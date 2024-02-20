from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

import uuid


def home(request):
    return render(request,"home.html")

def fibonacci(request):
    if request.method == "POST":
        fibonacci_form = Fibonacci_Form(request.POST)
        if fibonacci_form.is_valid():
            n = fibonacci_form.cleaned_data["fibonacci_count"]
            if (n>0):
                y = []
                x = []
                num1 = 0
                num2 = 1
                next_number = num2  
                for i in range(n+1):
                    print(next_number, end=" ")
                    y.append(next_number)
                    x.append(i)
                    num1, num2 = num2, next_number
                    next_number = num1 + num2
                    print(y)
                result = " - ".join(map(str,y))
                matplotlib.use('Agg')
                plt.figure(figsize=(20,10), dpi=300)#,facecolor='#191919')
                plt.bar(x,y)
                #plt.axes().set_facecolor("#BED754")
                #plt.axes().tick_params(axis="x", colors="#BED754")      # x tick labels
                #plt.axes().tick_params(axis="y", colors="#BED754")   # y tick labels

                #plt.grid()
                file_name = "fibonacci_chart_" + str(uuid.uuid1()) + ".png"
                plt.savefig('assets/' + file_name)
                #plt.show()
                print(x)
                print(y)
        context = {"form_submitted":True , "result" : result, "file_name": file_name, "fibonacci_form": fibonacci_form}
    else:
        fibonacci_form = Fibonacci_Form()   
        context = {"form_submitted":False, "fibonacci_form": fibonacci_form}
    return render(request, "fibonacci.html", context) # goes inside views.py

def factorial(request):
    result = 0
    if request.method == "POST":
        factorial_form = Factorial_Form(request.POST)
        if factorial_form.is_valid():
            n = factorial_form.cleaned_data["factorial_number"]
            if (n>0):
                result = 1
                for i in range(1,n+1):
                    result *=i
        context = {"form_submitted":True , "result" : result, "factorial_form": factorial_form,}
    else:
        factorial_form = Factorial_Form()
        context = {"form_submitted":False, "factorial_form": factorial_form,}
    return render(request, "factorial.html", context) # goes inside views.py

def trigonometry(request):
    result = {}
    file_name = 'trigonometry_chart_default.png'
    if request.method == "POST":
        trigonometry_form = Trigonometry_Form(request.POST,initial={"trigonometry_degree": "10"})
        if trigonometry_form.is_valid():
            degree = trigonometry_form.cleaned_data["trigonometry_degree"]

            chart_degree_start = trigonometry_form.cleaned_data["trigonometry_chart_degree_start"]
            chart_degree_finish = trigonometry_form.cleaned_data["trigonometry_chart_degree_finish"]


            result["sin"] = round(math.sin(math.radians(degree)),2)
            result["cos"] = round(math.cos(math.radians(degree)),2)
            if (degree!=0):
                result["tan"] = round(math.tan(math.radians(degree)),2)
                result["cotan"] = round(1 / math.tan(math.radians(degree)),2)
            matplotlib.use('Agg')
            x = np.linspace(np.radians(chart_degree_start), np.radians(chart_degree_finish), 1000)
            x = np.linspace(chart_degree_start,chart_degree_finish,720)
            plt.figure(figsize=(20,10), dpi=300)
            plt.plot(x, np.sin(np.radians(x)),'o',ms=1)
            plt.plot(x, np.cos(np.radians(x)),'o',ms=1)
            plt.plot(x, np.tan(np.radians(x)),'o',ms=1)
            plt.plot(x, 1/np.tan(np.radians(x)),'o',ms=1)
            plt.plot(degree,result["sin"],'*',ms=10)
            plt.plot(degree,result["cos"],'*',ms=10)
            plt.plot(degree,result["tan"],'*',ms=10)
            plt.plot(degree,result["cotan"],'*',ms=10)
            plt.legend(["sin", "cos", "tan", "cotan"], loc="lower right")
            plt.ylim(-4, 4)
            plt.locator_params(nbins=72,axis='x')
            plt.grid()
            file_name = "trigonometry_chart_" + str(uuid.uuid1()) + ".png"
            plt.savefig('assets/' + file_name)
            plt.show()
        context = {"form_submitted":True , "result" : result, "file_name": file_name, "trigonometry_form": trigonometry_form,}
    else:
        trigonometry_form = Trigonometry_Form()
        context = {"form_submitted":False , "result" : result, "file_name": file_name, "trigonometry_form": trigonometry_form,}
    return render(request, "trigonometry.html", context) # goes inside views.py

def exponentiation(request):
    result = 0
    file_name = 'exponentiation_chart_default.png'
    if request.method == "POST":
        exponentiation_form = Exponentiation_Form(request.POST,initial={"exponentiation_base": "10"})
        if exponentiation_form.is_valid():
            base = exponentiation_form.cleaned_data["exponentiation_base"]
            power = exponentiation_form.cleaned_data["exponentiation_power"]

            result = math.pow(base,power)

            matplotlib.use('Agg')
            x = np.linspace(-10,10, 500)
            plt.figure(figsize=(25,20), dpi=150)
            plt.plot(x, x**2)
            plt.plot(x, x**3)
            plt.plot(x, x**0.5)
            plt.legend(["x^2", "x^3","x^0.5"], loc="lower right")
            plt.ylim(-8, 8)
            plt.locator_params(nbins=30,axis='x')
            plt.locator_params(nbins=30,axis='y')

            plt.grid()
            file_name = "exponentiation_chart_" + str(uuid.uuid1()) + ".png"
            plt.savefig('assets/' + file_name)
            plt.show()
        context = {"form_submitted":True , "result" : result, 'file_name': file_name, "exponentiation_form": exponentiation_form,}
    else:
        exponentiation_form = Exponentiation_Form()
        context = {"form_submitted": False, "exponentiation_form": exponentiation_form}
    return render(request, "exponentiation.html", context) # goes inside views.py

def absolute(request):
    if request.method == "POST":
        absolute_form = Absolute_Form(request.POST)
        if absolute_form.is_valid():
            n = absolute_form.cleaned_data["absolute_number"]
            x = []
            y = []
            for i in range(-2 * abs(int(n)),2 * abs(int(n)) + 1,1):
                x.append(i)
                y.append(abs(i))
            result = abs(n)
            matplotlib.use('Agg')
            plt.figure(figsize=(20,10), dpi=300)#,facecolor='#191919')
            plt.plot(x,y)
            plt.plot(n,abs(n),'*',ms=20)
            #plt.axes().set_facecolor("#BED754")
            #plt.axes().tick_params(axis="x", colors="#BED754")      # x tick labels
            #plt.axes().tick_params(axis="y", colors="#BED754")   # y tick labels

            #plt.grid()
            file_name = "absolute_chart_" + str(uuid.uuid1()) + ".png"
            plt.savefig('assets/' + file_name)
            #plt.show()
        context = {"form_submitted":True , "result" : result, "file_name": file_name, "absolute_form": absolute_form}
    else:
        absolute_form = Absolute_Form()   
        context = {"form_submitted":False, "absolute_form": absolute_form}
    return render(request, "absolute.html", context) # goes inside views.py
