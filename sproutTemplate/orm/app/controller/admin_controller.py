from app import db
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from app.model.seed import Seed
from app.model.seedform import SeedForm


class AdminController():
    def seedregister(self):
        form = SeedForm()
        if form.validate_on_submit():
            seed = Seed(name=form.seedname.data, seed_type=form.seed_type.data,
            price = form.price.data, quantity=form.quantity.data)
            db.session.add(seed)
            db.session.commit()
            flash('Congratulations, you add seeds to the store!')
            return redirect(url_for('admin'))
        seeddisplay = Seed.get_all()
        return render_template('admin/admin.html', title='Admin', form=form, seeddisplay=seeddisplay)


admin_controller = AdminController()