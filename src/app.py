import os
from config import app
from src.model import Todo


@app.route("/")
def index():
    return "<p>Index route!</p>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host="0.0.0.0", port=port)
