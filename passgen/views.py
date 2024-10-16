import random
import string
from django.shortcuts import render
from django.http import HttpResponse

def generate_passwords(request):
    if request.method == "POST":
        try:
            num_passwords = int(request.POST.get('num_passwords'))
            length_password = int(request.POST.get('length_password'))
            
            if num_passwords <= 0 or length_password <= 0:
                raise ValueError

            passwords = []
            for _ in range(num_passwords):
                password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length_password))
                passwords.append(password)

            return render(request, 'index.html', {'passwords': passwords})
        
        except ValueError:
            return HttpResponse("Invalid input. Please enter positive numbers.", status=400)
    
    return render(request, 'index.html')
