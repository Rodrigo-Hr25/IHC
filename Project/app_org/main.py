from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required, current_user
from app_org.models import User, Product, Category, Course
from app_org import db
from flask import request, redirect, url_for
main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@login_required
def index():
    user = User.query.filter_by(id=current_user.id).first()

    stock = request.args.get('stock')
    price_min = request.args.get('price_min')
    price_max = request.args.get('price_max')
    categories = request.args.getlist('categories') 
    courses = request.args.getlist('courses')
    sizes = request.args.getlist('sizes') 
    colors = request.args.getlist('colors') 

    query = Product.query

    if stock == 'in':
        query = query.filter_by(has_stock=True)
    elif stock == 'out':
        query = query.filter_by(has_stock=False)

    if price_min:
        query = query.filter(Product.price >= float(price_min))
    if price_max:
        query = query.filter(Product.price <= float(price_max))

    if categories:
        query = query.filter(Product.category_id.in_(categories))

    if courses:
        query = query.filter(Product.course_id.in_(courses))

    if sizes:
        query = query.filter(Product.size.in_(sizes))

    if colors:
        query = query.filter(Product.color.in_(colors))

    products = query.all()

    all_categories = Category.query.all()
    all_courses = Course.query.all()
    all_sizes = db.session.query(Product.size).distinct().all()
    all_colors = db.session.query(Product.color).distinct().all()

    return render_template('index.html', user=user, products=products,
                           categories=all_categories, courses=all_courses,
                           sizes=[s[0] for s in all_sizes if s[0]], 
                           colors=[c[0] for c in all_colors if c[0]])


@main.route('/' , methods=['POST'])
@login_required
def index_post():
    products = Product.query.all()
    return render_template('index.html', products=products)


@main.route('/product/<int:product_id>', methods=['GET'])
@login_required
def product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return render_template('404.html')
    return render_template('product.html', product=product)


@main.route('/addproduct', methods=['GET'])
@login_required
def add_product():
    user=User.query.filter_by(id=current_user.id).first()
    if user.isAdmin == False:
        return redirect(url_for('main.index'))
    else:
        return render_template('addproduct.html')

@main.route('/addproduct', methods=['POST'])
@login_required
def add_product_post():
    name = request.form.get('name')
    price = request.form.get('price')
    description = request.form.get('description')
    image = request.files.get('image')
    if image and not image.filename.endswith('.png') and not image.filename.endswith('.jpeg'):
        print('Please upload a .png or .jpeg image.')
        return redirect(url_for('main.add_product'))
    product = Product(name=name, price=price, description=description, image=image.filename)
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('main.index'))