import io
import base64
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مولد رموز QR السريع</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <script>
        document.addEventListener('click', function() {
            if (!window.adOpened) {
                window.open("https://www.highrevenuegate.com/your_smartlink_here", "_blank");
                window.adOpened = true;
            }
        });
    </script>
    <style>
        body { background-color: #1a1a1a; color: #ffffff; font-family: sans-serif; text-align: center; padding-top: 50px; }
        .card-custom { background-color: #2d2d2d; border-radius: 15px; padding: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 500px; margin: 0 auto; }
        .btn-terabox { background-color: #00b4d8; color: white; font-weight: bold; width: 100%; margin-top: 15px; }
        .btn-terabox:hover { background-color: #0077b6; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card-custom">
            <h2 class="mb-4">⚡️ مولد الـ QR Code الدائم ⚡️</h2>
            <p class="text-muted">أدخل الرابط أو النص في الأسفل لتوليد الرمز فوراً</p>
            <form method="POST">
                <input type="text" name="data_input" class="form-control mb-3 text-center" placeholder="انسخ الرابط هنا..." required>
                <button type="submit" class="btn btn-success w-100 font-weight-bold">توليد الرمز الآن</button>
            </form>
            {% if qr_data %}
                <div class="mt-4">
                    <h5>الرمز الخاص بك جاهز:</h5>
                    <img src="data:image/png;base64,{{ qr_data }}" class="img-fluid my-3" style="max-width: 200px; border: 5px solid white; border-radius: 10px;">
                    <br>
                    <a href="https://www.terabox.com/your_link_here" target="_blank" class="btn btn-terabox">
                        📥 اضغط هنا لحفظ الرمز بجودة عالية عبر TeraBox
                    </a>
                </div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    qr_data = None
    if request.method == "POST":
        import qrcode
        input_text = request.form.get("data_input")
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(input_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        qr_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    return render_template_string(HTML_TEMPLATE, qr_data=qr_data)

if __name__ == "__main__":
    app.run(debug=True)
