from django import forms
from.models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields= '__all__'


        ##listado de campos del modelo de Contacto despues lo pasamos a la vista



    


    
#






