from flask import Flask, render_template, request, make_response
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/qr-code', methods=['GET'])
def generate_qr_code():
    url = request.args.get('url')
    color = request.args.get('color') or 'black'

    if not url:
        return 'URL is required', 400

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        response = make_response(buffer.getvalue())
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='qrcode.png')
        return response
    except Exception as e:
        return f'Error: {str(e)}', 400

if __name__ == "__main__":
    app.run()
