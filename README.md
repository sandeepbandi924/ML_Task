# MACHINE LEARNING TASK 

### Project Summary
The objective of this project was to develop a personalized feed algorithm for a social media application. The algorithm ranks posts based on user interactions and preferences, using a machine learning approach. The project was broken down into several key stages: data collection and preprocessing, feature engineering, model development, implementation, testing and validation, and documentation and reporting.

### Steps Taken

#### 1. Data Collection and Preprocessing
- **Synthetic Data Generation**: We generated a synthetic dataset to simulate real-world user interactions with posts. This involved creating 1000 users and 10,000 posts, along with random interactions such as likes, comments, shares, and views. Each interaction was timestamped to add a temporal component to the data.
- **Data Integration**: Interaction data was merged with post data to form a comprehensive dataset that could be used for feature engineering and model training.
### 2. Exploratory Data Analysis (EDA)
- **Objective**: To understand the distribution and relationships within the dataset, and to identify any potential issues or insights.
  - **Data Visualization**: Plotted distributions of interaction types, post activities over time, and user activity levels using histograms and bar plots.
  - **Correlation Analysis**: Examined correlations between different interaction types to understand their relationships.
  - **Content Analysis**: Investigated the distribution of post lengths and common words in post content.
#### 3. Feature Engineering
- **Interaction Features**: We extracted features that quantify user interactions with posts. This included counting the number of likes, comments, shares, and views each post received from each user.
- **Content Features**: Text features were extracted from the post content using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. This allowed us to capture important information about the content of each post.
- **Temporal Features**: We calculated the recency of each post by determining the age of the post in days from the current date. This feature helps in understanding the temporal relevance of posts to users.

#### 4. Model Development
- **Algorithm Selection**: We chose Logistic Regression as our machine learning model due to its simplicity and effectiveness for binary classification tasks.
- **Training the Model**: The dataset was split into training and testing sets. The Logistic Regression model was trained on the training data, learning to predict the relevance of posts to users based on the engineered features.
- **Evaluation Metrics**: The model's performance was evaluated using accuracy, precision, and recall metrics. These metrics provided insights into how well the model could distinguish between relevant and non-relevant posts.

#### 5. Implementation
- **Feed Generation**: We implemented a function to generate a ranked list of posts for a user based on the model’s predictions. The function takes a user ID as input and outputs posts sorted by their predicted relevance scores.

#### 6. Testing and Validation
- **Cross-Validation**: GridSearchCV with Stratified K-fold Cross Validation was applied to validate the model's performance. This technique helps in ensuring that the model is robust and performs well on unseen data.
- **Evaluation**: The cross-validation results were analyzed to confirm the reliability of the model's performance metrics, ensuring that the model generalizes well to new data.
#### 7. API Development and Integration
- **API Creation**: Developed a sample RESTful API using Flask to expose the personalized feed functionality. The API allows external applications to request personalized feeds for a given user.

- **Postman Integration**: Used Postman to test the POST request to the API. The request was structured to send a JSON payload with the user ID and post features, and the response was checked for correctness.

    - POST Request URL: http://localhost:5000/generate_feed
    - Request Body (JSON format):
### Results
- **Model Performance**: The Logistic Regression model demonstrated satisfactory accuracy, precision, and recall in predicting the relevance of posts to users. This indicates that the model can effectively distinguish between relevant and non-relevant posts based on user interactions and post features.
- **Feed Generation**: The feed generation function successfully produced personalized feeds for users. Posts were ranked based on predicted relevance scores, and sample outputs showed that the function could generate meaningful and personalized post rankings.

### Insights and Future Work
- **Scalability**: While the current implementation works well for a small synthetic dataset, scaling this approach to handle larger datasets and more complex models would involve optimizing data storage and processing, possibly using distributed computing frameworks.
- **Advanced Models**: Future iterations of the project could explore more advanced machine learning models, such as neural networks or ensemble methods, to potentially improve prediction accuracy.
- **Real-World Data**: Applying the algorithm to real-world data would provide further insights into its effectiveness and allow for fine-tuning based on actual user behavior.

### Conclusion
This project successfully demonstrated the development and implementation of a personalized feed algorithm for a social media application. By following a structured approach that included data collection, feature engineering, model training, and validation, we were able to create a functional and effective algorithm. The project highlights the potential of machine learning to enhance user experiences by providing personalized content recommendations.
