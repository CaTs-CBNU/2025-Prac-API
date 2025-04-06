from flask import Flask, jsonify
import csv
from flask import request

app = Flask(__name__)

code = {
    "CS1" : "청주시 상당구",
    "CS2" : "청주시 서원구",
    "CS3" : "청주시 흥덕구",
    "CS4" : "청주시 청원구",
    "CS5" : "충주시",
    "CS6" : "제천시",
    "CS7" : "보은군",   
    "CS8" : "옥천군",
    "CS9" : "영동군",
    "CS10" : "증평군",
    "CS11" : "진천군",
    "CS12" : "괴산군",
    "CS13" : "음성군",
    "CS14" : "단양군"
    
}

sex = {
    "M":"남",
    "F":"여"
}

# CSV 파일을 읽어와 JSON으로 변환
def read_csv(c,s):
    data = []
    sum = 0
    with open("2025-Prac-API-main\prac_api\cb_statistics_populations.csv", "r", encoding="EUC-KR") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if code[c] == row["시군"]:
                #data.append(row)
                sum += (int)(row[sex[s]])
    ret = {
        "count" : sum
    }
    data.append(ret)
    
    return data

@app.route("/cb", methods=["GET"])
def get_stores():
    cd = request.args.get("code","CS1")
    s = request.args.get("sex","M")
    stores = read_csv(cd,s)
    print(cd)
    return jsonify(stores)

@app.route("/stores", methods=["GET"])
def get_store():
    print("efg")
    stores = read_csv()
    return jsonify(stores)



if __name__ == "__main__":
    app.run(debug=True)