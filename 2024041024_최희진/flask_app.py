from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

# CSV 파일을 읽어 JSON으로 변환
def read_csv():
    data = []
    with open("C:/Users/User/Desktop/2025-Prac-API/prac_api/stores.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

GROUP_loc = {
    "CS1": "청주시 상당구",
    "CS2": "청주시 서원구"
}

GROUP_sex = {
    "M": "남",
    "W": "여"
}

def read1_csv():
    data = []
    with open("C:/Users/User/Desktop/2025-Prac-API/prac_api/cb_statistics_populations.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


@app.route("/cb", methods=["GET", "POST"])
def get_population():
    # 쿼리 파라미터 받기
    code = request.args.get("code")  # CS1 또는 CS2
    sex = request.args.get("sex")    # M 또는 W

    # 매핑된 한글 지역명과 성별 찾기
    loc_name = GROUP_loc[code]  # 청주시 상당구 or 청주시 서원구
    sex_name = GROUP_sex[sex]   # 남 or 여

    # CSV 데이터 불러오기
    data = read1_csv()

    # 해당 지역 데이터 필터링
    filtered_data = [row for row in data if row["시군"] == loc_name]

    # 성별에 따라 숫자 값만 추출
    total_population = sum(int(row[sex_name]) for row in filtered_data)

    return jsonify({
        "지역": loc_name,
        "성별": sex_name,
        "총 인구수": total_population
    })

if __name__ == "__main__":
    app.run(debug=True)
