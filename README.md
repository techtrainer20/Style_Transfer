# 🎨 Neural Style Transfer Web App

Transform your photos into artwork using deep learning and pre-trained models like `oil painting`,`candy`, `udnie`, `rain_princess`, and more — all powered by PyTorch and Flask with a beautiful user interface.

## 🚀 Features

- Upload your own image and apply different artistic styles
- Choose from multiple `.pth` style models
- RGB glowing buttons and smooth animations
- Sparkle + buffer effect during image processing
- Clean, mobile-friendly design
- Download your stylized image instantly

## 📁 Project Structure

```
neural-style-transfer-app/
├── app.py                  # Flask backend logic
├── model.py                # TransformerNet model definition
├── templates/
│   └── index.html          # Frontend HTML page
├── static/
│   ├── style.css           # (Optional) Additional CSS
│   └── logo.png            # App branding logo
├── saved_models/
│   ├── candy.pth
│   ├── oil_painting.pth
│   ├── rain_princess.pth
│   └── udnie.pth
└── requirements.txt        # Required Python packages
```

## 🧠 Supported Style Models (`.pth`)

- `candy.pth`
- `oil_painting.pth`
- `rain_princess.pth`
- `udnie.pth`

You can download more `.pth` models from:
- https://github.com/gnsmrky/pytorch-fast-neural-style-for-web
- https://github.com/pytorch/examples/tree/main/fast_neural_style

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/neural-style-transfer-app.git
cd neural-style-transfer-app
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 🖼️ How it works

- Upload a content image.
- Select a style model.
- Click "✨ Stylize Image" — the image is sent to the backend.
- The selected model applies style transfer using `TransformerNet`.
- The stylized output is shown with the option to download.

## 📦 Dependencies

- Flask
- Torch
- torchvision
- Pillow

Install via:

```bash
pip install -r requirements.txt
```

## 📄 License

MIT License © 2025 Vignesh M
