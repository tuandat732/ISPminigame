from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hellobanhiendcmbannhe'


@app.route('/check',methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template('index.html')
    elif request.method=="POST":
        form =request.form
        passw = form['pass']
        if(passw=='THEUPSIDEDOWN'):
            return render_template("index.html",check=True,link='./static/anh/1.png')
        elif(passw=='openthenextdoor'):
            return render_template("index.html",check=True,link='./static/anh/2.png')
        elif(passw=="specialjourney"):
            return render_template("index.html",check=True,link='./static/anh/3.png')
        elif(passw=='f1n4l_ch4ll_d0n3'):
            return render_template("index.html",check=True,link='./static/anh/4.png')
        else:
            return redirect('/check')

@app.route('/')
def indexx():
   return render_template("D18.html")

girls=[
    {"id":1,
    "name":"Irene",
    "link":"../static/girls/Irene.jpg",
    "count":"../static/count/lucgiac.png",
    "font":"false"
},
{
    "id":2,
    "name":"j_ssica",
    "link":"../static/girls/jessica.jpg",
    "count":"../static/count/ngugiac.png",
    "font":"true"
},
{
    "id":3,
    "name":"jis_o",
    "link":"../static/girls/jisoo.jpg",
    "count":"../static/count/sao.png",
    "font":"false"
},
{
    "id":4,
    "name":"Kyulkyun_",
    "link":"../static/girls/Kyulkyung.jpg",
    "count":"../static/count/tamgiac.png",
    "font":"true"
},
{
    "id":5,
    "name":"Ro_e",
    "link":"../static/girls/rose.jpg",
    "count":"../static/count/tim.png",
    "font":"false"
},
{
    "id":6,
    "name":"_ana",
    "link":"../static/girls/sana.jpg",
    "count":"../static/count/tron.png",
    "font":"true"
},
{
    "id":7,
    "name":"Se_lhyun",
    "link":"../static/girls/Seolhyun.jpg",
    "count":"../static/count/tugiac.png",
    "font":"false"
},
{
    "id":8,
    "name":"s_mi",
    "link":"../static/girls/somi.jpg",
    "count":"../static/count/vuong.png",
    "font":"true"
},
{
    "id":9,
    "name":"_zuyu",
    "link":"../static/girls/tzuyu.jpg",
    "count":"../static/count/ngugiac.png",
    "font":"false"
},
{
    "id":10,
    "name":"yo_na",
    "link":"../static/girls/yoona.jpg",
    "count":"../static/count/lucgiac.png",
    "font":"false"
}

]
@app.route('/show',methods=["POST","GET"])
def show():
    if request.method=="GET":
        return render_template("show.html",girls=girls)
    elif request.method=="POST":
        form =request.form
        passw = form['key1']+form['key2']+form['key3']+form['key4']
        if(passw=='9035'):
            return render_template("show.html",girls=girls,check=True)
        else:
             return render_template("show.html",girls=girls,check=False)

@app.route('/faded')
def faded():
    return render_template("minigame.html")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 