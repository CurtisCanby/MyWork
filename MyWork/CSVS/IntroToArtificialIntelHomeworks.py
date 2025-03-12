import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

# Load the dataset
movies = pd.read_csv("C:/Users/16812/OneDrive/Documents/Python/MyWork-1/MyWork/CSVS/movies.csv")
ratings = pd.read_csv("C:/Users/16812/OneDrive/Documents/Python/MyWork-1/MyWork/CSVS/ratings.csv")

# Merge datasets
data = pd.merge(ratings, movies, on='id')

# Create a pivot table
user_movie_matrix = data.pivot_table(index='user', columns='title', values='rating')

# Fill NaN values with 0
user_movie_matrix.fillna(0, inplace=True)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

def get_recommendations(user_id, num_recommendations=5):
    # Get the user's ratings
    user_ratings = user_movie_matrix.loc[user_id]
    
    # Compute the weighted sum of ratings from similar users
    similar_users = user_similarity_df[user_id]
    weighted_ratings = user_movie_matrix.T.dot(similar_users) / similar_users.sum()
    
    # Filter out movies the user has already rated
    recommendations = weighted_ratings[user_ratings == 0].sort_values(ascending=False)
    
    return recommendations.head(num_recommendations)

# Example usage
print(get_recommendations(user_id=1, num_recommendations=5))

# Split data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2)

# Create a function to calculate RMSE
def rmse(predictions, targets):
    return np.sqrt(mean_squared_error(predictions, targets))

# Example evaluation
test_user_movie_matrix = test_data.pivot_table(index='user', columns='title', values='rating')
test_user_movie_matrix.fillna(0, inplace=True)

predictions = []
targets = []

for user_id in test_user_movie_matrix.index:
    user_recommendations = get_recommendations(user_id, num_recommendations=len(test_user_movie_matrix.columns))
    predictions.extend(user_recommendations.values)
    targets.extend(test_user_movie_matrix.loc[user_id].values)

print(f'RMSE: {rmse(predictions, targets)}')
