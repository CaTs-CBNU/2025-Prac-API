from flask import Flask, jsonify, render_template, request
import csv

app = Flask(__name__)
group_code_mapping = {
    "청주시 상당구":"CS1",
    "청주시 서원구":"CS2",
    "청주시 흥덕구":"CS3",
    "청주시 청원구":"CS4"
    #...이하 생략
}

# CSV 파일을 읽어와 JSON으로 변환
def read_csv(code, sex):
    total = 0
    with open("C:/API_tutorial/2025-Prac-API/prac_api/cb_statistics_populations.csv", "r", encoding="cp949") as f:
        reader = csv.DictReader(f)
        for row in reader:
            si_gun = row["시군"].strip()
            if group_code_mapping.get(si_gun) == code:
                if sex == "M":
                    value = row["남"]
                elif sex == "F":
                    value = row["여"]
                total += int(value) 
    return total


# @app.route("/", methods=["GET"])
# def get_dk():
#     stores = {"허거동균" : 20210400034, "학년": 3}
#     return render_template('C:\API_tutorial\2025-Prac-API\prac_api\index.html')


@app.route("/cb", methods=["GET"])
def get_grpsx():
    code = request.args.get("code")
    sex = request.args.get("sex")
    total = read_csv(code, sex)
    return jsonify({"count": total})


if __name__ == "__main__":
    app.run(debug=True)