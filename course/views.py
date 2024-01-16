from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"course/home.html")


from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import course
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

# Cr̥eate your views here.
class NewCourse(SuccessMessageMixin,CreateView):
    model = course
    fields = '__all__'
    success_message = "%(name)s is created"

class ViewCourse(ListView):
    model = course
    context_object_name = 'courses'

class UpdateCourse(SuccessMessageMixin,UpdateView):
    model = course
    fields = '__all__'
    success_message = "%(name)s is Updated"

class DeleteCourse(DeleteView):
    model = course
    success_url = '/course/view'
    success_message = "course was deleted successfully."

    def delete(self, request, *args, **kwargs):
        #messages.error(self.request, self.success_message)
        messages.success(self.request, self.success_message)
        return super(DeleteCourse, self).delete(request, *args, **kwargs)

class DetailCourse(LoginRequiredMixin,DetailView):
    model = course

def get_fees(request, course_id):
        courses = course.objects.get(pk=course_id);
        return JsonResponse({'fees': courses.fees});
