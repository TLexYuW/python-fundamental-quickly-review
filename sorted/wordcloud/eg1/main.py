import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

text = open("../python.txt", "r").read()

# exclude
print(STOPWORDS)

python_mask = np.array(PIL.Image.open("../py.jpg"))

colormap = ImageColorGenerator(python_mask)

wc = WordCloud(height=1000, width=1000,
               stopwords=set(list(STOPWORDS) + ["code"]),
               mask=python_mask, background_color="white",
               contour_width=1,
               contour_color="white",
               min_font_size=3,
               max_words=400).generate(text)

wc.recolor(color_func=colormap)
plt.imshow(wc)
plt.axis("off")
plt.show()
