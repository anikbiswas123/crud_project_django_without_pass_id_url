from django.shortcuts import render,redirect
from .models import person

# Create your views here.
def showPerson(request):
    perobj=person.objects.all()
    return render(request,'ShowData.html',locals())

def Addperson(request):
    if request.method == 'POST':
        p_name=request.POST.get('p_name')
        p_add=request.POST.get('p_add')
        p_phone=request.POST.get('p_phone')
        
        if p_name and p_add and p_phone :
            person.objects.create(p_name=p_name,p_address=p_add,p_phone=p_phone)
            return redirect(showPerson)
    return render(request,'addperson.html')

# def EditPerson(request):
    
#         edit_info = ""
#         edit_id = ""
        
#         if request.method == 'POST' and 'edit' in request.POST:
#                edit_id = request.POST.get('edit_id')
#                if person.objects.filter(id = edit_id).exists():
#                     edit_info = person.objects.get(id = edit_id)
                   
     
#         if request.method == 'POST' and 'edit_info' in request.POST:
#            name = request.POST.get('p_name')
#            add = request.POST.get('p_add')
#            phone = request.POST.get('p_phone')
#            e_id = request.POST.get('id')
           
#            edit_info = person.objects.get(id = e_id)
#            edit_info.p_name = name
#            edit_info.p_address = add
#            edit_info.p_phone = phone
#            edit_info.save()
           
#            return redirect(showPerson)
#         return render(request,'edit_person.html',locals())    


def edit_customer(request):
    edit_info = ""
    edit_id = ""
    if request.method == 'POST' and 'edit' in request.POST:
        edit_id = request.POST.get('edit_id')
        if person.objects.filter(id = edit_id).exists():
            edit_info = person.objects.get(id = edit_id)
    
    if request.method == 'POST' and 'edit_info' in request.POST:
        p_name = request.POST.get('p_name')
        p_add = request.POST.get('p_add')
        p_phone = request.POST.get('p_phone')
        e_id = request.POST.get('id')
        edit_info = person.objects.get(id = e_id)
        edit_info.p_name = p_name
        edit_info.p_address = p_add
        edit_info.p_phone = p_phone
        edit_info.save()
        
        return redirect(showPerson)

    data = {
        'edit': 'edit',
        'edit_info': edit_info,
    }
    return render(request, "add_and_eidt.html",data)


def Delete_data(request):
     edit_id = ""
     if request.method == 'POST':
         p_id=request.POST.get('del_id')
         p_obj=person.objects.get(id=p_id)
         p_obj.delete()
         return redirect(showPerson)

def deltaisPer(request):
    if request.method == 'POST':
        p_id=request.POST.get('details_id')
        p_obj=person.objects.get(id=p_id)
    return render(request,'deltaiseperson.html',locals())     
         
   
    