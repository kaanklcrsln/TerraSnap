# 🛰️ TerraSnap - Satellite Image Analysis Bot

A modern web application that analyzes satellite imagery using AI-powered image captioning to identify and describe land features such as terrain types, water bodies, vegetation, and human structures.

## 📋 Features

- **Satellite Image Upload**: Support for PNG, JPEG, and WebP formats
- **AI-Powered Analysis**: Uses Hugging Face's free image captioning model to analyze satellite imagery
- **Real-time Preview**: Instant image preview when selecting satellite images
- **Responsive UI**: Modern, minimalist black and white interface with smooth animations
- **No API Keys Required**: Uses free, public AI models - no authentication needed
- **Fast Processing**: Quick analysis with loading indicators

## 🎨 Design

- **Color Scheme**: Minimalist black (#000000) and white (#FFFFFF) theme
- **Typography**: Ubuntu, Inter, and Space Grotesk fonts
- **Layout**: 50/50 split interface (upload panel on left, results panel on right)
- **Sharp UI Elements**: All elements feature sharp corners (no rounded borders) for a modern look

## 🛠️ Technologies

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Model**: Hugging Face Vision-GPT2 Image Captioning
- **Image Processing**: Pillow (PIL)
- **HTTP Requests**: Requests library

## 📦 Requirements

```bash
Flask
Requests
Pillow
```

## 🚀 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/kaanklcrsln/terrasnap.github.io.git
cd terrasnap
```

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the application**:
```bash
python app.py
```

5. **Open in browser**:
```
http://127.0.0.1:5000/
```

## 📝 How to Use

1. Click the **"Select Image"** button to upload a satellite image
2. Preview the image in the left panel
3. Click the **"Analyze"** button to start analysis
4. Wait for the AI model to process the image
5. View detailed land feature descriptions in the right panel

## 🌍 Supported Image Types

- PNG (Portable Network Graphics)
- JPEG (Joint Photographic Experts Group)
- WebP (Modern web image format)

## 🧠 AI Model Details

- **Model**: `nlpconnect/vit-gpt2-image-captioning`
- **Provider**: Hugging Face
- **Type**: Vision-Language Model
- **Cost**: FREE (no API key required)
- **Processing**: ~3-5 seconds per image

## 📂 Project Structure

```
terrasnap/
├── app.py                 # Flask backend application
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Main stylesheet
├── templates/
│   └── index.html        # Frontend HTML
└── .env                  # Environment variables (not tracked)
```

## 🔒 Security

- `.env` file is protected by `.gitignore`
- Sensitive data (API keys, credentials) should be stored in `.env`
- Flask runs in debug mode - switch to production mode for deployment

## 🌟 Features Coming Soon

- Chat functionality to ask follow-up questions about analysis
- Multi-image batch processing
- Analysis history and saved results
- Export results as PDF/CSV
- Advanced filtering options

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## 📄 License

MIT License - feel free to use this project for personal and commercial purposes.

## 👨‍💻 Author

**Kaan Kilic** - [GitHub](https://github.com/kaanklcrsln)

## 🐛 Troubleshooting

**Issue**: "Modelden geçerli JSON yanıt alınamadı"
- **Solution**: The Hugging Face API might be rate-limited or under heavy load. Wait a moment and try again.

**Issue**: Font not loading
- **Solution**: Check your internet connection. Google Fonts requires an active internet connection.

**Issue**: Image preview not showing
- **Solution**: Make sure you're uploading a supported image format (PNG, JPEG, WebP).

## 📧 Contact

For questions or issues, please create an issue on GitHub.

---

**Happy analyzing! 🚀**
