from flask import Flask, render_template, request, make_response, redirect
from flask_bootstrap import Bootstrap
from datetime import datetime, tzinfo, timedelta
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask_wtf import Form
import pytz

app = Flask(__name__)
app.secret_key = 'development key'
Bootstrap(app)
tzdict = {'Tokyo':'Asia/Tokyo', 
            'St.Pete':'US/Eastern',
            'Tampa':'US/Eastern',
            'Paris':'Europe/Paris', 
            'Vancouver':'America/Vancouver',
            'Homburg':'Europe/Berlin',
            'Milano':'Europe/Rome',
            'London':'Europe/London',
            'Dallas':'US/Central',
            'San Jose':'US/Pacific',
            'New York':'US/Eastern',
            'Singapore':'Asia/Singapore',
            'IST':'Asia/Kolkata'} 
class CityForm(Form):
    city1 = SelectField(u'Left', 
        choices=[
            ('Tokyo', 'Tokyo'),
            ('St.Pete', 'St.Pete'),
            ('Paris', 'Paris'),
            ('London', 'London'),
            ('IST', 'IST'),
            ('New York', 'New York'),
            ('Singapore', 'Singapore'),
            ('San Jose', 'San Jose')
            ])
    city2 = SelectField(u'Center',
        choices=[
            ('Tokyo', 'Tokyo'),
            ('St.Pete', 'St.Pete'),
            ('Paris', 'Paris'),
            ('London', 'London'),
            ('IST', 'IST'),
            ('New York', 'New York'),
            ('Singapore', 'Singapore'),
            ('San Jose', 'San Jose')
            ])            
    city3 = SelectField(u'Right', 
        choices=[
            ('Tokyo', 'Tokyo'),
            ('St.Pete', 'St.Pete'),
            ('Paris', 'Paris'),
            ('London', 'London'),
            ('IST', 'IST'),
            ('New York', 'New York'),
            ('Singapore', 'Singapore'),
            ('San Jose', 'San Jose')
            ])
    city4 = SelectField(u'Right', 
        choices=[
            ('Tokyo', 'Tokyo'),
            ('St.Pete', 'St.Pete'),
            ('Paris', 'Paris'),
            ('London', 'London'),
            ('IST', 'IST'),
            ('New York', 'New York'),
            ('Singapore', 'Singapore'),
            ('San Jose', 'San Jose')
            ])
    submit = SubmitField('Submit')

def BuildTimezoneList(time1st, label):
    #time.strftime("%m/%d %H:%M")
    timelist = [label]
    timelist.append(time1st.strftime("%m/%d %a %H:00"))
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("%m/%d %a %H:00"))
    return timelist

def BuildTimezoneListnoYear(time1st, label):
    #time.strftime("%m/%d %H:%M")
    timelist = [label]
    timelist.append(time1st.strftime("%a %H:00"))
    for i in range(24):
        time1st = time1st + timedelta(hours=1)
        timelist.append(time1st.strftime("%a %H:00"))
    return timelist

@app.route("/", methods=['GET', 'POST'])
def index():
    form = CityForm()
    cities = request.cookies.get('cities')
    if not 'cities' in request.cookies:
        citylist= 'Tokyo,Singapore,IST,New York'.split(',')
        resp = make_response(redirect('/'))
        resp.set_cookie('cities', 'Tokyo,Singapore,IST,New York')
        return resp
    else:
        citylist = cities.split(',')
    
    if form.validate_on_submit():
        city1 = form.city1.data
        city2 = form.city2.data
        city3 = form.city3.data
        city4 = form.city4.data
        citylist[0]=city1
        citylist[1]=city2
        citylist[2]=city3
        citylist[3]=city4
        cities = city1 +',' + city2  + ',' + city3 + ',' + city4
        resp = make_response(redirect('/'))
        resp.set_cookie('cities', cities)
        return resp

    #cnt = len(citylist)
    cnt =4
    tzlist = list()
    loopCnt = 0
    for i in citylist:
        if loopCnt == 0:
            try:
                tzlist.append(BuildTimezoneList(datetime.now(pytz.timezone(tzdict[i])),i))
            except:
                resp = make_response(redirect('/'))
                resp.set_cookie('cities', 'Tokyo,Singapore,IST,New York')
                return resp
        else:
            try:
                tzlist.append(BuildTimezoneListnoYear(datetime.now(pytz.timezone(tzdict[i])),i))
            except:
                resp = make_response(redirect('/'))
                resp.set_cookie('cities', 'Tokyo,Singapore,IST,New York')
                return resp
        loopCnt +=1

    timenow=datetime.now().strftime("%m/%d %H:%M")

    form.city1.default = citylist[0]
    form.city2.default = citylist[1]
    form.city3.default = citylist[2]
    print(citylist[3])
    form.city4.default = citylist[3]
    form.process()
    #return render_template('index.html',cat1=cat1list,cat2=cat2list,cat3=cat3list,cat4=cat4list, timenow=timenow, cnt=cnt, tzlist=timezonelist )
    return render_template('index.html',cat1=tzlist[0],cat2=tzlist[1],cat3=tzlist[2],cat4=tzlist[3], timenow=timenow, cnt=cnt,  form=form, tzlist=citylist )
    # return render_template('index.html',cat1=tzlist[0],cat2=tzlist[1],cat3=tzlist[2], timenow=timenow, cnt=cnt,  form=form, tzlist=citylist )

