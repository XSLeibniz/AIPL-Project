from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    # 接收前端传来的图像数据
    image_data = request.json['image_data']

    # 在这里编写对图像数据进行处理的代码
    # 这里只是一个示例，您需要根据实际情况来编写
    # 这里可以使用OpenCV等库来处理图像数据

    # 返回处理后的结果给前端
    return jsonify({'message': '图像数据已收到并处理完成'})


if __name__ == '__main__':
    app.run(debug=True)






