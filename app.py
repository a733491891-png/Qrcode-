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
        // فتح إعلان الـ Smartlink الخاص بك في الخلفية عند الضغط في أي مكان
        document.addEventListener('click', function() {
            if (!window.adOpened) {
                window.open("https://www.effectivecpmnetwork.com/ini6wd4r?key=2310fbd3cc6aadd5c14f230538009cc1", "_blank");
                window.adOpened = true;
            }
        });
    </script>
    <style>
        body { background-color: #1a1a1a; color: #ffffff; font-family: sans-serif; text-align: center; padding-top: 50px; }
        .card-custom { background-color: #2d2d2d; border-radius: 15px; padding: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 500px; margin: 0 auto; }
        .btn-telegram { background-color: #0088cc; color: white; font-weight: bold; width: 100%; margin-top: 15px; border-radius: 10px; padding: 12px; text-decoration: none; display: inline-block; }
        .btn-telegram:hover { background-color: #006699; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card-custom">
            <h2 class="mb-4">⚡️ مولد الـ QR Code السريع ⚡️</h2>
            <p class="text-muted">أدخل الرابط أو النص في الأسفل لتوليد الرمز فوراً</p>
            <form method="POST">
                <input type="text" name="data_input" class="form-control mb-3 text-center" placeholder="انسخ الرابط هنا..." required>
                <button type="submit" class="btn btn-success w-100 font-weight-bold" style="padding: 12px; border-radius: 10px;">توليد الرمز الآن</button>
            </form>
            
            {% if qr_data %}
                <div class="mt-4">
                    <h5 class="text-success">🎯 الرمز الخاص بك جاهز:</h5>
                    <p class="text-muted small">اضغط مطولاً على الصورة لحفظها في جهازك</p>
                    <img src="data:image/png;base64,{{ qr_data }}" class="img-fluid my-2" style="max-width: 200px; border: 5px solid white; border-radius: 10px;">
                    <br>
                    <a href="https://t.me/seeveenn" target="_blank" class="btn btn-telegram">
                        ✈️ انضم لقناتنا على تليجرام لتحديثات الأدوات والأسرار
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
