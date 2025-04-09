from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

GROUP_CODE = {
    "CS1":"청주시 상당구",
    "CS2":"청주시 서원구",
    "CS3":"청주시 흥덕구",
    "CS4":"청주시 청원구",
    "CS5":"충주시",
    "CS6":"제천시",
    "CS7":"보은군",
    "CS8":"옥천군",
    "CS9":"영동군",
    "CS10":"증평군",
    "CS11":"진천군",
    "CS12":"괴산군",
    "CS13":"음성군",
    "CS14":"단양군"
}

@app.route("/cb", methods=["GET"])
def get_pop_sum():
    code = request.args.get('code')
    sex = request.args.get('sex')

    region=GROUP_CODE[code]

    gender=None
    if sex == "M":
        gender="남"
    elif sex == "F":
        gender = "여"

    total=0
    with open("cb_statistics_populations.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if region in row["시군"]:
                    total+=int(row[gender].replace(",",""))

    return jsonify({"count":total})



if __name__ == "__main__":
    app.run(debug=True)