from flask import Flask, jsonify, request

app = Flask(__name__)

rates = {"USD":1, "EUR":0.92, "ILS":3.7, "GPT":0.8}

@app.route('/health', methods=["GET"])
def health():
    return jsonify({"status": "OK"})

def convert_currency(amount, src_currency, dist_currency):
    return (amount / rates[src_currency]) * rates[dist_currency]

@app.route('/convert', methods=["POST"])
def convert():
    data = request.get_json()
    amount = data.get("amount")
    src_currency = data.get("from")
    dist_currency = data.get("to")

    converted = convert_currency(amount, src_currency, dist_currency)

    return jsonify({"converted": converted})


    
if __name__ == "__main__":
    app.run(port = 8080)




