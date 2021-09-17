from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import exercises_model,part_model
from django.http import Http404

# Create your views here.

class show_exercise(View):
    def get(self,request,part,wid):
        exercise=get_object_or_404(exercises_model,id=wid)
        if part==exercise.part.name:
            return render(request,'workouts/show_exercise.html',context={
                'exercise':exercise})
        else:
            raise Http404

class show_part(View):
    def get(self,request,part_name):
        parts=part_model.objects.all()
        part_name_list=[]
        for p in parts:
            part_name_list.append(p.name)
        if part_name in part_name_list:
            all_exercises=exercises_model.objects.all()
            return render(request,'workouts/show_part_exercise.html',context={
                'all_exercises':all_exercises,'part':part_name})
        else:
            raise Http404

class part_index(View):
    def get(self,request): 
        parts=part_model.objects.all()
            
        return render(request,'workouts/part_index.html',context={
            'parts':parts})
        



         