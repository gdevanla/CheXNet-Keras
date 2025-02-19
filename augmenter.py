# from imgaug import augmenters as iaa

# augmenter = iaa.Sequential(
#     [
#         iaa.Fliplr(0.5),
#     ],
#     random_order=True,
# )

import albumentations as A

augmenter = A.Compose([
    A.HorizontalFlip(p=0.5),
])

print("Albumentations setup complete!")
