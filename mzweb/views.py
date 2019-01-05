# -*- coding: utf-8 -*-
 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render
import face_recognition
import PIL.Image as Image
import os
import base64
import PIL.ImageDraw as ImageDraw
from django.http import HttpResponse

@csrf_exempt
def mz_api(request):
    if request.method == 'POST':
        r=int(request.POST.get('r',0))
        g=int(request.POST.get('g',0))
        b=int(request.POST.get('b',0))
        img=request.FILES.get('img',None)
        if not img:
            return JsonResponse({"result": -3, "data": "error"})
        key=str(request.POST.get('key'))+os.path.splitext(img.name)[1]
        path = default_storage.save(img.name, ContentFile(img.read()))
        tmp_file = os.path.join('./', path)
        image = face_recognition.load_image_file(img.name)
        face_landmarks_list = face_recognition.face_landmarks(image)
        for face_landmarks in face_landmarks_list:
            pil_image = Image.fromarray(image)
            d = ImageDraw.Draw(pil_image, 'RGBA')    
            # Gloss the lips
            d.polygon(face_landmarks['top_lip'], fill=(r, g, b, 64))
            d.polygon(face_landmarks['bottom_lip'], fill=(r, g, b, 64))
        pil_image.save(key)
        with open(key, 'rb') as f:
            response = HttpResponse(f,content_type="image/"+os.path.splitext(img.name)[1][1:])
            response['Content-Disposition'] = 'attachment; filename='+key
        os.remove(key)
        os.remove(img.name)
        return response

    return JsonResponse({"result": 0, "data": "error"})
