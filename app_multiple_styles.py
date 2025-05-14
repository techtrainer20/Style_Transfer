import os
from flask import Flask, render_template, request, redirect, send_file
from PIL import Image
import torch
from torchvision import transforms
import torchvision.transforms.functional as TF
from model import TransformerNet

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_IMAGE'] = 'static/output.jpg'

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model(model_filename):
    model_path = os.path.join("saved_models", model_filename)
    model = TransformerNet()
    state_dict = torch.load(model_path, map_location=device)
    filtered_state_dict = {k: v for k, v in state_dict.items() if "running_mean" not in k and "running_var" not in k}
    model.load_state_dict(filtered_state_dict)
    model.to(device).eval()
    return model

def image_loader(image_path, max_size=512):
    image = Image.open(image_path).convert("RGB")
    size = max(image.size)
    if size > max_size:
        size = max_size
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    image = transform(image).unsqueeze(0)
    return image.to(device)

def save_image(tensor, path):
    image = tensor.clone().detach().cpu().squeeze(0)
    image = image / 255
    image = TF.to_pil_image(image.clamp(0, 1))
    image.save(path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['content_image']
        style_name = request.form.get('style_model', 'candy.pth')

        if file and style_name:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)

            model = load_model(style_name)

            content = image_loader(path)
            with torch.no_grad():
                output = model(content).cpu()
            save_image(output, app.config['OUTPUT_IMAGE'])
            return redirect('/')
    return render_template('index.html', output_path=app.config['OUTPUT_IMAGE'])

@app.route('/download')
def download():
    return send_file(app.config['OUTPUT_IMAGE'], as_attachment=True)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)