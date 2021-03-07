from flask import render_template
from app.model.seed import Seed

class GalleryController:
    @staticmethod
    def get(seed_type):
        return Seed.get_by_type(seed_type)