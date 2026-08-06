from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from django.shortcuts import render
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def abc(request):
    return render(request,"abc.html")

@login_required(login_url='login')

def led(request):
    return render(request,"led.html")

@login_required(login_url='login')

def index(request):
    return render(request,"index.html")

@login_required(login_url='login')
def counter(request):
    if(request.method=="POST"):
        data=request.POST
        result=data.get('result')
        if result=="":
            result=0
        else:
            result=int(data.get("result"))
        if("increment" in request.POST):
            result+=1
            return render(request,"counter.html",context={'result':result})
        if("decrement" in request.POST):
            result-=1
            return render(request,"counter.html",context={'result':result})
        if("reset" in request.POST):
            result=0
            return render(request,"counter.html",context={'result':result})
    return render(request,"counter.html")

@login_required(login_url='login')
def email(request):
    return render(request,"email.html")

@login_required(login_url='login')
def calci(request):
    if(request.method=="POST"):
        data=request.POST
        first=int(data.get('firstnumber'))
        second=int(data.get('secondnumber'))
        fav=int(data.get('favnumber'))
        if('buttonadd' in request.POST):
            result=first+second
            return render(request,"calci.html",context={'result':"sum="+str(result)})
        if('buttonsub' in request.POST):
            result=first-second
            return render(request,"calci.html",context={'result':"sub="+str(result)})
        if('buttonmul' in request.POST):
            result=first*second
            return render(request,"calci.html",context={'result':"mul="+str(result)})
        if('buttondiv' in request.POST):
            result=first/second
            return render(request,"calci.html",context={'result':"div="+str(result)})
        if('buttonfav' in request.POST):
            result=fav
            return render(request,"calci.html",context={'result':"fav="+str(result)})
    
    return render(request,"calci.html")  


def Employee(request):
    if (request.method=="POST"):
        data=request.POST
        Ename=data.get('employeename')
        Edesignation=data.get('employeedes')
        Eplace=data.get('employeeplace')
        Employee_Table.objects.create(EMP_NAME=Ename,EMP_DES=Edesignation,EMP_Place=Eplace)
        result="Employee details saved Successfully!!"
        return render(request,"Employee.html",context={'result':result})
    return render(request,"Employee.html")

@login_required(login_url='login') 
def Employee_View(request):
    getEmployee=Employee_Table.objects.all()
    return render(request,"Employee_View.html",context={'getEmployee':getEmployee})

def Employee_update(request,id):
    getEmployee=Employee_Table.objects.get(id=id)
    if(request.method=="POST"):
        data=request.POST
        empname=data.get('employeename')
        empdes=data.get('employeedes')
        empplace=data.get('employeeplace')
        getEmployee.EMP_NAME=empname
        getEmployee.EMP_DES=empdes
        getEmployee.EMP_Place=empplace
        getEmployee.save()
        return redirect('/Employee_View/')
    return render(request,"Employee_update.html",context={'getEmployee':getEmployee})


def Employee_delete(request,id):
    getEmployee=Employee_Table.objects.get(id=id)
    if(request.method=="POST"):
        data=request.POST
        getEmployee.delete()
        return redirect('/Employee_View/')
    return render(request,'Employee_delete.html',context={'getEmployee':getEmployee})

    
def SignupPage(request):
    if(request.method=="POST"):
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password asre not matching")
            print("Your password and confirm password asre not matching")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/login/')
    return render(request,"signup.html")
    
