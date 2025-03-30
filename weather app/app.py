from flask import Flask,render_template,request
import requests



app=Flask(__name__)

API_KEY="95c8073918781befdff1540a7c322fe5"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"


@app.route("/",methods=["GET","POST"])
def home():
    weather_data=None
    error=None

    if request.method == "POST":
        city=request.form["city"]
        
        if city:
            weather_req = {"q" : city ,"appid" :API_KEY, "units":"metrix" }
            result =  requests.get( BASE_URL, params=weather_req)

            if result.status_code == 200:
                weather_data = result.json()
            else:
                error="the request is bad.please try again later!!!"

    return render_template("index.html", weather=weather_data, error=error)

if __name__=="__main__":
    app.run(debug=True)



         