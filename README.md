# END TO END MACHINE LEARNING PROJECT TASK

### Technical Documentation

#### Data Collection and Preprocessing

- **Synthetic Data Generation**: Created a synthetic dataset with user interactions, post content, and timestamps.
- **Data Preprocessing**: Merged interaction and post data, handled missing values, and created necessary features.

#### Feature Engineering

- **Interaction Features**: Counted the number of likes, comments, and shares a post received.
- **Content Features**: Extracted TF-IDF features from the post content.
- **Temporal Features**: Included the recency of the post as a feature.

#### Model Development

- **Algorithm Selection**: Chose logistic regression for its simplicity and efficiency.
- **Model Training**: Trained the model using the synthetic dataset and evaluated it using accuracy, precision, and recall metrics.

#### Implementation

- **Feed Generation**: Implemented a function to generate a ranked list of posts for a user based on predicted interaction probabilities.
- **Scalability Considerations**: Discussed potential scaling issues and suggested using more complex models and distributed computing for larger datasets.

#### Testing and Validation

- **Cross-Validation**: Performed k-fold cross-validation to validate the model's performance.
- **Evaluation**: Provided a brief analysis of the model's performance based on evaluation metrics.

### Instructions for Running the Code

1. Set up the Python environment with the required libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `nltk`, `wordcloud`.
2. Run the Jupyter Notebook or Python script to generate the synthetic dataset, preprocess the data, perform EDA, feature engineering, train the model, and generate the personalized feed.
3. Follow the steps in the code to evaluate the model's performance and visualize the results.