def LoginPage(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/index/')
        else:
            result="Wrong password!!!"
            return HttpResponse("Username or Password is Incorrect!!")
    return render(request,'login.html')
    
def LogoutPage(request):
    logout(request)
    return redirect('/login/')
        
def predict(request):
    if(request.method=="POST"):
        data=request.POST
        hours=float(data.get('texthours'))
        age=int(data.get('textage'))
        internet=bool(data.get('textinternet'))
        if('buttonadd' in request.POST):
            import pandas as pd
            path=r"C:\Users\Yashaswini A\Data\Data\Exammarks.csv"
            data=pd.read_csv(path)
            medianvalue=data.hours.median()
            data.hours=data.hours.fillna(medianvalue)
            inputs=data.drop('marks',axis=1)
            output=data.drop(['hours','age','internet'],axis=1)
            import sklearn
            from sklearn import linear_model
            model=linear_model.LinearRegression()
            model.fit(inputs,output)
            result=model.predict([[hours,age,internet]])
            return render(request,'predict.html',context={'result':"Marks="+str(result[0][0])})
        
    return render(request,'predict.html')


def social(request):
    if(request.method=="POST"):
        data=request.POST

        gender=int(data.get('textgender'))
        age=int(data.get('textage'))
        salary=float(data.get('textsalary'))

        if('buttonpredict' in request.POST):

            import pandas as pd
            path=r"C:\Users\Yashaswini A\Data\Data\Social_Network_Ads.csv"
            data=pd.read_csv(path)

            # Convert Gender to numeric
            data['Gender'] = data['Gender'].map({'Male':1,'Female':0})

            # Inputs and Outputs
            inputs=data[['Gender','Age','EstimatedSalary']]
            output=data['Purchased']

            from sklearn.linear_model import LogisticRegression
            model=LogisticRegression()

            model.fit(inputs,output)

            result=model.predict([[gender,age,salary]])

            if result[0]==1:
                prediction="User will Purchase the Product"
            else:
                prediction="User will NOT Purchase the Product"

            return render(request,'social.html',context={'result':prediction})

    return render(request,'social.html')

def classify(img_file):
    data = []
    labels = []
    classes = 4
    cur_path = os.getcwd() #To get current directory


    classs = {  0:"Kingfisher",
    1:"Parrot",
    2:"Peacock",
    3:"Pigeon"  
    }
    model_path = os.path.join(settings.BASE_DIR, 'ANN_multi', 'ANN_multi','my_model_ann.h5')
    model = load_model(model_path)
    print("Loaded model from disk")
    path2="uploads//"+img_file
    print(path2)
    test_image = Image.open(path2)
    test_image = test_image.resize((30, 30))
    test_image = np.expand_dims(test_image, axis=0)
    test_image = np.array(test_image)
    predict_x=model.predict(test_image)
    result=np.argmax(predict_x,axis=1)
    sign = classs[int(result) ]        
    print(sign) 
    return sign



def Classification(request):
    if request.method == 'POST':
        if 'myfile' in request.FILES:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save("uploads//"+myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            result=classify(myfile.name)
            return render(request, 'Classification.html', {'uploaded_file_url': uploaded_file_url,'result':"Predicited result  " +result })
        else:
            result = "Please upload an image."
            return render(request, 'Classification.html', {'result':result })
    return render(request,'Classification.html')


@login_required(login_url='login')
def banana_leaf(request):
    
    pred_svm = None
    pred_lr = None
    pred_knn = None
    svm_acc = None
    lr_acc = None
    knn_acc = None
    best_model = None
    best_prediction = None

    if request.method == "POST":
        import pandas as pd
        from sklearn.preprocessing import LabelEncoder
        from sklearn.svm import SVC
        from sklearn.linear_model import LogisticRegression
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import train_test_split

        # Load dataset
        data = pd.read_csv(r"C:\Users\Yashaswini A\Downloads\Project_Dataset_2026\Project_Dataset_2026\banana leaf dataset\banana_leaf_dataset.csv")

        # Encoding
        le_color = LabelEncoder()
        le_texture = LabelEncoder()
        le_soil = LabelEncoder()
        le_target = LabelEncoder()

        data["ColorIntensity"] = le_color.fit_transform(data["ColorIntensity"])
        data["Texture"] = le_texture.fit_transform(data["Texture"])
        data["SoilType"] = le_soil.fit_transform(data["SoilType"])
        data["DiseaseLabel"] = le_target.fit_transform(data["DiseaseLabel"])

        # Features & Target
        X = data.drop("DiseaseLabel", axis=1)
        y = data["DiseaseLabel"]

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Models
        svm = SVC()
        lr = LogisticRegression(max_iter=200)
        knn = KNeighborsClassifier()

        # Train
        svm.fit(X_train, y_train)
        lr.fit(X_train, y_train)
        knn.fit(X_train, y_train)

        # Accuracy
        svm_acc = accuracy_score(y_test, svm.predict(X_test))
        lr_acc = accuracy_score(y_test, lr.predict(X_test))
        knn_acc = accuracy_score(y_test, knn.predict(X_test))

        # User Input
        length = float(request.POST.get("LeafLength"))
        width = float(request.POST.get("LeafWidth"))
        color = request.POST.get("ColorIntensity")
        spots = int(request.POST.get("SpotsPresent"))
        moisture = float(request.POST.get("MoistureLevel"))
        texture = request.POST.get("Texture")
        humidity = float(request.POST.get("Humidity"))
        temp = float(request.POST.get("Temperature"))
        soil = request.POST.get("SoilType")

        # Transform input
        color = le_color.transform([color])[0]
        texture = le_texture.transform([texture])[0]
        soil = le_soil.transform([soil])[0]

        # DataFrame
        user_input = pd.DataFrame([[length, width, color, spots,
                                    moisture, texture, humidity, temp, soil]],
                                  columns=X.columns)

        # Predictions
        pred_svm = le_target.inverse_transform(svm.predict(user_input))[0]
        pred_lr = le_target.inverse_transform(lr.predict(user_input))[0]
        pred_knn = le_target.inverse_transform(knn.predict(user_input))[0]

        # Best Model
        accuracies = {
            "SVM": svm_acc,
            "Logistic Regression": lr_acc,
            "KNN": knn_acc
        }

        best_model = max(accuracies, key=accuracies.get)

        best_prediction = {
            "SVM": pred_svm,
            "Logistic Regression": pred_lr,
            "KNN": pred_knn
        }[best_model]
    
    return render(request, "banana_leaf.html", {
        "svm": pred_svm,
        "lr": pred_lr,
        "knn": pred_knn,
        "svm_acc": round(svm_acc * 100, 2) if svm_acc else None,
        "lr_acc": round(lr_acc * 100, 2) if lr_acc else None,
        "knn_acc": round(knn_acc * 100, 2) if knn_acc else None,
        "best_model": best_model,
        "best_prediction": best_prediction
    })




@login_required(login_url='login')
def cinnamon(request):
    
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score

    result = None
    knn_acc = lr_acc = svm_acc = 0
    best_algo = ""

    if request.method == "POST":

        # User input
        Moisture = float(request.POST['Moisture'])
        Ash = float(request.POST['Ash'])
        Volatile_Oil = float(request.POST['Volatile_Oil'])
        Acid_Insoluble_Ash = float(request.POST['Acid_Insoluble_Ash'])
        Chromium = float(request.POST['Chromium'])
        Coumarin = float(request.POST['Coumarin'])

        # Load dataset
        df = pd.read_csv(r"C:\Users\Yashaswini A\Downloads\Project_Dataset_2026\Project_Dataset_2026\cinnamon\balanced_cinnamon_quality_dataset.csv")
        df.columns = df.columns.str.strip()

        # 🔥 function INSIDE POST
        def find_col(keyword):
            for col in df.columns:
                if keyword in col.lower():
                    return col
            return None

        # Column mapping
        moisture_col = find_col("moisture")
        ash_col = find_col("ash")
        volatile_col = find_col("volatile")
        acid_col = find_col("acid")
        chromium_col = find_col("chromium")
        coumarin_col = find_col("coumarin")
        label_col = find_col("quality")

        # Features
        feature_cols = [moisture_col, ash_col, volatile_col, chromium_col, coumarin_col]

        if acid_col:
            feature_cols.append(acid_col)

        X = df[feature_cols]
        y = df[label_col]

        # Encode
        le = LabelEncoder()
        y = le.fit_transform(y)

        # Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Models
        knn = KNeighborsClassifier()
        lr = LogisticRegression(max_iter=200)
        svm = SVC()

        knn.fit(X_train, y_train)
        lr.fit(X_train, y_train)
        svm.fit(X_train, y_train)

        # Accuracy
        knn_acc = round(accuracy_score(y_test, knn.predict(X_test)) * 100, 2)
        lr_acc = round(accuracy_score(y_test, lr.predict(X_test)) * 100, 2)
        svm_acc = round(accuracy_score(y_test, svm.predict(X_test)) * 100, 2)

        # Prediction
        sample = [Moisture, Ash, Volatile_Oil, Chromium, Coumarin]

        if acid_col:
            sample.append(Acid_Insoluble_Ash)

        sample = [sample]

        pred = svm.predict(sample)
        result = le.inverse_transform(pred)[0]

        # Best model
        acc_dict = {
            "KNN": knn_acc,
            "Logistic Regression": lr_acc,
            "SVM": svm_acc
        }

        best_algo = max(acc_dict, key=acc_dict.get)

    return render(request, "cinnamon.html", {
        "result": result,
        "knn_acc": knn_acc,
        "lr_acc": lr_acc,
        "svm_acc": svm_acc,
        "best_algo": best_algo
    }) 