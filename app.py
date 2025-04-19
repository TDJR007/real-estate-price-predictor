from flask import Flask, render_template, request, jsonify
import predict
import os

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            data = request.get_json()
            size = float(data['size'])
            year = int(data['year'])
            view = data['view']

            prediction = predict.predict_price(size=size, year=year, view=view)
            return jsonify({"prediction": prediction})

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
