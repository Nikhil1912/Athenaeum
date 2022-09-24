from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book, Login
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Login and Encryption instructions from https://pythonguides.com/encrypt-and-decrypt-password-in-django/
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        encryptedpassword=make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword=check_password(request.POST['password'], encryptedpassword)
        print(checkpassword)
        data=Login(email=email, password=encryptedpassword)

        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'index.html')