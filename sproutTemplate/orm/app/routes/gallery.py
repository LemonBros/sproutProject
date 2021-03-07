from app import app 
from flask import render_template, request
from app.controller.gallery_controller import GalleryController

@app.route('/gallery')
def gallery():
    seed_type = request.args.get('seed_type')
    inventory = GalleryController.get(seed_type)
    return render_template('gallery-tab/gallery.html', seed_type = seed_type, inventory = inventory)
