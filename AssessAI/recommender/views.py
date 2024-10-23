from django.shortcuts import render
import numpy as np
import pandas as pd
import joblib

model = joblib.load("recommender/models_and_file/assessai.pkl")

# Create your views here.
def home(request):
    return render(request, 'index.html')


def project(request):
    if request.method == "POST":
        preparation = request.POST.get("test-preparation")
        math = request.POST.get("month-score")
        reading = request.POST.get("reading-score")
        writing = request.POST.get("writing-score")
        gender = request.POST.get("gender")
        lunch = request.POST.get("lunch")
        parent = request.POST.get("parent-education")
        race = request.POST.get("race")
        gender = 0 if gender == "female" else 1
        lunch = 0 if lunch == "standard" else 1
        preparation = 0 if preparation == "completed" else 1
        math = int(math)
        reading = int(reading)
        writing = int(writing)
        if race == "groupA":
            race = [1, 0, 0, 0, 0]
        elif race == "groupB":
            race = [0, 1, 0, 0, 0]
        elif race == "groupC":
            race = [0, 0, 1, 0, 0]
        elif race == "groupD":
            race = [0, 0, 0, 1, 0]
        else:
            race = [0, 0, 0, 1, 0]
        if parent == "associate":
            parent = [1, 0, 0, 0, 0, 0]
        elif parent == "bachelor":
            parent = [0, 1, 0, 0, 0, 0]
        elif parent == "high-school":
            parent = [0, 0, 1, 0, 0, 0]
        elif parent == "masters":
            parent = [0, 0, 0, 1, 0, 0]
        elif parent == "some-college":
            parent = [0, 0, 0, 0, 1, 0]
        else:
            parent = [0, 0, 0, 0, 0, 1]
        arr = [gender, lunch, preparation, math, reading, writing]
        for x in race:
            arr.append(x)
        for y in parent:
            arr.append(y)
        print(np.array([arr]))
        prediction = model.predict(np.array([arr]))
        print(prediction)
        return render(request, "Project.html", {"prediction":prediction[0] + 1})
    return render(request, "Project.html")