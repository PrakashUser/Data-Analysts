import pandas as pd

# Load the Excel file
file_path =  r"D:\\Cognifyz_Internship\\Internship_Task.xlsx"

df = pd.read_excel(  r"D:\\Cognifyz_Internship\\Internship_Task.xlsx")

# Ensure the necessary columns exist
if 'City' not in df.columns or 'Aggregate rating' not in df.columns:
    raise ValueError("Dataset must contain 'City' and 'Aggregate rating' columns")

# City with the highest number of restaurants
city_counts = df['City'].value_counts()
highest_restaurant_city = city_counts.idxmax()

# Average rating for restaurants in each city
city_avg_rating = df.groupby('City')['Aggregate rating'].mean()

# City with the highest average rating
highest_avg_rating_city = city_avg_rating.idxmax()

# Display results
print(f"City with the highest number of restaurants: {highest_restaurant_city} ({city_counts.max()} restaurants)")
print("\nAverage rating per city:")
print(city_avg_rating)
print(f"\nCity with the highest average rating: {highest_avg_rating_city} ({city_avg_rating.max():.2f} rating)")
