import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data from a CSV file
data = pd.read_csv('chaya.csv')

# Get the text data for the word cloud (Cart_Abandonment_Factors column)
abandonment_factors = data['Cart_Abandonment_Factors'].str.cat(sep=' ')

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(abandonment_factors)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Cart Abandonment Factors')

# Show the plot
plt.show()
