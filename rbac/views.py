from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views import View
from rbac.models import User,Role
from rbac.forms import UserForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class UserInfo(View):

    def get(self,request):

        users = User.objects.all()

        return render(request, 'user.html', {'users':users})

    def post(self,request):

        data= request.POST['case']
        print(data)

class RoleInfo(View):

    def get(self,request):

        roles = Role.objects.all()
        print('111')
        return render(request, 'role.html', locals())

def user_del(request):

    if request.method == 'GET':
        uid = request.GET.get('uid')

        User.objects.filter(id=uid).first().delete()
        # # print(request)
        # return redirect('rbac:user_list')
        data = {
            'deleted': True
        }
        return JsonResponse(data)



def user_edit(request,uid):
    obj = User.objects.filter(id=uid).first()
    if request.method == 'GET':
        form = UserForm(instance=obj)
        return render(request, 'user_edit.html', {'form':form})
    else:
        form = UserForm(data=request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('rbac:user_list')
        else:
            return render(request, 'user_edit.html', {'form':form})

def user_add(request):
    if request.method == 'GET':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rbac:user_list')
        else:
            return redirect('rbac:user_list',{'form':form})

    return render(request, 'user_add.html', {'form':form})

@csrf_exempt
def user_batch_del(request):


    checkval =  (request.POST.getlist('checkval'))

    for uid in checkval:
        User.objects.filter(id=uid).first().delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)