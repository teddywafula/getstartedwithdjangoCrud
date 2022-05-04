from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
# Create your views here.


def index(request):
    members = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {"members": members}
    return HttpResponse(template.render(context, request))


def create(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render({},request))


def store(request):
    first = request.POST['firstname']
    last = request.POST['lastname']
    member = Members(firstname=first, lastname=last)
    member.save()

    return HttpResponseRedirect(reverse('index'))


def edit(request,member_id):
    member = Members.objects.get(id=member_id)
    template = loader.get_template('edit.html')
    context = {"member": member}
    return HttpResponse(template.render(context, request))


def update(request, member_id):
    member = Members.objects.get(id=member_id)
    first = request.POST['firstname']
    last = request.POST['lastname']
    member.firstname = first
    member.lastname = last
    member.save()

    return HttpResponseRedirect(reverse('index'))


def show(request,member_id):
    member = Members.objects.get(id=member_id)
    template = loader.get_template('show.html')
    context = {"member": member}
    return HttpResponse(template.render(context, request))


def delete(request,member_id):
    member = Members.objects.get(id=member_id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))