NFL Rushing Stats Analysis Project
Overview
This project focuses on analyzing and predicting NFL rushing performance using statistical models and web-scraped data. The project involves:

Scraping and Preprocessing Data: Collecting player and team statistics from web sources.
Building Predictive Models: Using linear regression to predict rushing yards for players based on their performance and opposing teams' defensive stats.
Evaluation and Reporting: Testing the model's accuracy and visualizing results.
Project Objectives
Extract and clean data for NFL players and teams using BeautifulSoup.
Perform feature engineering to prepare the data for machine learning.
Build and evaluate a predictive model using sci-kit-learn.
Create a user-friendly interface for making predictions.
Datasets
Player Rushing Stats: Detailed player-level stats such as attempts, rushing yards, touchdowns, and yards per game (Y/G).
Defense Rushing Stats: Team-level defensive stats, including total rushing yards allowed per game.
Example Data
Player Rushing Stats (23_rb_stats.csv)

Player	Tm	G	Att	Yds	TD	Y/G
Derrick Henry	TEN	17	280	1167	12	68.6
Christian McCaffrey	SFO	16	272	1459	14	91.2
Defense Rushing Stats (23_defense_rush_stats.csv)

Tm	Att	Yds	TD
Arizona Cardinals	25.8	119.2	0.82
Seattle Seahawks	24.0	106.8	1.12
Key Features
Data Collection and Cleaning
Web Scraping: Extracted data from football statistics websites using BeautifulSoup.
Data Cleaning: Filtered and organized raw HTML data into structured CSV files for analysis.
Predictive Model
Regression Analysis: Trained a linear regression model using players' average yards per game (Y/G).
Feature Engineering: Combined player performance and opposing team defense stats to predict outcomes.
Evaluation
Metrics: Model performance was evaluated using Mean Squared Error (MSE) and R-squared (R²) scores.
Project Implementation
Dependencies
Python Libraries:
pandas for data manipulation.
sci-kit-learn for building and evaluating machine learning models.
BeautifulSoup for web scraping.
requests for fetching web content.
Key Scripts
Data Scraping:
Extracts player and team stats.
Saves data into CSV files for further processing.
Data Analysis:
Computes average yards per game for players and average yards allowed by teams.
Trains a linear regression model.
Prediction Function:
Predicts rushing yards for a player against a specific team's defense.
Example Prediction Code
player_name = "Derrick Henry"  
defense_team_name = "Arizona Cardinals"  
  

## Results  
- **Model Performance**:  
  - **MSE**: Evaluated the difference between actual and predicted rushing yards.  
  - **R² Score**: Measured the proportion of variance explained by the model.  

- **Example Prediction**:  
  Predicted rushing yards for Derrick Henry against the Arizona Cardinals: **72.5 yards/game**.  

## File Structure  
- **`data_scraping.py`**: Contains code for extracting and cleaning data using BeautifulSoup.  
- **`model_training.py`**: Includes code for training and evaluating the predictive model.  
- **`23_rb_stats.csv`**: Player rushing stats dataset.  
- **`23_defense_rush_stats.csv`**: Defensive stats dataset.  

## Future Enhancements  
- Integrate more advanced machine learning models for better accuracy.  
- Include additional features like weather conditions or player injury status.  
- Build a dashboard for interactive visualization and predictions.  
