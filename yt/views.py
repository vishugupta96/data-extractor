from re import T
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from yt.decorators import allowed_users

import pandas as pd
import json
from django.contrib.auth.decorators import login_required
from .utills import twetter_scrap,linkedin_scrap ,youtube_extract,INSTAGRAM_DATA_EXTRACT

from yt.models import Client, Link
from .forms import ClientForm

import os

from django.http import HttpResponse, Http404
from datamine import settings

from django.http import request

def start(request):

    return render(request,'base1.html',{}) 



################################################################################

def dashboard(request):
    info_d = pd.read_csv("yt/utills/ig_info.csv")
    info_tweet = pd.read_csv("static/file/twetter.csv")
    info_yt = pd.read_csv("yt/utills/yt_info.csv")

    
    context = {
    'ig_media':info_d.iloc[0]['media_count'],
    'ig_followers':info_d.iloc[0]['followers'],
    'ig_following':info_d.iloc[0]['following'],
    'tweet_followers':info_tweet.iloc[0]['followers_count'],
    'tweet_friends':info_tweet.iloc[0]['friend_count'],

    'yt_followers':info_yt.iloc[0]['followers'],
    'yt_following':info_yt.iloc[0]['lifetime_views'],
    
    }

    return render(request,'main-dashboard.html',context)




#################################################################################
@login_required(login_url='main:login')
@allowed_users(allowed_roles=['admin','client', 'manager'])

def youtube(request):
    vid_path = os.path.join(settings.MEDIA_ROOT,'yt_videos.csv')
    comm_path = os.path.join(settings.MEDIA_ROOT,'yt_comments.csv')
    if request.method == 'GET':
        t = os.path.join(settings.MEDIA_ROOT,'yt_info.csv')
        info_yt = pd.read_csv(t)
        t = os.path.join(settings.MEDIA_ROOT,'yt_videos.csv')
        video_yt = pd.read_csv(t)
        t = os.path.join(settings.MEDIA_ROOT,'yt_comments.csv')
        comments_yt = pd.read_csv(t)

        json_records = video_yt.reset_index().to_json(orient ='records')
        data_v = []
        data_v = json.loads(json_records)

        json_records = comments_yt.reset_index().to_json(orient ='records')
        data_c = []
        data_c = json.loads(json_records)


        

        context = { 
        'yt_followers':info_yt.iloc[0]['followers'],
        'yt_following':info_yt.iloc[0]['lifetime_views'],
        'yt_comments_count':info_yt.iloc[0]['comments_count'],
        'video_yt' : data_v,
        'comments_yt':data_c,
        'file_url_1':'/file/yt_info.csv',
        'file_url_2':vid_path,
        'file_url_3':comm_path}

    if request.method =='POST':
        youtube = youtube_extract.yt_data_mine()

        t = os.path.join(settings.MEDIA_ROOT,'yt_info.csv')
        info_yt = pd.read_csv(t)
        t = os.path.join(settings.MEDIA_ROOT,'yt_videos.csv')
        video_yt = pd.read_csv(t)
        t = os.path.join(settings.MEDIA_ROOT,'yt_comments.csv')
        comments_yt = pd.read_csv(t)

        json_records = video_yt.reset_index().to_json(orient ='records')
        data_v = []
        data_v = json.loads(json_records)

        json_records = comments_yt.reset_index().to_json(orient ='records')
        data_c = []
        data_c = json.loads(json_records)
        

        # video_yt.to_csv('static/file/yt_videos.csv', index=False)
        # comments_yt.to_csv('static/file/yt_comments.csv', index=False)

        #info to array then into a file and then to frontend

        context = { 
        'yt_followers':youtube['followers'],
        'yt_following':youtube['lifetime_views'],
        'yt_comments_count':youtube['comments_count'],
        'video_yt' : data_v,
        'comments_yt':data_c,
        'file_url_1':'/file/yt_info.csv',
        'file_url_2':vid_path,
        'file_url_3':comm_path
        }

    return render(request,'yt_table.html',context)

#################################################################################
@login_required(login_url='main:login')
@allowed_users(allowed_roles=['admin','client', 'manager'])
#twetter
def house(request):
    if request.method == 'GET':
        t = os.path.join(settings.MEDIA_ROOT,'twetter.csv')
        print('t: ', str(t))
        df = pd.read_csv(t,on_bad_lines='skip')
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context = {'d': data,'file_url':'/file/twetter.csv'}

    if request.method == 'POST':
        screen = request.POST.get('screen')
        print(screen)

        ####prev main and youtube####

        id = '3'

        c_data =  Client.objects.get(id = id)
        print(c_data.username)

        twitter_scrap = twetter_scrap.twetter_data_mine(c_data, screen)
        # youtube = youtube_extract.yt_data_mine()
        #######

        t = os.path.join(settings.MEDIA_ROOT,'twetter.csv')
        print('t: ', str(t))

        df = twitter_scrap
        df.to_csv('tt.csv')
        c_data.twitter_file_url = t
        c_data.save()    
        # parsing the DataFrame in json format.
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context = {'d': data,'file_url':'/file/twetter.csv'}

    return render(request,'table.html',context)

