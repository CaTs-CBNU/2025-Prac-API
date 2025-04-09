from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

def convert_code_to_name(code):
    mapping = {
        "CS1": "청주시 상당구",
        "CS2": "청주시 서원구",
        #나머지 생략
    }
    return mapping.get(code, "")

def read_csv(code, sex):
    total = 0
    target_name = convert_code_to_name(code)

    with open("../cb_statistics_populations.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if target_name in row["시군"]:
                if sex == "M":
                    total += int(row["남"].replace(",", ""))
                elif sex == "F":
                    total += int(row["여"].replace(",", ""))
    return total

@app.route("/cb", methods=["GET"])
def get_population():
    code = request.args.get("code") 
    sex = request.args.get("sex") 
    total = read_csv(code, sex)
    return jsonify({"count": total})

if __name__ == "__main__":
    app.run(debug=True)
