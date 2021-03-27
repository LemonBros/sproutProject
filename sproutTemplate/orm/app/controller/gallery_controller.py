from flask import render_template
from app.model.seed import Seed
# """gallery controller returns the image path and the gallery items name"""
class GalleryController:
    @staticmethod
    def get(seed_type):
        seeds = Seed.get_by_type(seed_type)
        for item in seeds:
            item['imagePath'] = "images/%s.png" % (item['name'])
        return seeds