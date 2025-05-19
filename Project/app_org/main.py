from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app_org.models import User, Product, Category, Course, Submission, Vote, Contest
from app_org import db
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@login_required
def index():
    user = User.query.filter_by(id=current_user.id).first()
    
    if user.isAdmin:
        return redirect(url_for('main.admin'))

    stock = request.args.get('stock')
    price_min = request.args.get('price_min')
    price_max = request.args.get('price_max')
    categories = request.args.getlist('categories') 
    courses = request.args.getlist('courses')
    sizes = request.args.getlist('sizes') 
    colors = request.args.getlist('colors') 

    query = Product.query

    if stock == 'in':
        query = query.filter(Product.quantity > 0)
    elif stock == 'out':
        query = query.filter(Product.quantity == 0)

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

@main.route('/', methods=['POST'])
@login_required
def index_post():
    user = User.query.filter_by(id=current_user.id).first()
    if user.isAdmin:
        return redirect(url_for('main.admin'))
    
    products = Product.query.all()
    return render_template('index.html', user=user, products=products)

@main.route('/admin', methods=['GET'])
@login_required
def admin():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))

    stock = request.args.get('stock')
    price_min = request.args.get('price_min')
    price_max = request.args.get('price_max')
    categories = request.args.getlist('categories') 
    courses = request.args.getlist('courses')
    sizes = request.args.getlist('sizes') 
    colors = request.args.getlist('colors') 

    query = Product.query

    if stock == 'in':
        query = query.filter(Product.quantity > 0)
    elif stock == 'out':
        query = query.filter(Product.quantity == 0)

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

    return render_template('indexAdmin.html', user=user, products=products,
                           categories=all_categories, courses=all_courses,
                           sizes=[s[0] for s in all_sizes if s[0]], 
                           colors=[c[0] for c in all_colors if c[0]])

@main.route('/profileAdmin', methods=['GET'])
@login_required
def profile_admin():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    return render_template('profileAdmin.html', user=user)

@main.route('/edit_profileAdmin', methods=['GET'])
@login_required
def edit_profile_admin():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    return render_template('editAdmin.html', user=user)

@main.route('/product/<int:product_id>', methods=['GET'])
@login_required
def product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return render_template('404.html')
    return render_template('product.html', product=product)

