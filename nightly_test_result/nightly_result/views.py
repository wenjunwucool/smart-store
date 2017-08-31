# Create your views here.
#obj = Project.objects.get(name=project_name)
from django.http import HttpResponse
from nightly_result.forms import FileUploadForm
from django.shortcuts import render
def upload_file(request):
	if request.method == 'POST':
            my_form = FileUploadForm(request.POST, request.FILES)
            if my_form.is_valid():
                f = my_form.cleaned_data['my_file']
                handle_uploaded_file(f)
            return HttpResponse('Upload Success')
	else:
		my_form = FileUploadForm()
        return render(request,'upload_temp.html',{'form':my_form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

