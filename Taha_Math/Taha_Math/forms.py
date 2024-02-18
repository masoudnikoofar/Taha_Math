from django import forms

class Fibonacci_Form(forms.Form):
    fibonacci_count = forms.IntegerField(label="چند عضو دنباله چاپ شوند")

class Factorial_Form(forms.Form):
    factorial_number = forms.IntegerField(label="فاکتوریل چه عددی محاسبه شود؟")

class Trigonometry_Form(forms.Form):
    trigonometry_degree = forms.FloatField(label="زاویه (درجه):")
    trigonometry_chart_degree_start = forms.IntegerField(label="زاویه شروع نمودار (درجه):")
    trigonometry_chart_degree_finish = forms.IntegerField(label="زاویه پایان نمودار (درجه):")

class Exponentiation_Form(forms.Form):
    exponentiation_base = forms.FloatField(label="پایه:")
    exponentiation_power = forms.IntegerField(label="توان:")
    