from flask import Flask
import requests
import json
from io import BytesIO
from flask import render_template
import csv

app = Flask(__name__, template_folder='template')

# To display the fetched data
@app.route('/', methods=['GET'])
def get_data():
    data = requests.get('https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog').content
    return render_template('display_info.html',data = json.loads(data))

#route to import json data to csv
@app.route('/convertCSV')
def response_to_csv():
    data = requests.get('https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog').content
    data = json.loads(data)
    f = csv.writer(open("output.csv", "w+"))
    f.writerow(["id", "description", "date", "action", "user id", "criticality"])
    for x in data:
        f.writerow([x["id"],
                    x["description"],
                    x["date"],
                    x["action"],
                    x["user_id"],
                    x["criticality"]])
    return "File created as output.csv File name"

if __name__ == '__main__':

    app.run(debug=True)
