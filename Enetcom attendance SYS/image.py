#importer le package Image de la bibliothèque Pillow
#from PIL import Image

#lire l'image 151.jpg
#n'oubliez pas de copier le dossier train dans votre espace de travail
#imageLue = Image.open("007.png")

#Convertir l'image au niveau de gris
#imageGris = imageLue.convert("L")

#Afficher l'image au niveau de gris
 #imageGris.show()

from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

# reading the image
img = imread('Mazen.jpeg')
plt.axis("off")
plt.imshow(img)
print(img.shape)
resized_img = resize(img, (128*4, 64*4))
plt.axis("off")
plt.imshow(resized_img)
print(resized_img.shape)

fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
plt.axis("off")
plt.imshow(hog_image, cmap="gray")
plt.imsave("resized_img.jpg", resized_img)
plt.imsave("hog_image.jpg", hog_image, cmap="gray")