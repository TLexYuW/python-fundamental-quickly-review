import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
from wordcloud import WordCloud


text = "Hello World"

wc = WordCloud(width=1000, height=600, background_color="white").generate(text)
plt.axis("off")
plt.imshow(wc)
plt.show()