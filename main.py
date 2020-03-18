from flask import Flask ,redirect,url_for,request,render_template
from flask_assets import Bundle, Environment
from flask_fontawesome import FontAwesome
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import pyrebase
from firebase import firebase
#from flask_pymongo import PyMongo
#from pymongo import MongoClient

app = Flask(__name__)
fa = FontAwesome(app)
js = Bundle('material-dashboard.min.js', 'demo.js',
            'material-dashboard.js', output='gen/main.js')
assets = Environment(app)
assets.register('main_js', js)

# Initialize the extension
GoogleMaps(app)
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDP0GX-Wsui9TSDxtFNj2XuKrh7JBTPCnU"

# data calling form firebase
from firebase import firebase
firebase = firebase.FirebaseApplication("https://testapp1-bd305.firebaseio.com/", None)

@app.route("/map")
def map():
    # a = request.args.get('a')
    # b = request.args.get('b')
    # a1=float(a)
    # b1=float(b)
    # map = Map(
    #     identifier="map",
    #     varname="map",
    #     style=(
    #         "height:100%;"
    #         "width:100%;"
    #         "top:0;"
    #         "left:0;"
    #         "position:absolute;"
    #         "z-index:200;"
    #     ),
    #     lat=float(a),
    #     lng=float(b),
    #     markers=[(a1, b1)],
    #     # maptype = "TERRAIN",
    #     zoom="17"
    # )
    return render_template(
        'map.html'
    )

@app.route('/')
def dashboard():
    return render_template('dashboard.html')
@app.route('/info')
def info():
    dic_info={}
    name = request.args.get('name')
    complaint = request.args.get('complaint')
    status = request.args.get('status')
    time = request.args.get('time')
    imei = request.args.get('imei')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    pno = request.args.get('pno')
    dic_info['name']=name
    dic_info['complaint'] = complaint
    dic_info['status'] = status
    dic_info['time'] = time
    dic_info['imei'] = imei
    dic_info['lat'] = lat
    dic_info['lon'] = lon
    dic_info['pno'] = pno


    return render_template('info.html', my_var=dic_info)




if __name__ =='__main__':
    app.run(debug=True)
