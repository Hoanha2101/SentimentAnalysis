from flask import Flask, render_template, request, jsonify
import csv
import time
import json
from MyFile.predict import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/PREDICT', methods=['POST'])
def PREDICT():
    try:
        data = request.get_json()
        user_input = data['text']
        
        sentiment = infer(user_input)

        with open('data.csv', 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader_ = csv.reader(csvfile)
            history = list(csv_reader_)
            
        if len(history) == 0:
            with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, sentiment])
        else: 
            with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, sentiment])
            
        # Chuẩn bị phản hồi
        response_data = {"input": user_input,
                        "sentiment": sentiment}

        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/stream')
def stream():
    def generate():
        while True:
            # Đọc dữ liệu từ file CSV
            with open('data.csv', 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                history = list(csv_reader)
            history_json = json.dumps(history)
            # Gửi dữ liệu dưới dạng sự kiện SSE
            yield f"data: {history_json}\n\n"
            time.sleep(1)  # Đợi 1 giây trước khi gửi dữ liệu mới

    return app.response_class(generate(), content_type='text/event-stream')

@app.route('/getChartData')
def get_chart_data():
    with open('data.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        history = list(csv_reader)
        
    data = []
    for i in history:
        if len(i) != 0:
            data.append(i[1])
            
    return jsonify(data)

if __name__ == '__main__':
    
    app.run(debug=True)
