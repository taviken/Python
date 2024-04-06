import numpy as np
import perlin_noise as pn
from PIL import Image


def get_noise_val(noises, xcoord, ycoord):
    val = 0.0
    for octave, noise in enumerate(noises):
        val += (1 / float(octave + 1)) * noise([xcoord, ycoord])
    return val


def NormalizeData(data):
    return (data - np.amin(data)) / (np.amax(data) - np.amin(data))


def gen_noise_map(grid_size=256):
    noise1 = pn.PerlinNoise(octaves=3)
    noise2 = pn.PerlinNoise(octaves=6)
    noise3 = pn.PerlinNoise(octaves=12)
    noise4 = pn.PerlinNoise(octaves=24)

    xpix, ypix = grid_size, grid_size
    column = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i / xpix, j / ypix])
            noise_val += 0.5 * noise2([i / xpix, j / ypix])
            noise_val += 0.25 * noise3([i / xpix, j / ypix])
            noise_val += 0.125 * noise4([i / xpix, j / ypix])

            row.append(noise_val)
        column.append(row)

    data = np.array(column)
    data = NormalizeData(data) * 255
    im = Image.fromarray(data)
    return im


if __name__ == '__main__':
    im = gen_noise_map()
    im.show()
    im.convert('L').save(r'C:\Users\nekiv\Desktop/terrain.png')
