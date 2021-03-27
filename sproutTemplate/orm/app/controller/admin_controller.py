from app import db
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from app.model.seed import Seed
from app.model.seedform import SeedForm, SeedUpdate, SeedDelete


class AdminController():
    def seedregister(self):
        #this function registers the seed into the database
        form = SeedForm()
        if form.validate_on_submit():
            seed = Seed(name=form.seedname.data, seed_type=form.seed_type.data,
            price = form.price.data, quantity=form.quantity.data)
            db.session.add(seed)
            db.session.commit()
            flash('Congratulations, you add seeds to the store!')
            return redirect(url_for('admin'))
        seeddisplay = Seed.get_all()
        return render_template('admin/admin.html', title='Admin Register', form=form, seeddisplay=seeddisplay)
    
    def seedupdate(self): 
        #this function updates the seed database   
        all_seeds = db.session.query(Seed).order_by('name').all()
        seed_group_name = [(i.id, i.name) for i in all_seeds]
        form = SeedUpdate()
        form.seedname.choices = seed_group_name
        if form.validate_on_submit():
            Seed.adminupdate(seedname=form.seedname.data, quantity=form.quantity.data)
            flash('Added Quantity to Seed')
            return redirect(url_for('adminupdate'))
        
        seeddisplay = Seed.get_all()
        return render_template('admin/adminupdate.html', title='Admin Update', seedupdate=form, seeddisplay=seeddisplay)

    def seeddelete(self):
        #this function deletes the seed from the database
        all_seeds = db.session.query(Seed).order_by('name').all()
        seed_group_name = [(i.id, i.name) for i in all_seeds]
        form = SeedDelete()
        form.seedname.choices = seed_group_name
        if form.validate_on_submit():
            Seed.admindelete(seedname=form.seedname.data)
            flash('Deleted Seed')
            return redirect(url_for('admindelete'))
        seeddisplay = Seed.get_all()
        return render_template('admin/admindelete.html', title='Admin Delete', seeddelete=form, seeddisplay=seeddisplay)




admin_controller = AdminController()