@app.route("/p")
def mysite():
    tz_tokyo = pytz.timezone('Asia/Tokyo'   )
    tz_van = pytz.timezone('US/Pacific')
    tz_paris = pytz.timezone('Europe/Paris')
    tz_sp = pytz.timezone('US/Eastern')
    tz_NY = pytz.timezone('America/New_York')
    tz_IST = pytz.timezone('Asia/Kolkata')
    tz_Singapore = pytz.timezone('Asia/Singapore')


    cat1list=BuildTimezoneList(datetime.now(tz_tokyo), 'Tokyo')
    cat2list=BuildTimezoneListnoYear(datetime.now(tz_Singapore), 'Singapore')
    cat3list=BuildTimezoneListnoYear(datetime.now(tz_IST), 'IST')
    cat4list=BuildTimezoneListnoYear(datetime.now(tz_NY), 'New York')
    timenow=datetime.now().strftime("%m/%d %H:%M")
    cnt=4
    #return render_template('indexp.html',cat1=cat1list,cat2=cat2list,cat3=cat4list,timenow=timenow, cnt=cnt, tzlist='empty' )
    return render_template('indexp.html',cat1=cat1list,cat2=cat2list,cat3=cat3list, cat4=cat4list,timenow=timenow, cnt=cnt, tzlist='empty' )

@app.route("/setting")
def Setting():
    cities = request.cookies.get('cities')
    citylist = cities.split(',')
    
    return render_template('setting.html',citylist=citylist)

@app.route("/t")
def codetest():
    l1 = ['L1-1', 'L1-2', 'L1-3','L1-4']
    l2 = ['L2-1', 'L2-2', 'L2-3', 'L2-4']
    l3 = ['L3-1', 'L3-2', 'L3-3' , 'L3-4']
    return render_template('test.html',cat1=l1,cat2=l2,cat3=l3)

@app.route("/latest")
def mysitelatest():
    # Tokyo,Singapore,IST,New York
    tz_tokyo = pytz.timezone('Asia/Tokyo'  )
    # tz_van = pytz.timezone('US/Pacific')
    # tz_paris = pytz.timezone('Europe/Paris')
    # tz_sp = pytz.timezone('US/Eastern')
    # tz_zu = pytz.timezone('Europe/Zurich')

    tz_van = pytz.timezone('US/Pacific')
    tz_Singapore = pytz.timezone('Asia/Singapore')
    tz_IST = pytz.timezone('Asia/Kolkata')
    tz_NY = pytz.timezone('America/New_York')

    cat1list=BuildTimezoneList(datetime.now(tz_tokyo), 'Tokyo')
    cat2list=BuildTimezoneListnoYear(datetime.now(tz_Singapore), 'Singapore')
    cat3list=BuildTimezoneListnoYear(datetime.now(tz_IST), 'IST')
    cat4list=BuildTimezoneListnoYear(datetime.now(tz_NY), 'New York')
    timenow=datetime.now().strftime("%m/%d %H:%M")
    cnt=4
    #return render_template('indexp.html',cat1=cat1list,cat2=cat2list,cat3=cat4list,timenow=timenow, cnt=cnt, tzlist='empty' )
    return render_template('latestpic.html',cat1=cat1list,cat2=cat2list,cat3=cat3list,cat4=cat4list,timenow=timenow, cnt=cnt, tzlist='empty' )



if __name__ == '__main__':
    app.run(debug=True)
