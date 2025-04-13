from flask import Flask, render_template, request, jsonify
import predict

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data, make prediction
        try:
            data = request.get_json()
            size = float(data['size'])
            year = int(data['year'])
            view = (data['view'])

            #print(request.form)

            prediction = predict.predict_price(size=size, year=year, view=view)
            return jsonify({"prediction": prediction})

        except Exception as e:
            return jsonify({'error': str(e)}), 500
            return render_template("index.html", prediction=predicted_value)

    # If method is GET
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)