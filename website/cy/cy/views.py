# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from reports.models import Reports

def home(request):
    if 'search' in request.GET:
        search = request.GET['search']
        results = Reports.objects.filter(name=search)
        if results:
            return redirect(reverse('people:personal_property', kwargs={"name": search, "index": "overview"}))
        results = Reports.objects.filter(department=search)
        if results:
            return redirect('people/departments/#%s' % search)
        return render(request,'home.html', {'no_results': True})
    return render(request,'home.html', {})

def about(request):
    return render(request,'about.html', {})

def reference(request):
    return render(request,'reference.html', {})
