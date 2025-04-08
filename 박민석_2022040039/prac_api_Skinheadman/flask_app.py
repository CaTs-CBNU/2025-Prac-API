from flask import Flask, jsonify
import csv
from flask import request

app = Flask(__name__)



sex = {
    "M" : "남",
    "F" : "여",
    "A" : "세대수"
}

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

# CSV ?��?��?�� ?��?��??? JSON?���? �??��
def read_csv(code_request,sex_request):
    data = []
    count=0
    with open("prac_api_Skinheadman\cb_statistics_populations.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["시군"] == code[code_request]:
                if sex_request == "A" :
                    data.append(row)
                count += int(row[sex[sex_request]])
        if sex_request == 'M' :
            count_dic = {
                "시군" : code[code_request],
                "남성 인구수" : count
            }
            data.append(count_dic)
        elif sex_request == 'F' :
            count_dic = {
                "시군" : code[code_request],
                "여성 인구수" : count
            }
            data.append(count_dic)
    return data

#/cb?code=<CS_>&sex=<M or F>로 동작
@app.route("/cb", methods=["GET"])
def get_sex():
    code_request = request.args.get("code","CS1")
    sex_request = request.args.get("sex","A")
    codes = read_csv(code_request,sex_request)
    return jsonify(codes)

if __name__ == "__main__":
    app.run(debug=True)