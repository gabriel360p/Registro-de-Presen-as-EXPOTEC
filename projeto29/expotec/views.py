from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as error404
from django.http import HttpResponse
from . import urls
from .models import Matriculas, Presenca

def viewindex(request):
	return render(request,'dashboard.html')

def viewinsere(request):
	return render(request,'insere/insere.html')

def viewregistra(request):
	return render(request,'presenca/registra.html')

def viewlistapresencas(request):
	allpresencas = Presenca.objects.all()
	return render(request,'listas/listapresencas.html',{'presencas':allpresencas})

def viewinseridos(request):
	allmatriculas = Matriculas.objects.all()
	return render(request,'insere/inseridos.html',{'matriculas':allmatriculas})

#-----------------------------------------------

def definsere(request):
	if request.method=="POST":
		nomeinput = request.POST.get('nome')
		matriculainput = request.POST.get('matricula')

		try:
			buscar = error404(Matriculas,matmatricula=matriculainput)
			return render(request,'insere/insere.html',{'keepnome':nomeinput,'keepmatricula':matriculainput,'mensagemAlert':"Matricula Salva anteriormente"})
		except:
			pessoa = Matriculas(matmatricula=matriculainput, matpessoa=nomeinput)
			pessoa.save()
			return render(request,'insere/insere.html',{'keepnome':nomeinput,'keepmatricula':matriculainput,'mensagemAlert':"Usuario Salvo"})
	else:
		return render(request,'insere/insere.html',{'keepnome':nomeinput,'keepmatricula':matriculainput,'mensagemAlert':"Acesso GET NEGADO"})

def defpresenca(request):
	if request.method=="POST":
		matriculainput = request.POST.get('matricula')

		try:
			busca = error404(Matriculas,matmatricula=matriculainput)
			try:
				verfica = error404(Presenca,prematmatricula=matriculainput)
				return render(request,'presenca/registra.html',{'mensagemAlert':"Presença Registrada Anteriormente",'keepmatricula':matriculainput})
			except:
				try:
					consulta = Presenca(prematmatricula=matriculainput,prematpessoa=busca.matpessoa)
					consulta.save()
					return render(request,'presenca/registra.html',{'mensagemAlert':"Presença Registrada",'keepmatricula':matriculainput})
				except Exception as e110:
					print(e110)
					return render(request,'presenca/registra.html',{'mensagemAlert':"Erro ao registrar presença ",'keepmatricula':matriculainput})
		except:
			return render(request,'presenca/registra.html',{'mensagemAlert':"Matricula não encontrada",'keepmatricula':matriculainput})

	else:
		return render(request,'presenca/registra.html',{'keepmatricula':matriculainput,'mensagemAlert':"Acesso GET NEGADO"})


def defbusca(request):
	if request.method=="POST":
		buscainput = request.POST.get('busca')

		try:
			allresultados = Matriculas.objects.filter(matmatricula=buscainput)
			print(allresultados)
			return render(request,'resultados.html',{'resultados':allresultados,'savebusca':buscainput})
		except Exception as e125:
			print(e125)
			return render(request,'resultados.html',{'mensagemAlert':"Ocorreu um erro na busca",'savebusca':buscainput})
	else:
		return HttpResponse("Get Negado")