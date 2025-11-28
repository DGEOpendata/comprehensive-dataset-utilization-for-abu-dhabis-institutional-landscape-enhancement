
import pandas as pd

# Load the dataset
url = 'https://example.com/abu_dhabi_organizations.csv'
dataset = pd.read_csv(url)

# Display the first few rows of the dataset
dataset.head()

# Analyzing the dataset for insights
# Group by sector and count the number of organizations in each sector
sector_analysis = dataset.groupby('Sector')['Organization Name'].count()
print(sector_analysis)

# Filter organizations with a specific role
heritage_organizations = dataset[dataset['Primary Function'].str.contains('heritage', case=False)]
print(heritage_organizations[['Organization Name', 'Primary Function']])

# Example: Save filtered data to a new CSV file
heritage_organizations.to_csv('heritage_organizations.csv', index=False)
