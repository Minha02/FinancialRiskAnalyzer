from flask import request, jsonify
from validator import validate_transaction
from llm_integrator import analyse_transaction

def create_transaction():
    try:
        transaction = request.get_json(force=True)
        validate_transaction(transaction)
        # Here, you could add code to save or process the transaction

        #return jsonify({"message": "Transaction validated and processed successfully."}), 201
    
        llm_response = analyse_transaction(transaction)
        return jsonify({
            "message": "Transaction validated and analyzed.",
            "llm_result": llm_response
        }), 201

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 422

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
