from PIL import Image
import numpy

sobelMatricies = {
    "3x3 Vertical": [[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]],
    "3x3 Horizontal": [[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]],
    "5x5 Vertical": [[-1, -2, 0, 2, 1],
                      [-2, -4, 0, 4, 2],
                      [-4, -8, 0, 8, 4],
                      [-2, -4, 0, 4, 2],
                      [-1, -2, 0, 2, 1]],
    "5x5 Horizontal": [[-1, -2, -4, -2, -1],
                       [-2, -4, -8, -4, -2],
                       [0, 0, 0, 0, 0],
                       [2, 4, 8, 4, 2],
                       [1, 2, 4, 2, 1]]
}

outputPictures = {}

picture = Image.open("skyline-bw.jpg").convert("L")
pictureArray = numpy.asarray(picture)

for matrix in sobelMatricies.keys():
    sobel = sobelMatricies[matrix]
    outputPictures[matrix] = []
    for i in range(picture.height):
        outputPictures[matrix].append([])
        for j in range(picture.width):
            sobelValue = 0
            if "3" in matrix:
                sobelValue = ((sobel[0][0] * pictureArray[i - 1][j - 1] if i >= 1 and j >= 1 else 0) + (sobel[0][1] * pictureArray[i - 1][j] if i >= 0 else 0) + (sobel[0][2] * pictureArray[i - 1][j + 1] if i >= 1 and j < picture.width -1 else 0) +
                              (sobel[1][0] * pictureArray[i][j - 1] if j >= 1 else 0) + (sobel[1][1] * pictureArray[i][j]) + (sobel[1][2] * pictureArray[i][j + 1] if j < picture.width - 1 else 0) +
                              (sobel[2][0] * pictureArray[i + 1][j - 1] if i < picture.height - 1 and j >= 1 else 0) + (sobel[2][1] * pictureArray[i + 1][j] if i < picture.height - 1 else 0) + (sobel[2][2] * pictureArray[i + 1][j + 1] if i < picture.height - 1 and j < picture.width - 1 else 0))

            elif "5" in matrix:
                sobelValue = ((sobel[0][0] * pictureArray[i - 2][j - 2] if i >= 2 and j >= 2 else 0) + (sobel[0][1] * pictureArray[i - 2][j - 1] if i >= 2 and j >= 1 else 0) + (sobel[0][2] * pictureArray[i - 2][j] if i >= 2 else 0) + (sobel[0][3] * pictureArray[i - 2][j + 1] if i >= 2 and j < picture.width - 1 else 0) + (sobel[0][4] * pictureArray[i - 2][j + 2] if i >= 2 and j < picture.width - 2 else 0) +
                                                (sobel[1][0] * pictureArray[i - 1][j - 2] if i >= 1 and j >= 2 else 0) + (sobel[1][1] * pictureArray[i - 1][j - 1] if i >= 1 and j >= 1 else 0) + (sobel[1][2] * pictureArray[i - 1][j] if i >= 1 else 0) + (sobel[1][3] * pictureArray[i - 1][j + 1] if i >= 1 and j < picture.width - 1 else 0) + (sobel[1][4] * pictureArray[i - 1][j + 2] if i >= 1 and j < picture.width - 2 else 0) +
                                                (sobel[2][0] * pictureArray[i - 0][j - 2] if i >= 0 and j >= 2 else 0) + (sobel[2][1] * pictureArray[i - 0][j - 1] if i >= 0 and j >= 1 else 0) + (sobel[2][2] * pictureArray[i - 0][j] if i >= 0 else 0) + (sobel[2][3] * pictureArray[i - 0][j + 1] if i >= 0 and j < picture.width - 1 else 0) + (sobel[2][4] * pictureArray[i - 0][j + 2] if i >= 0 and j < picture.width - 2 else 0) +
                                                (sobel[3][0] * pictureArray[i + 1][j - 2] if i < picture.height - 1 and j >= 2 else 0) + (sobel[3][1] * pictureArray[i + 1][j - 1] if i < picture.height - 1 and j >= 1 else 0) + (sobel[3][2] * pictureArray[i + 1][j] if i < picture.height - 1 else 0) + (sobel[3][3] * pictureArray[i + 1][j + 1] if i < picture.height - 1 and j < picture.width - 1 else 0) + (sobel[3][4] * pictureArray[i + 1][j + 2] if i < picture.height - 1 and j < picture.width - 2 else 0) +
                                                (sobel[4][0] * pictureArray[i + 2][j - 2] if i < picture.height - 2 and j >= 2 else 0) + (sobel[4][1] * pictureArray[i + 2][j - 1] if i < picture.height - 2 and j >= 1 else 0) + (sobel[4][2] * pictureArray[i + 2][j] if i < picture.height - 2 else 0) + (sobel[4][3] * pictureArray[i + 2][j + 1] if i < picture.height - 2 and j < picture.width - 1 else 0) + (sobel[4][4] * pictureArray[i + 2][j + 2] if i < picture.height - 2 and j < picture.width - 2 else 0))

            outputPictures[matrix][i].append(numpy.uint8(sobelValue / 255))
    Image.fromarray(numpy.asarray(outputPictures[matrix])).save("{}.bmp".format(matrix))

gradientPictures = {
    "3x3": [],
    "5x5": []
}
for key in gradientPictures.keys():
    for i in range(picture.height):
        gradientPictures[key].append([])
        for j in range(picture.width):
            gradientValue = (((outputPictures[key + " Vertical"][i][j] ** 2) + (outputPictures[key + " Horizontal"][i][j] ** 2)) ** .5)

            gradientPictures[key][i].append(numpy.uint8(gradientValue))

    Image.fromarray(numpy.asarray(gradientPictures[key])).save("{} Gradient Threshold.png".format(key))
