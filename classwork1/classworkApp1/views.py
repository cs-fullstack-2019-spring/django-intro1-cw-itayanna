

# imorting the respons function

from django.http import HttpResponse



# functions created to put a respons in eachof the paths

def index(request):
    return HttpResponse("This is a bad request. Start with the music route")

def music(request):
    return HttpResponse("Music: chronixx/ laurynHill/ jojo")

def chronixx(request):
    return HttpResponse('Jamar McNaughton, popularly known as Chronixx, is a Jamaican reggae artist. '
                        'His stage name replaced the name "Little Chronicle" which he was'
                        ' given because of his father, the singer "Chronicle". ')

def laurynHill(request):
    return HttpResponse('Lauryn Noelle Hill is an American singer, songwriter and rapper, known for being a member of Fugees and'
                        ' for her solo album The Miseducation of Lauryn Hill, which won many awards and broke several sales records.')

def jojo(request):
    return HttpResponse('Joanna Noëlle "JoJo" Levesque is an American singer, songwriter, and actress. Raised in '
                        'Foxborough, Massachusetts, she performed in various singing competitions as a child, and after competing on the ')

