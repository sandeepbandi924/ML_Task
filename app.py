from flask import Flask, request, jsonify,render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_feed', methods=['POST'])
def generate_feed_api():
    user_id = request.json['user_id']
    loaded_model = joblib.load('logistic_regression.joblib')
    loaded_features_df = joblib.load('features_df.joblib')
    sample_feed = generate_feed(user_id, loaded_model, loaded_features_df)
    return jsonify(sample_feed.to_dict('records'))


def generate_feed(user_id, model, features_df):
    user_posts = features_df[features_df['User_ID'] == user_id].copy()
    user_X = user_posts.drop(['User_ID', 'Post_ID', 'Relevant'], axis=1)
    user_posts['Relevance_Score'] = model.predict_proba(user_X)[:, 1]
    return user_posts.sort_values(by='Relevance_Score', ascending=False)


if __name__ == '__main__':
    app.run(debug=True)

    