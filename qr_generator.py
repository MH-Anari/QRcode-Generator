from flask import Flask, request, render_template
import qrcode
import os

os.system('clear || cls')
app = Flask(__name__)

def make_qrcode(data):
    qr = qrcode.QRCode (
        border=2,
        box_size=10
    )
    qr.add_data(data)
    img = qr.make_image()
    img.save('./static/qrcode.jpg')

# route directory
@app.route('/', methods=['POST', 'GET'])
def index():

    # delete old qrcode
    if os.path.exists('./static/qrcode.jpg'):
        os.remove('./static/qrcode.jpg')

    # get data from html form
    if request.method == 'POST':
        _data_ = request.form.get('data')
        make_qrcode(_data_)

    return render_template('index.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 8080)