# Comic Chatbot with Flask and Stable Diffusion

## Installation and Usage

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install flask pillow flask-sqlalchemy transformers diffusers torch
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser to http://127.0.0.1:5000 to interact with the chatbot.

## Docker

1. Build the Docker image:
   ```bash
   docker build -t comic_chatbot .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 comic_chatbot
   ```

3. Open your browser to http://127.0.0.1:5000.

## Notes and Best Practices

- Customize and fine-tune the Stable Diffusion model for more consistent styles.
- Adjust font paths and text positioning as needed.
- Add more robust error handling and security measures for production environments.
