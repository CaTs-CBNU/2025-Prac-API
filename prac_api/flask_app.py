from flask import Flask, jsonify
import csv

app = Flask(__name__)

# CSV 파일을 읽어와 JSON으로 변환
def read_csv():
    data = []
    with open("stores.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

@app.route("/stores", methods=["GET"])
def get_stores():
    stores = read_csv()
    return jsonify(stores)

if __name__ == "__main__":
    app.run(debug=True)