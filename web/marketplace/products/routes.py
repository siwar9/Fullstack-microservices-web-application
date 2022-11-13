from flask import redirect, render_template, url_for,flash,request
from marketplace import ALLOWED_EXTENSIONS, db, app
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets
import os
from werkzeug.utils import secure_filename


@app.route('/')
def home():
    products = Addproduct.query.filter(Addproduct.stock >0) #display only available items
    brands = Brand.query.all()
    categories = Category.query.all()
    return render_template('products/index.html', products=products,brands=brands,categories=categories)


@app.route('/addbrand',methods = ['GET','POST'])
def addbrand():
    if request.method=="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added successfully!', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands='brands')


@app.route('/addcategory',methods = ['GET','POST'])
def addcategory():
    if request.method=="POST":
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        flash(f'The category {getcategory} was added successfully!', 'success')
        db.session.commit()
        return redirect(url_for('addcategory'))
    return render_template('products/addbrand.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        stock = form.stock.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file=file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
        addpro=Addproduct(name=name,price=price,stock=stock,brand_id=brand,category_id=category,file=filename)
        db.session.add(addpro)
        flash(f'The product {name} was added successfully!', 'success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addproduct.html', title="Add Product Page", form=form, brands=brands, categories=categories)
