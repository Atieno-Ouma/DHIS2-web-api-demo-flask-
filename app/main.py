
from flask import Flask
from flask import render_template
import requests
import pandas as pd
from werkzeug.wrappers import json

auth = {
    "user": "admin",
    "password": "district"
}

app= Flask(__name__)
@app.route('/')
def index():

    data_elements_url = "https://play.dhis2.org/2.34.6/api/dataElements"
    data_elements = get_json(data_elements_url, auth)['dataElements']

    print(data_elements)
    #final_dict = data_elements.items()
    final_df= pd.DataFrame.from_records(data_elements)

    print(final_df)




    return render_template("home.html",tables=[final_df.to_html(classes='data')], titles=final_df.columns.values)



def get_json(url, auth):
    user = auth['user'];
    password = auth['password']

    r = requests.get(url, auth=(user, password))
    return r.json()


