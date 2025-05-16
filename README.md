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
├── app_multiple_styles.py                  # Flask backend logic
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
Windows: venv\Scripts\activate # Linux source venv/bin/activate 
pip install -r requirements.txt
```

3. Run the app:

```bash
python app_multiple_styles.py
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
## Screenshots
![image](https://github.com/user-attachments/assets/112126e9-671d-4088-a5af-252a67f00a2a)***![image](https://github.com/user-attachments/assets/c0823029-b9cc-4c2a-a9f9-b0115d5bd2a2)***![image](https://github.com/user-attachments/assets/28a32759-415a-44f0-a9bb-4c5b3d23fef2)***


## 📄 License

MIT License © 2025 Vignesh M
