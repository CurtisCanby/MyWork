import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.sparse.linalg import svds

# Load the dataset
movies = pd.read_csv("C:/Users/16812/OneDrive/Documents/Python/MyWork-1/MyWork/CSVS/movies.csv")
ratings = pd.read_csv("C:/Users/16812/OneDrive/Documents/Python/MyWork-1/MyWork/CSVS/ratings.csv")

# Merge datasets
data = pd.merge(ratings, movies, on='id')

# Create a pivot table
user_movie_matrix = data.pivot_table(index='user', columns='title', values='rating')

# Fill NaN values with 0
user_movie_matrix.fillna(0, inplace=True)

# Normalize the user_movie_matrix by subtracting the mean user rating
user_ratings_mean = np.mean(user_movie_matrix, axis=1)
user_movie_matrix_normalized = user_movie_matrix - user_ratings_mean.values.reshape(-1, 1)

# Perform Singular Value Decomposition
user_movie_matrix_normalized = user_movie_matrix_normalized.to_numpy()
U, sigma, Vt = svds(user_movie_matrix_normalized, k=50)

# Convert sigma to a diagonal matrix
sigma = np.diag(sigma)

# Reconstruct the matrix
all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.values.reshape(-1, 1)
predicted_ratings_df = pd.DataFrame(all_user_predicted_ratings, columns=user_movie_matrix.columns)

def get_recommendations(user_id, num_recommendations=5):
    try:
        # Get and sort the user's predicted ratings
        user_row_number = user_id - 1
        sorted_user_predictions = predicted_ratings_df.iloc[user_row_number].sort_values(ascending=False)
        
        # Get the user's data and merge in the movie information
        user_data = data[data.user == user_id]
        user_full = user_data.merge(movies, how='left', on='id').sort_values(['rating'], ascending=False)
        
        sorted_user_predictions = sorted_user_predictions.reset_index()
        sorted_user_predictions.columns = ['title', 'Predictions']
        
        # Use the correct title column after the merge
        user_full_titles = user_full['title_y']
        
        # Recommend the highest predicted rating movies that the user hasn't seen yet
        recommendations = movies[~movies['title'].isin(user_full_titles)].merge(
            sorted_user_predictions, how='left', on='title').sort_values('Predictions', ascending=False)
        return recommendations[['title', 'Predictions']].head(num_recommendations)
    except IndexError:
        print(f"User ID {user_id} not found.")
        return pd.DataFrame(columns=['title', 'Predictions'])
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['title', 'Predictions'])

# Example usage
print(get_recommendations(user_id=1, num_recommendations=5))

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
    # Extract only the predictions
    user_predictions = user_recommendations['Predictions'].values
    predictions.extend(user_predictions)
    targets.extend(test_user_movie_matrix.loc[user_id].values)

# Ensure no NaN values in predictions and targets
predictions = np.nan_to_num(predictions)
targets = np.nan_to_num(targets)

print(f'RMSE: {rmse(predictions, targets)}')