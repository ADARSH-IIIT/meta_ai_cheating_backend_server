from flask import Flask, request, jsonify
from meta_ai_api import MetaAI

app = Flask(__name__)

# Initialize the MetaAI client
ai = MetaAI()

@app.route('/search', methods=['GET'])
def search_query():
    # Extract 'q' from the GET request's query parameters
    query = request.args.get('q')
    
    if not query:
        return jsonify({"error": "Missing 'q' parameter"}), 400
    
    try:
        # Use MetaAI to process the query
        response = ai.prompt(message=query)
        
        # Return the response to the client
        return jsonify({"response": response}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
