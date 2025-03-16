import datetime
import smtplib
from .aiqqualityhistory import dataget
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from myapp.models import *

# Create your views here.
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import base64
def logout(request):
    request.session['lid']=''
    return HttpResponse("<script>alert('Logouted'); window.location='/';</script>")


def loginTemp(request):
    return render(request, '../static/../templates/index.html')
def AdminHome(request):
    return render(request,'Admin/adminindex.html')
def feedback(request):
    ob=feedbacktbl.objects.all()
    return render(request,'Admin/feedback.html',{'data':ob})

def loginPost(request):
    usernaame=request.POST["textfield"]
    password=request.POST["textfield2"]

    a=  logintbl.objects.filter(username=usernaame, pasword=password)
    print(a)
    if a.exists():
        ob = logintbl.objects.get(username=usernaame, pasword=password)
        request.session['lid']=ob.id
        if ob.utype == 'admin':
            return HttpResponse("<script>alert('Success'); window.location='/AdminHome';</script>")
        elif ob.utype == 'expert':
            return HttpResponse("<script>alert('Success'); window.location='/expert_home';</script>")


        else:
            return HttpResponse("<script>alert('Not Found'); window.location='/';</script>")

    else:
        return HttpResponse("<script>alert('Not Found'); window.location='/';</script>")


def expert_Add(request):
    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        post=request.POST['post']
        mobileno=request.POST['mobileno']
        email=request.POST['email']

        aa=logintbl.objects.filter(username=email)
        if aa.exists():
            return HttpResponse("<script>alert('Username Already Taken'); window.location='/expert_Add';</script>")

        a=logintbl()
        a.username=email
        a.pasword=mobileno
        a.utype='expert'
        a.save()


        b=experttbl()
        b.LOGIN=a
        b.name=name
        b.email=email
        b.mobileno=mobileno
        b.Post=post
        b.place=place
        b.save()
        return HttpResponse("<script>alert('Added'); window.location='/expert_Add';</script>")
    return render(request,'admin/expertReg.html')


def admin_view_expert(request):
    a=experttbl.objects.all()
    return render(request,'admin/view_expert.html',{'data':a})

def edit_expert(request,id):
    a=experttbl.objects.get(id=id)
    return render(request,'admin/expert edit.html',{'data':a})


def edit_expert_post(request):
    id = request.POST['id']
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    mobileno = request.POST['mobileno']
    email = request.POST['email']

    # existing_user = logintbl.objects.filter(username=email).exclude(id=request.session['lid'])
    #
    # if existing_user.exists():
    #     return HttpResponse("<script>alert('Email Already Taken'); window.location='/admin_view_expert';</script>")

    expert = experttbl.objects.get(id=id)

    expert.name = name
    expert.email = email
    expert.mobileno = mobileno
    expert.Post = post
    expert.place = place
    expert.save()

    # login_entry = logintbl.objects.get(id=request.session['lid'])
    # login_entry.username = email
    # login_entry.save()

    return HttpResponse("<script>alert('Updated Successfully'); window.location='/admin_view_expert';</script>")


def delete_expert(request,id):
    a=experttbl.objects.get(id=id)
    a.delete()
    a.LOGIN.delete()
    return HttpResponse("<script>alert('Deleted'); window.location='/admin_view_expert';</script>")



def admin_view_user(request):
    a=usertbl.objects.all()
    return render(request,'admin/view user.html',{'data':a})


def admin_view_tips(request):
    a=tips_table.objects.all()
    return render(request,'admin/view tips.html',{'data':a})


def expert_home(request):
    return render(request,'Expert/expertindex.html')


def add_tips(request):
    if 'submit' in request.POST:
        tips=request.POST['tips']
        details=request.POST['details']

        a=tips_table()
        a.tips=tips
        a.details=details
        a.date=datetime.datetime.now().today().date()
        a.EXPERT=experttbl.objects.get(LOGIN_id=request.session['lid'])
        a.save()
        return HttpResponse("<script>alert('Added'); window.location='/add_tips';</script>")

    return render(request,'Expert/add tips.html')


def expert_view_tips(request):
    a=tips_table.objects.filter(EXPERT__LOGIN_id=request.session['lid'])
    return render(request,'Expert/view tips.html',{'data':a})


def delete_tips(request,id):
    a=tips_table.objects.get(id=id)
    a.delete()
    return HttpResponse("<script>alert('Deleted'); window.location='/expert_view_tips';</script>")


def edit_tips(request,id):
    a=tips_table.objects.get(id=id)
    if 'submit' in request.POST:
        id=request.POST['id']
        tips=request.POST['tips']
        details=request.POST['details']

        a=tips_table.objects.get(id=id)
        a.tips=tips
        a.details=details
        a.save()
        return HttpResponse("<script>alert('Updated'); window.location='/expert_view_tips';</script>")

    return render(request,'Expert/edit tips.html',{'data':a})


