from django.http import JsonResponse

from backend.models import Plane
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        data = {

            'name': user.name,
            'surname': user.surname,
            'username': user.username,
            'password': user.password
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    

def get_plane(request, plane_id):
    try:
        plane = Plane.objects.get(id=plane_id)
        data = {
            'id': plane.id,
            'brand': plane.brand,
            'category': plane.category,
            'colour': plane.colour,
            'weight': plane.weight
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Plane not found'}, status=404)

def get_planes(request):
    planes = Plane.objects.all()
    plane_list = []
    for plane in planes:
        plane_data = {
            'id': plane.id,
            'model': plane.model,
            'colour': plane.colour,
            'brand': plane.brand,
            'category':plane.category,
            'weight': plane.weight,
            'image':plane.image
        }
        plane_list.append(plane_data)

    return JsonResponse(plane_list, safe=False)
@csrf_exempt
def add_planes(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        category = request.POST.get("category")
        colour = request.POST.get("colour")
        weight = request.POST.get("weight")
        image = request.POST.get("image")

        plane = Plane.objects.create(
            brand=brand,
            category=category,
            colour=colour,
            weight=weight,
            image=image
        )

        return JsonResponse({"success": True, "plane_id": plane.id})
    else:
        return JsonResponse({"error": "Invalid request method."})


@csrf_exempt 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        # Kullanıcıyı users tablosundan kontrol etmek için authenticate() fonksiyonunu düzenliyoruz
        user = authenticate(request, username=username, password=password, backend='django.contrib.auth.backends.ModelBackend')
        
        if user is not None:
            login(request, user)
            return JsonResponse({"status":"ok"}) # Giriş başarılı olduğunda yönlendirilecek sayfa
        else:
            error_message = "Kullanıcı adı veya şifre hatalı."
            return  JsonResponse({"status":"false"})
    else:
        return render(request, 'login.html')
    

@csrf_exempt 
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        User.objects.create_user(username=username, password=password,first_name=name,last_name=surname)
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status":"ok"})
        else:
            return  JsonResponse({"status":"false"})  # Hatalı kayıt durumunda hata mesajını içeren template'i render et
    else:
        return render(request, 'register.html')