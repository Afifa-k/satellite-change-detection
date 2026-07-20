import rasterio

with rasterio.open(r"C:\Users\Afifa\Desktop\OSCD\Onera Satellite Change Detection dataset - Images\abudhabi\imgs_1_rect\B04.tif") as src:
    image = src.read(1)

print(type(image))
print(image.dtype)
print(image.shape)

print(image[0,0])
print(image[10,20])
print(image.min())
print(image.max())