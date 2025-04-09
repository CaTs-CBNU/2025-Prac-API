from flask import Flask, jsonify, request
import csv

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False

code = {
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

@app.route("/cb", methods=["GET"])
def population():
    code_param = request.args.get("code")  
    sex_param = request.args.get("sex")    
    sum = 0
    flag = None

    #매핑
    if sex_param == "M":
        flag = "남"
    elif sex_param == "F":
        flag = "여"
    else:
        return jsonify({"error": "잘못된 성별 값입니다. 'M' 또는 'F'만 허용됩니다."}), 400 #

    try:
        # CSV 파일 열기
        with open("C:/Users/xnoa0/Desktop/pracapi/cb_statistics_populations.csv", encoding="UTF-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("시군") == code.get(code_param):
                    try:
                        sum += (int)(row.get(flag, 0))
                    except ValueError:
                        print(f"잘못된 값: {row}")
                        continue
    except FileNotFoundError:
        return jsonify({"error": "CSV 파일을 찾을 수 없습니다."}), 404

    # 결과 반환
    return jsonify({"total": sum})

if __name__ == "__main__":
    app.run(debug=True)