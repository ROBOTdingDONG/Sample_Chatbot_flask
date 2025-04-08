from flask import Flask, render_template, request, jsonify, url_for
from models import db, ChatHistory
from PIL import Image, ImageDraw, ImageFont
import os
import uuid
import torch
from diffusers import StableDiffusionPipeline

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Load Stable Diffusion model (comic style)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to(device)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    dialogue = request.json.get('dialogue')

    # Enhance prompt to maintain consistent comic style and characters
    comic_prompt = f"comic book style, consistent characters, {prompt}"

    # Generate image
    image = pipe(comic_prompt).images[0]

    # Add dialogue text overlay
    draw = ImageDraw.Draw(image)
    font_path = "arial.ttf"  # Ensure this font file is available or adjust path
    font = ImageFont.truetype(font_path, 24)
    text_position = (20, image.height - 100)  # Adjust positioning as desired
    draw.text(text_position, dialogue, font=font, fill="white")

    # Save image
    filename = f"{uuid.uuid4().hex}.png"
    image_path = os.path.join('static', 'images', filename)
    image.save(image_path)

    # Save to database
    chat_entry = ChatHistory(prompt=prompt, dialogue=dialogue, image_path=image_path)
    db.session.add(chat_entry)
    db.session.commit()

    return jsonify({"image_url": url_for('static', filename=f'images/{filename}')})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
