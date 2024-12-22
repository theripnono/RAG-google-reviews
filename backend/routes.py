from flask import Blueprint, request, jsonify
from download_google_reviews import GetGoogleReviews

# Create a Blueprint for routes
g_insights = Blueprint('g_insights', __name__)

# Route: Create a new todo
@g_insights.route('/analyze', methods=['POST'])
def get_reviews():
    if request.is_json:

        data = request.get_json()

        URL="https://www.google.com/maps/place/El+Curry+Verde/@43.3769804,-1.8015808,17z/data=!3m1!4b1!4m6!3m5!1s0xd5109081bb759a1:0xc866b9f78bb1dc19!8m2!3d43.3769766!4d-1.7967152!16s%2Fg%2F1hc7nn793?entry=ttu"

        #GetGoogleReviews(URL)
        
        print(data)
        
        return jsonify({"message": "URL analyzed successfully", "data": data}), 200
    else:
        return jsonify({"error": "Invalid JSON format"}), 400

# Route: Get all todos
@g_insights.route('/answer', methods=['GET'])
def get_llm_answers():

    return 
