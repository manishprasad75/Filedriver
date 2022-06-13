from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .serializers import FileSerializer
from .models import File
from django.core.files.storage import FileSystemStorage
import uuid


@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == "GET":
        user = request.user.id
        all_files = File.objects.filter(user_id=user)
        serialized = FileSerializer(all_files, many=True)
        data = serialized.data
        context = {"data": data}
        return render(request, 'index.html', context)
        return JsonResponse({"msg": "work"})


@login_required(login_url="/accounts/login/")
def upload_file(request):
    context = {}
    if request.method == "POST":
        user = request.user
        unique_name = str(uuid.uuid4())
        file_name = request.FILES['video'].name
        file_location = unique_name + file_name
        myfile = request.FILES['video']

        fs = FileSystemStorage("media/")
        filename = fs.save(file_location, myfile)

        video = File(user_id=user, file_name=file_name, file_location="media/" + file_location)
        video.save()
        print(context)
        return redirect("index")

    return render(request, 'update_page.html', context)


