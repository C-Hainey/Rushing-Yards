import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the datasets
rushing_stats = pd.read_csv('23_rb_stats.csv')
defense_stats = pd.read_csv('23_defense_rush_stats.csv')

# Define helper functions
def get_player_avg_yards(player_name, rushing_df):
    player_stats = rushing_df[rushing_df['Player'] == player_name]
    if not player_stats.empty:
        return player_stats['Y/G'].values[0]
    else:
        print("Available players:", rushing_df['Player'].unique())  # Print available players for debugging
        raise ValueError(f"Player '{player_name}' not found in rushing stats.")

def get_defense_avg_yards_allowed(team_name, defense_df):
    defense_stats = defense_df[defense_df['Tm'] == team_name]
    if not defense_stats.empty:
        return defense_stats['Yds'].values[0]
    else:
        print("Available teams:", defense_df['Tm'].unique())  # Print available teams for debugging
        raise ValueError(f"Team '{team_name}' not found in defense stats.")

# Prepare the feature matrix and target variable
X = rushing_stats[['Y/G']]  # Use 'Y/G' as the feature
y = rushing_stats['Y/G']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))

# Predicting for new data
def predict_rushing_yards(player_name, defense_team_name, rushing_df, defense_df, model):
    player_avg_yards = get_player_avg_yards(player_name, rushing_df)
    defense_avg_yards_allowed = get_defense_avg_yards_allowed(defense_team_name, defense_df)
    
    # Create a DataFrame for prediction
    new_data = pd.DataFrame({
        'Y/G': [player_avg_yards]  # Use player average yards per game as input feature
    })
    
    predicted_yards = model.predict(new_data)
    return predicted_yards[0]

# Main program
if __name__ == "__main__":
    player_name = input("Enter the player's name: ")
    defense_team_name = input("Enter the defense team's name: ")

    try:
        predicted_yards = predict_rushing_yards(player_name, defense_team_name, rushing_stats, defense_stats, model)
        print(f"Predicted Yards per Game for {player_name} against {defense_team_name}: {predicted_yards:.2f}")
    except ValueError as e:
        print(e)