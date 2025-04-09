from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)

city_code = {
    "CS1": "청주시 상당구",
    "CS2": "청주시 서원구",
    "CS3": "청주시 흥덕구",
    "CS4": "청주시 청원구",
    "CS5": "충주시",
    "CS6": "제천시",
    "CS7": "보은군",
    "CS8": "옥천군",
    "CS9": "영동군",
    "CS10": "증평군",
    "CS11": "진천군",
    "CS12": "괴산군",
    "CS13": "음성군",
    "CS14": "단양군"
}

sex_code = {
    "M": "남",
    "F": "여"
}

def read_csv(C, S):
    p = 0
    region = city_code[C]
    gender = sex_code[S]

    file_path = os.path.join(os.path.dirname(__file__), "cb_statistics_populations.csv")

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if region in row["시군"]:
                p += int(row[gender].replace(",", ""))

    return {"count": p}

@app.route("/cb", methods=["GET"])
def get_mains():
    city = request.args.get("code")
    sex = request.args.get("sex")
    result = read_csv(city, sex)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