def add_solution(request):
    if 'submit' in request.POST:
        solution=request.POST['solution']

        a=Solutions()
        a.solution=solution
        a.date=datetime.datetime.now().today().date()
        a.EXPERT=experttbl.objects.get(LOGIN_id=request.session['lid'])
        a.save()
        return HttpResponse("<script>alert('Added'); window.location='/add_solution';</script>")

    return render(request,'Expert/add solution.html')
def expert_view_solutions(request):
    a=Solutions.objects.filter(EXPERT__LOGIN_id=request.session['lid'])
    return render(request,'Expert/view solution.html',{'data':a})


def delete_solution(request,id):
    a=Solutions.objects.get(id=id)
    a.delete()
    return HttpResponse("<script>alert('Deleted'); window.location='/expert_view_solutions';</script>")
def edit_solutions(request,id):
    a=Solutions.objects.get(id=id)
    if 'submit' in request.POST:
        id=request.POST['id']
        solution=request.POST['solution']

        a=Solutions.objects.get(id=id)
        a.solution=solution
        a.save()
        return HttpResponse("<script>alert('Updated'); window.location='/expert_view_solutions';</script>")

    return render(request,'Expert/edit solution.html',{'data':a})


def flutter_login(request):
    username = request.POST['username']
    password = request.POST['psw']
    a = logintbl.objects.filter(username=username, pasword=password)
    if a.exists():
        b = logintbl.objects.get(username=username, pasword=password)
        if b.utype == 'user':
            lid=b.id
            var=usertbl.objects.get(LOGIN_id=str(lid))

            return JsonResponse({"status": "ok", "lid":str(lid),'type':'user'})


        else:
            return JsonResponse({"status": "no"})


    else:

        return JsonResponse({"status":"no"})

def user_reg(request):
    name=request.POST['name']
    email=request.POST['email']
    mobileno=request.POST['mobileno']
    place=request.POST['place']
    latitude=request.POST['latitude']
    longitude=request.POST['longitude']
    password=request.POST['password']


    aa=logintbl.objects.filter(username=email)
    if aa.exists():
        return JsonResponse({'status': 'ok'})

    a=logintbl()
    a.pasword=password
    a.username=email
    a.utype='user'
    a.save()

    b=usertbl()
    b.LOGIN=a
    b.name=name
    b.email=email
    b.mobileno=mobileno
    b.place=place
    b.latitude=latitude
    b.longitude=longitude
    b.save()
    mail_code(email,"Hai "+name+", Welcome to air quality forecasting.")
    return JsonResponse({'status':'ok'})


def user_view_tips(request):
    a=tips_table.objects.all()
    l=[]
    for i in a:
        l.append({'id':i.id,'tips':i.tips,'details':i.details,'date':str(i.date),'EXPERT':i.EXPERT.name})
    print(l)
    return JsonResponse({'status':'ok','data':l})


def user_view_suggestions(request):
    a=Solutions.objects.all()
    l=[]
    for i in a:
        l.append({'id':i.id,'solution':i.solution,'date':str(i.date),'EXPERT':i.EXPERT.name})
    print(l)
    return JsonResponse({'status':'ok','data':l})


def user_send_feedback(request):
    lid=request.POST['lid']
    feedbacks=request.POST['feedback']
    a=feedbacktbl()
    a.feedback=feedbacks
    a.date=datetime.datetime.now().today()
    a.USERID=usertbl.objects.get(LOGIN_id=lid)
    a.save()
    return JsonResponse({'status':'ok'})





from django.http import JsonResponse
import json
from myapp.chatbot import AIR_QUALITY_RESPONSES

# Sample air quality dataset
from .chatbot import get_best_response,cb
def chatbot_response(request):
    print(request.POST)
    if request.method == "POST":
        user_message = request.POST.get('message', '').lower()
        response = cb(user_message)
        return JsonResponse({"response": response})


    return JsonResponse({"response": "Invalid request!"})


from django.shortcuts import render, redirect
from .models import dataset_table, experttbl
from django.http import HttpResponse

def add_dataset(request):
    if 'submit' in request.POST:
        question = request.POST['question']
        answer = request.POST['answer']

        expert = experttbl.objects.get(LOGIN_id=request.session['lid'])

        dataset_table.objects.create(
            question=question,
            answer=answer,
            date=datetime.datetime.now().today().date(),
            EXPERT=expert
        )
        return HttpResponse("<script>alert('Success'); window.location='/add_dataset';</script>")
    return render(request,'Expert/add dataset.html')


def expert_view_dataset(request):
    a=dataset_table.objects.filter(EXPERT__LOGIN_id=request.session['lid'])
    return render(request,'Expert/view dataset.html',{'data':a})

def delete_dataset(request,id):
    a=dataset_table.objects.get(id=id)
    a.delete()
    return redirect('/expert_view_dataset')


