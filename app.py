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
    
    <title>⚡️ مولد الـ QR Code السريع مجاناً - تحويل الروابط إلى باركود</title>
    <meta name="description" content="أفضل موقع مجاني وسريع لتوليد رموز QR Code أونلاين. قم بتحويل الروابط، النصوص، وحسابات التواصل الاجتماعي إلى باركود جاهز للتحميل بضغطة زر واحدة.">
    <meta name="keywords" content="كيو ار كود, qr code, مولد qr code, صنع باركود, تحويل الرابط الى باركود, qr code generator, صنع qr code مجانا">
    
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
        body { background-color: #1a1a1a; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding-top: 50px; }
        .card-custom { background-color: #2d2d2d; border-radius: 15px; padding: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); max-width: 500px; margin: 0 auto; }
        .btn-telegram { background-color: #0088cc; color: white; font-weight: bold; width: 100%; margin-top: 15px; border-radius: 10px; padding: 12px; text-decoration: none; display: inline-block; }
        .btn-telegram:hover { background-color: #006699; color: white; }
        .seo-section { max-width: 600px; margin: 50px auto; text-align: right; padding: 20px; line-height: 1.8; color: #b3b3b3; }
        .seo-section h3 { color: #28a745; margin-bottom: 15px; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card-custom">
            <h1 class="h3 mb-4">⚡️ مولد الـ QR Code السريع ⚡️</h1>
            <p class="text-muted">أدخل الرابط أو النص في الأسفل لتوليد الرمز فوراً مجاناً</p>
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

        <div class="seo-section">
            <h3>ما هو الـ QR Code وكيف يمكنك الاستفادة منه؟</h3>
            <p>رمز الاستجابة السريعة أو ما يُعرف بـ <strong>QR Code</strong> هو عبارة عن مصفوفة ثنائية الأبعاد تُستخدم لتخزين البيانات والروابط بشكل مشفر وسريع. من خلال موقعنا، يمكنك تحويل أي رابط إلكتروني، نص، حساب تيك توك، انستقرام، أو حتى شبكة واي فاي إلى رمز باركود مخصص مجاناً 100% وبدون أي حدود.</p>
            
            <h4 class="text-white mt-4 mb-2 h5">💡 خطوات صنع باركود مخصص لروابطك:</h4>
            <ul>
                <li>قم بنسخ الرابط الذي تريد تحويله (رابط موقع، فيديو، أو حساب).</li>
                <li>الصق الرابط داخل مربع الإدخال في الأعلى بدقة.</li>
                <li>اضغط على زر <strong>"توليد الرمز الآن"</strong> ليقوم النظام البرمجي بإنشاء الكود فوراً.</li>
                <li>إذا كنت تستخدم الهاتف أو الآيباد، اضغط مطولاً على الصورة لحفظها مباشرة في معرض الصور.</li>
            </ul>
            
            <p class="mt-3 small text-center text-muted">جميع الحقوق محفوظة لموقع توليد رموز كيو ار السريع © 2026</p>
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
