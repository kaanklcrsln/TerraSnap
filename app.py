
import base64, io, os
from flask import Flask, request, jsonify, render_template, send_from_directory
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')

# Google AI API'yi yapılandır
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"API anahtarı yapılandırma hatası: {e}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze_image():
    try:
        data = request.json
        if 'image' not in data:
            return jsonify({'error': 'Resim verisi bulunamadı.'}), 400

        image_data = data['image']
        image_data = image_data.split(',')[-1]  # base64 kısmını ayıkla
        image_bytes = base64.b64decode(image_data)
        
        image = Image.open(io.BytesIO(image_bytes))

        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Bu resimdeki manzarayı veya nesneyi açıkla.", image], stream=True)
        response.resolve()

        analysis = response.text

        return jsonify({'summary': analysis})

    except Exception as e:
        print(f"Hata oluştu: {e}")
        # Fallback to another model if the first one fails
        try:
            model = genai.GenerativeModel('gemini-pro-latest')
            response = model.generate_content(["Bu resimdeki manzarayı veya nesneyi açıkla.", image], stream=True)
            response.resolve()

            analysis = response.text
            return jsonify({'summary': analysis})
        except Exception as e2:
            print(f"Fallback model hatası: {e2}")
            return jsonify({'error': f'Sunucu hatası: {str(e2)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
