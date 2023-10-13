from django.shortcuts import render
from .form import registrationForm



# Create your views here.
def reg_form(r):
    form=registrationForm()
    if r.method=='POST':
        form=registrationForm(r.POST)
        if form.is_valid():
            form.save()
            form=registrationForm()

    return render(r,'form/registration.html',{'form':form})

# def fetch_data(r):
#     form=DataForm()
#     if r.method=='POST':
#         form=DataForm(r.POST)
#         if form.is_valid():
#             form.save()
#             form=DataForm()
#     return render(r,'cbv/view.html',{'key':form})