def edit_dataset(request,id):
    aa=dataset_table.objects.get(id=id)
    if 'submit' in request.POST:
        id = request.POST['id']
        question = request.POST['question']
        answer = request.POST['answer']

        expert =dataset_table.objects.get(id=id)

        dataset_table.objects.create(
            question=question,
            answer=answer,
        )
        return HttpResponse("<script>alert('Success'); window.location='/expert_view_dataset';</script>")
    return render(request,'Expert/edit dataset.html',{'data':aa})






def forecasting_code(x, y):
    import numpy as np
    print(x, y)
    import pandas as pd
    from statsmodels.tsa.arima.model import ARIMA
    from datetime import timedelta

    # Convert x to a pandas DateTime index if it represents time (e.g., days)
    # Here x should be numeric and represents sequential time points like [1, 2, 3, ...]
    dates = pd.date_range(start='2023-01-01', periods=len(x), freq='D')  # Adjust start date if necessary
    data = pd.Series(y, index=dates)

    # Train ARIMA model
    model = ARIMA(data, order=(5, 1, 0))  # ARIMA(p, d, q) parameters can be adjusted
    model_fit = model.fit()

    # Predict the next 7 days
    forecast = model_fit.forecast(steps=7)

    # Generate future dates for the next 7 days
    last_date = data.index[-1]  # Get the last date from the data
    future_dates = [last_date + timedelta(days=i) for i in range(1, 8)]  # Next 7 days

    # Return predicted values for the next 7 days as a list
    result = list(forecast)

    # Optionally, return the forecasted values with corresponding future dates
    forecast_df = pd.DataFrame({
        'date': future_dates,
        'predicted_value': forecast
    })

    print(forecast_df)  # Print the forecasted values with dates
    for i in range(0,len(forecast_df)):
        if result[i]<0:
            result[i]=0.0
        result[i]=round(result[i],2)
    return result  # Return the forecasted values for the next 7 days


API_KEY = "de474c37bfef960bc38f8b88bf88cf81dddf6c52"
from .airquality_prediction import forecast_data
def get_forcast_data(request):
    x,y=dataget()
    res=forecast_data(y)
    print(res)
    result=[]
    for i in range(0,len(res)):
        result.append(res[i][0])

    from datetime import datetime, timedelta

    # Get the current date
    current_date = datetime.today()

    # Generate the next 10 days from the current date
    dates = [current_date + timedelta(days=i) for i in range(len(res))]
    print(dates)
    print(result)
    forecast_datas=[]
    for i in range(len(result)):
        r={"day":dates[i],"max":result[i]}
        forecast_datas.append(r)

    return render(request, "forecastingindex.html", {"current_aqi": "", "graph_image": forecast_datas})
from .sam8ple import fetch_aqi_data_sug
def get_forcast_data1(request):
    location = "Kozhikode"  # Replace with your location or accept it as input

    # Fetch AQI data from WAQI API
    url = f"https://api.waqi.info/feed/{location}/?token={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        return render(request, "forecastingindex.html", {"message": "Failed to fetch AQI data."})

    # Current AQI and forecast data
    current_aqi = data["data"]["aqi"]
    forecast_data = data["data"].get("forecast", {}).get("daily", {}).get("pm25", [])
    print(current_aqi,"=================")
    print( data["data"],"=================")
    print(forecast_data,"=================")
    # Prepare data for graph
    dates = [item["day"] for item in forecast_data]
    aqi_values = [item["avg"] for item in forecast_data]

    # Create graph
    # plt.figure(figsize=(10, 5))
    # plt.plot(dates, aqi_values, marker="o", label="PM2.5 Forecast")
    # plt.title(f"AQI Forecast for {location}")
    # plt.xlabel("Date")
    # plt.ylabel("PM2.5 Levels")
    # plt.xticks(rotation=45)
    # plt.legend()
    # plt.tight_layout()
    #
    # # Save the plot to a string buffer
    # buffer = BytesIO()
    # plt.savefig(buffer, format="png")
    # buffer.seek(0)
    # graph_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
    # buffer.close()
    sug=fetch_aqi_data_sug(forecast_data[0]['max'])
    print(sug)
    ob=Solutions.objects.filter(solution='\n'.join(sug))
    if len(ob)==0:
        ob=Solutions()
        ob.solution='\n'.join(sug)
        ob.date=datetime.datetime.today()
        ob.EXPERT=experttbl.objects.get(LOGIN__id=request.session['lid'])
        ob.save()
    return render(request, "forecastingindex.html", {"current_aqi": "", "graph_image": forecast_data})


from email.mime.text import MIMEText
def mail_code(email,msg):

    try:

            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('hibamuhsinakm8005@gmail.com', 'pkpolwistnzbayfr')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText(msg)
            print(msg)
            msg['Subject'] = 'Air Quality Forecasting '
            msg['To'] = email
            msg['From'] = 'hibamuhsinakm8005@gmail.com'

            print("ok====")

            try:
                gmail.send_message(msg)
            except Exception as e:
                return ""
            return ""
    except Exception as e:
        print(e)
        return ""
