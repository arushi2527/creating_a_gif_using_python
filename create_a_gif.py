import imageio.v3 as iio

filenames = ['kuromi1.png', 'kuromi2.png']

images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('kuromi.gif', images, duration = 500, loop = 0 )