@main.route('/product_admin/<int:product_id>', methods=['GET'])
@login_required
def product_admin(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return render_template('404.html')
    return render_template('productAdmin.html', product=product)

@main.route('/edit_product/<int:product_id>', methods=['GET'])
@login_required
def edit_product(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return render_template('404.html')
    return render_template('editProduct.html', product=product)

@main.route('/update_product/<int:product_id>', methods=['POST'])
@login_required
def update_product(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    product = Product.query.get_or_404(product_id)
    product.name = request.form.get('name')
    product.description = request.form.get('description')
    product.price = float(request.form.get('price'))
    product.quantity = int(request.form.get('quantity'))
    category_name = request.form.get('category')
    category = Category.query.filter_by(name=category_name).first()
    if category:
        product.category_id = category.id
    else:
        flash('Category not found. Please ensure the category exists.', 'warning')
        return redirect(url_for('main.edit_product', product_id=product.id))
    db.session.commit()
    flash('Product updated successfully!', 'success')
    return redirect(url_for('main.edit_product', product_id=product.id))

@main.route('/upload_image/<int:product_id>', methods=['POST'])
@login_required
def upload_image(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    product = Product.query.get_or_404(product_id)
    image = request.files.get('image')
    if image and (image.filename.endswith('.png') or image.filename.endswith('.jpeg')):
        image.save(os.path.join('app_org/static/assets', image.filename))
        product.image = image.filename
        db.session.commit()
        flash('Image updated successfully!', 'success')
    else:
        flash('Please upload a .png or .jpeg image.', 'warning')
    return redirect(url_for('main.edit_product', product_id=product.id))

@main.route('/addproduct', methods=['GET'])
@login_required
def add_product():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    categories = Category.query.all()
    courses = Course.query.all()
    return render_template('addproduct.html', user=user, categories=categories, courses=courses)

@main.route('/addproduct', methods=['POST'])
@login_required
def add_product_post():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))

    name = request.form.get('name')
    description = request.form.get('description')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    category_id = int(request.form.get('category_id'))
    course_id = request.form.get('course_id')
    if course_id:
        course_id = int(course_id)
    else:
        course_id = None
    has_size = request.form.get('has_size') == 'true' 
    has_color = request.form.get('has_color') == 'true'
    size = request.form.get('size', 'N/A') if has_size else 'N/A'
    color = request.form.get('color', 'N/A') if has_color else 'N/A' 
    image = request.files.get('image')

    if not image or not (image.filename.endswith('.png') or image.filename.endswith('.jpeg')):
        flash('Please upload a .png or .jpeg image.', 'warning')
        return redirect(url_for('main.add_product'))

    image_filename = image.filename
    image.save(os.path.join('app_org/static/assets', image_filename))

    product = Product(
        name=name,
        description=description,
        price=price,
        quantity=quantity,
        image=image_filename,
        category_id=category_id,
        course_id=course_id,
        has_size=has_size,
        has_color=has_color,
        size=size,
        color=color
    )

    db.session.add(product)
    db.session.commit()
    flash('Product added successfully!', 'success')
    return redirect(url_for('main.admin'))

@main.route('/delete_product/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('main.admin'))

@main.route('/contests', methods=['GET'])
@login_required
def contests():
    user = User.query.filter_by(id=current_user.id).first()
    if user.isAdmin:
        return redirect(url_for('main.concurso'))
    
    contests = Contest.query.filter_by(is_active=True).all()
    voted_submission_ids = [vote.submission_id for vote in Vote.query.filter_by(user_id=user.id).join(Submission).join(Contest).filter(Contest.is_active == True).all()]
    
    return render_template('contests.html', user=user, contests=contests, voted_submission_ids=voted_submission_ids)

@main.route('/ended_contests', methods=['GET'])
@login_required
def ended_contests():
    user = User.query.filter_by(id=current_user.id).first()
    if user.isAdmin:
        return redirect(url_for('main.ended_contests_admin'))
    
    ended_contests = Contest.query.filter_by(is_active=False).all()
    return render_template('ended_contests.html', ended_contests=ended_contests)

@main.route('/vote/<int:submission_id>', methods=['POST'])
@login_required
def vote_submission(submission_id):
    user = User.query.filter_by(id=current_user.id).first()
    if user.isAdmin:
        return redirect(url_for('main.concurso'))
    
    submission = Submission.query.get_or_404(submission_id)
    if not submission.approved or not submission.contest.is_active:
        flash('This submission is not available for voting.', 'warning')
        return redirect(url_for('main.contests'))

    existing_vote = Vote.query.filter_by(user_id=user.id).join(Submission).filter(Submission.contest_id == submission.contest_id).first()
    if existing_vote:
        if existing_vote.submission_id != submission_id:
            previous_submission = Submission.query.get(existing_vote.submission_id)
            previous_submission.votes -= 1
            db.session.delete(existing_vote)
            db.session.commit()
        else:
            flash('You have already voted for this submission.', 'warning')
            return redirect(url_for('main.contests'))

    vote = Vote(user_id=user.id, submission_id=submission_id)
    submission.votes += 1
    db.session.add(vote)
    db.session.commit()
    flash('Your vote has been recorded!', 'success')
    return redirect(url_for('main.contests'))

@main.route('/unvote/<int:submission_id>', methods=['POST'])
@login_required
def unvote_submission(submission_id):
    user = User.query.filter_by(id=current_user.id).first()
    if user.isAdmin:
        return redirect(url_for('main.concurso'))
    
    submission = Submission.query.get_or_404(submission_id)
    if not submission.approved or not submission.contest.is_active:
        flash('This submission is not available for unvoting.', 'warning')
        return redirect(url_for('main.contests'))

    existing_vote = Vote.query.filter_by(user_id=user.id, submission_id=submission_id).first()
    if not existing_vote:
        flash('You have not voted for this submission.', 'warning')
        return redirect(url_for('main.contests'))

    submission.votes -= 1
    db.session.delete(existing_vote)
    db.session.commit()
    flash('Your vote has been retracted!', 'success')
    return redirect(url_for('main.contests'))

@main.route('/picture', methods=['GET'])
@login_required
def picture():
    user = User.query.filter_by(id=current_user.id).first()
    if user.isAdmin:
        return redirect(url_for('main.concurso'))
    
    active_contest = Contest.query.filter_by(is_active=True).order_by(Contest.id.desc()).first()
    
    return render_template('picture.html', user=user, active_contest=active_contest)

@main.route('/submit_design', methods=['POST'])
@login_required
def submit_design():
    user = User.query.filter_by(id=current_user.id).first()
    if user.isAdmin:
        return redirect(url_for('main.concurso'))

    name = request.form.get('name')
    description = request.form.get('description')
    image = request.files.get('image')

    active_contest = Contest.query.filter_by(is_active=True).order_by(Contest.id.desc()).first()
    
    if not active_contest:
        flash('There are no active contests at the moment. Please wait for a new contest to be created.', 'warning')
        return redirect(url_for('main.picture'))

    if not image or not image.filename.endswith('.png'):
        flash('Please upload a .png image.', 'warning')
        return redirect(url_for('main.picture'))

    image_filename = image.filename
    image.save(os.path.join('app_org/static/assets', image_filename))

    submission = Submission(
        name=name,
        description=description,
        image=image_filename,
        user_id=user.id,
        approved=False,
        votes=0,
        contest_id=active_contest.id
    )

    db.session.add(submission)
    db.session.commit()
    flash('Your design has been submitted for review!', 'success')
    return redirect(url_for('main.contests'))

@main.route('/contestsAdmin', methods=['GET'])
@login_required
def concurso():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    
    contests = Contest.query.filter_by(is_active=True).all()
    return render_template('contestsAdmin.html', user=user, contests=contests)

@main.route('/ended_contests_admin', methods=['GET'])
@login_required
def ended_contests_admin():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.ended_contests'))
    
    ended_contests = Contest.query.filter_by(is_active=False).all()
    return render_template('ended_contestsAdmin.html', ended_contests=ended_contests)

@main.route('/submit', methods=['GET'])
@login_required
def submit():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    submissions = Submission.query.all()
    return render_template('submissions.html', user=user, submissions=submissions)

@main.route('/approve_submission/<int:submission_id>', methods=['POST'])
@login_required
def approve_submission(submission_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    
    submission = Submission.query.get_or_404(submission_id)
    submission.approved = True
    db.session.commit()
    flash('Submission approved successfully!', 'success')
    return redirect(url_for('main.submit'))

@main.route('/reject_submission/<int:submission_id>', methods=['POST'])
@login_required
def reject_submission(submission_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    
    submission = Submission.query.get_or_404(submission_id)
    db.session.delete(submission)
    db.session.commit()
    flash('Submission rejected successfully!', 'success')
    return redirect(url_for('main.submit'))

@main.route('/end_contest/<int:contest_id>', methods=['POST'])
@login_required
def end_contest(contest_id):
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    
    contest = Contest.query.get_or_404(contest_id)
    contest.is_active = False
    db.session.commit()
    flash(f'Contest {contest.name} has been ended successfully!||{contest_id}', 'success')
    return redirect(url_for('main.concurso'))

@main.route('/create_contest', methods=['POST'])
@login_required
def create_contest():
    user = User.query.filter_by(id=current_user.id).first()
    if not user.isAdmin:
        return redirect(url_for('main.index'))
    
    name = request.form.get('contest_name')
    if not name:
        flash('Please provide a contest name.', 'warning')
        return redirect(url_for('main.concurso'))
    
    contest = Contest(name=name, is_active=True)
    db.session.add(contest)
    db.session.commit()
    flash(f'Contest {name} created successfully!||{contest.id}', 'success')
    return redirect(url_for('main.concurso'))