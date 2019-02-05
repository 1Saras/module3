from flask import Flask, render_template, request
from engine import Phonebook
import os

app = Flask(__name__)
phonebook = Phonebook()

@app.route('/')
def hello_world():
    return render_template("layouts/basepage.html")


@app.route('/businesses')
def allbusinesses():
    businesses = phonebook.get_all_businesses()
    return render_template('pages/allbusinesses.html', businesses = businesses)

@app.route('/people')
def allpeople():
    people = phonebook.get_all_people()
    return render_template('pages/allpeople.html', people=people)




@app.route('/findbusiness', methods=['GET','POST'])
def searchbusiness():
    categories = sorted([i[0].strip() for i in list(set(phonebook.get_categories()))])
    cities = sorted([i[0].strip() for i in list(set(phonebook.get_cities()))])

    if request.method =='GET':

        return render_template('pages/findbusiness.html', categories=categories, cities=cities)
    elif request.method=='POST':
        business_input = request.form.get('bizname', None)
        category = request.form.get('biz_cat', None)
        location = request.form.get('biz_loc', None)
        search = phonebook.find_business(biz_name=business_input, category=category, location=location)
        return render_template('pages/findbusiness.html', categories=categories, cities=cities, search=search)

    else:
        print("Hold on")

if __name__ == '__main__':
    app.run()
