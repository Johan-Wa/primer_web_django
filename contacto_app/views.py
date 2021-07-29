from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from .forms import FormularioContacto

# Create your views here.


def contacto(request):

    formulario_contacto = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid:
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email_s = EmailMessage("Mensaje desde la app de django",
            'El usuario con el nombre {}, y la dirección de email {} escribe:\n\n {}'.format(nombre,email,contenido),
            "",['johandavidgp@gmail.com'], reply_to=[email])

            try:
                email_s.send()

                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')
        
    
    return render(request, 'contacto_app/contacto.html', {
        'formulario': formulario_contacto
    })