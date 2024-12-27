from flask import Blueprint, request, jsonify
from download_google_reviews import GetGoogleReviews
from agent import ReviewAnalysisAgent


# Create a Blueprint for routes
g_insights = Blueprint('g_insights', __name__)


@g_insights.route('/analyze', methods=['POST'])
def get_reviews():
    if request.is_json:

        data = request.get_json()
        try:
            GetGoogleReviews(data['url'])

        except Exception as e:
            print(e)     

        return jsonify({"message": "URL analyzed successfully", "data": data}), 200
    else:
        return jsonify({"error": "Invalid JSON format"}), 400

# Route: Get all todos
@g_insights.route('/reviews-insights', methods=['POST'])
def get_llm_answer():
    agent = ReviewAnalysisAgent(llm_model = "gpt-4o-mini",
                             emedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    if request.is_json:
        data = request.get_json()

        try:
            print(data['question'])
            answer=agent.get_answer(data['question'])
            return jsonify({"message": "Answer generated successfully", "data": answer}), 200
        
        except Exception as e:
            print(e)
        return jsonify({"message": "Answer cannot be successfully generated", "data": data}), 200

    return 
