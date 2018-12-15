# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Blog
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_post(request):
    msg = ''
    success = False
    if request.method == 'POST':
            store = json.loads(request.body.decode("utf-8"))
            new_post = Blog()
            new_post.title = store['title']
            new_post.body = store['body']
            new_post.author = store['author']
            new_post.save()
            new_post.publish()
            success = True
            msg = "Post added Successfully!"
    else:
        msg = 'Not a Post request'
    return JsonResponse({
        'success' : success,
        'message' : msg
    })

def read_post(request, id):
    msg = ''
    success = False
    blog_json = {}

    if Blog.objects.filter(id=id).count():
        blog = Blog.objects.get(id=id)
        blog_json = {
            'title' : blog.title,
            'body' : blog.body,
            'author' : blog.author
        }
        msg = "Successfully fetched Blog"
        success = True
    else:
        msg = "Error while reading blog from database"
    
    return JsonResponse({
        'success':success,
        'message':msg,
        'blog':blog_json
    })

@csrf_exempt
def update_post(request, id):
    msg = ''
    success = False
    
    if request.method == 'POST':
        store = json.loads(request.body.decode("utf-8"))
        
        try:
            blog = Blog.objects.get(id=id)
        except:
            msg = "Error! No such post to edit!"
            return JsonResponse({'success':success,'message':msg})
        
        blog.title = store['title']
        blog.author = store['author']
        blog.body = store['body']
        blog.save()

        msg = "Successfully updated the blog"
        success = True
    else:
        msg = "Error! Not POST method"
    return JsonResponse({
        'success':success,'message':msg
        })

def delete_post(request, id):
    msg = ''
    success = False

    try:
            blog = Blog.objects.get(id=id)
    except:
        msg = "Error! No such post to delete!"
        return JsonResponse({'success':success,'message':msg})
    
    blog.delete()
    success = True
    msg = "Record Deleted Successfully!"

    return JsonResponse({
        'success' : success,
        'message' : msg
    })