################################################################################
#linked

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['admin','client', 'manager'])
def linked(request):
    #context = {'d': {},'c': {},'file_url':'/file/linked1.json','file_2_url':'/file/linked3.json'}

    if request.method == 'GET':
        
        t = os.path.join(settings.MEDIA_ROOT,'linked1.csv')
        print('t: ', str(t))
        
        l = os.path.join(settings.MEDIA_ROOT,'linked3.csv')
        print('l: ', l)


        linked_df1 = pd.read_csv(t, on_bad_lines='skip')
        json_records = linked_df1.reset_index().to_json(orient ='records')
        data_c = []
        data_c = json.loads(json_records)


        linked_df2 = pd.read_csv(l, on_bad_lines='skip')
        json_records = linked_df2.reset_index().to_json(orient ='records')
        data_v = []
        data_v = json.loads(json_records)

        context = {'d': data_c,'c': data_v,'file_url':'/file/linked1.json','file_2_url':'/file/linked3.json'}

    if request.method == 'POST':
        dict_1,dict_2 = linkedin_scrap.link_mine()

        ####prev main and youtube####
        json_object = json.dumps(dict_1, indent = 4)
        with open("static/file/linked1.csv", "w") as outfile:
            outfile.write(json_object)

        json_object = json.dumps(dict_2, indent = 4)
        with open("static/file/linked3.csv", "w") as outfile:
            outfile.write(json_object)

        context = {'d': dict_1,'c': dict_2,'file_url':'/file/linked1.json','file_2_url':'/file/linked3.json'}

    return render(request,'linked-table.html',context)

################################################################################

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['admin', 'manager'])
def insta(request):
    c_user = request.user
    print(c_user)
    l1 =  Link.objects.filter(user = c_user)
    #need to change
    #query set list give option to select
    print(l1[0].id)
    a = Client.objects.filter(link__id=l1[0].id)
    print(a)
    print(a[0].fb_client_id)
    if request.method == 'GET':

        df = pd.read_csv("yt/utills/ig_media.csv")
        # parsing the DataFrame in json format.
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)


        comm = pd.read_csv("yt/utills/ig_comments.csv")
        # parsing the DataFrame in json format.
        json_records = comm.reset_index().to_json(orient ='records')
        data_comm = []
        data_comm = json.loads(json_records)

        ins = pd.read_csv("yt/utills/ig_insights.csv")
        # parsing the DataFrame in json format.
        json_records = ins.reset_index().to_json(orient ='records')
        data_ins = []
        data_ins = json.loads(json_records)

        info_d = pd.read_csv("yt/utills/ig_info.csv")
        # parsing the DataFrame in json format.
        json_records = info_d.reset_index().to_json(orient ='records')
        data_info = []
        data_info = json.loads(json_records)

        context = {'d': data,
        'user': c_user,
        'c':data_comm,
        'e':data_ins,
        'f':data_info,
        'media':'/file/ig_media.csv',
        'insights':'/file/ig_insights.csv',
        'comments':'/file/ig_comments.csv'}
        return render(request,'ig_table.html',context)

#------------------post------------------------
    if request.method== 'POST':

        data_inta = INSTAGRAM_DATA_EXTRACT.instagram_extractor(a[0])

        df = pd.read_csv("yt/utills/ig_media.csv") 
        # parsing the DataFrame in json format.
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)


        comm = pd.read_csv("yt/utills/ig_comments.csv")
        # parsing the DataFrame in json format.
        json_records = comm.reset_index().to_json(orient ='records')
        data_comm = []
        data_comm = json.loads(json_records)

        ins = pd.read_csv("yt/utills/ig_insights.csv")
        # parsing the DataFrame in json format.
        json_records = ins.reset_index().to_json(orient ='records')
        data_ins = []
        data_ins = json.loads(json_records)

        info_d = pd.read_csv("yt/utills/ig_info.csv")
        # parsing the DataFrame in json format.
        json_records = info_d.reset_index().to_json(orient ='records')
        data_info = []
        data_info = json.loads(json_records)



        context = {'d': data,
        'user' : c_user,
        'c':data_comm,
        'e':data_ins,
        'f':data_info,
        'media':'/file/ig_media.csv',
        'insights':'/file/ig_insights.csv',
        'comments':'/file/ig_comments.csv'}
        return render(request,'ig_table.html',context)


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['admin', 'manager'])
def add_new(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    
    stud = Client.objects.all()
    return render(request,"ClientForm.html",{'form' : form,'stud':stud})

@login_required(login_url='main:login')

def delete_data(request,id):
    if request.method == "POST":
        pi = Client.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect("/client_new/")

@login_required(login_url='main:login')

def update_client(request, id):
    if request.method == "POST":
        print(request.POST)
        obj  = Client.objects.get(id = id)
        form = ClientForm(request.POST, instance = obj)
        if form.is_valid():
            # save the data from the form and
            # redirect to detail_view
            form.save()
            return HttpResponseRedirect('/'+"client-update/"+str(id)+"/")


    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Client, id = id)
 
    # pass the object as instance in form
    form = ClientForm( instance = obj)
 

    # add form dictionary to context
    context["form"] = form
 
    return render(request, "get_client.html", context)





