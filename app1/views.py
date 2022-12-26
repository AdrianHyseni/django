from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
## Revers perdoret per te ber redirect ne nje faqe tjeter
from django.urls import reverse
import math as m

def sqrt_url(request,int):
    if int == 404:
        return HttpResponseNotFound("<h1>Numri 404 eshte i rezervuar</h1>")
    else:
        return HttpResponse(f'Ky eshte numri {int} dhe rrenja katrore eshte {m.sqrt(int)}')

# Create your views here.
def index(request):
    return HttpResponse("Faqa e pare")

### Bazat e pamjeve
def gjeo_page(request):
    return HttpResponse("Kjo eshte faqa e gjografise")

def text_page(request,text):
    return HttpResponse(f"Kjo eshte faqa e {text}")

def int_page(request,int):
    if int == 404:
        return HttpResponseNotFound("Me vjen keq nuk mund te procesojme 404")
    return HttpResponse(f"Numri eshte {int} dhe ky numer ne katror eshte {int*int}")

def redirect_page(request,str):
    if str == 'Home':
        return HttpResponseRedirect('/app1/',str)



#Krijo nje web ku te shkruash muajin dhe te dali nje sfid per ate muaj

muaji ={
    'Janar':'Abonohu ne palester',
    'Shkurt':'Merr badge si Arkitekt ',
    'Mars':'Vizito Vjenen',
    'Prill':'Nis patenten e motorrit',
    'Maj':'Humb 10Kg',
    'Qeshor':'Vizito Romen',
    'Korrik':'Meso AWS',
    'Gusht':'Certefikohu ne AWS',
    'Shtator':'Fillo te mesosh nje gjuh te huaj',
    'Tetor':'Vizito Budapestin',
    'Nentor':'Vizito Prizerenin',
    'Dhjetor':'Vizito Lyon per Krishlindje',

}


def sfida_mujore(request, month):
    sfida = muaji[month]
    return HttpResponse(f'Sfida per muajin {month} eshte: {sfida}')

def sfida_mujore_int(request, month_int):
    if month_int >=13:
        return HttpResponseNotFound("Muaji i 13-te nuk ekziston ne kalendar")
    lista_e_muajve = list(muaji.keys())
    redirect_month = lista_e_muajve[month_int-1] #list[3]
    redirect_path = reverse('sfida-mujore', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    #return HttpResponse(redirect_month)

def sfida(request):
    list_items = ""
    lista_muajve = list(muaji.keys())

    for muaj in lista_muajve:
        capitalized_m = muaj.capitalize()
        path_muaj = reverse('sfida-mujore', args=[capitalized_m])
        list_items += f'<li><a href ="{path_muaj}\">{capitalized_m}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def rendered_view(request):
    return render(request, 'html/index.html')

def sfida_rendered_view(request,text):
    try:
        sfida_muajit = muaji[text]
        return render(request, 'html/sfida.html',{"text":sfida_muajit,
                                                    "muaji":text.capitalize()})
    except:
        return HttpResponseNotFound('<h1>This month does not exists</h1>')

def faqa_kryesore_sfides(request):
    muajt = list(muaji.keys())
    return render(request, 'html/faqa_pare.html', {'muajt':muajt})
    