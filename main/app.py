from flask import Flask
from controller import create_transaction

app = Flask(__name__)

@app.route("/transaction", methods=["POST"])
def transactions_route():
    return create_transaction()

if __name__ == "__main__":
    app.run(debug=True)
