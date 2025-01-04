from flask import Flask, request, jsonify
from meta_ai_api import MetaAI
import time

app = Flask(__name__)
ai = MetaAI()

@app.route('/search', methods=['GET'])
def search_query():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing 'q' parameter"}), 400
    
    for attempt in range(3):
        try:
            response = ai.prompt(message=query)
            return jsonify({"response": response}), 200
        except Exception as e:
            if attempt < 2:  # Retry for the first 2 attempts
                time.sleep(1)  # Wait before retrying
            else:
                return jsonify({"error": "Unable to get a response", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
