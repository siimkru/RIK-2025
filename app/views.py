from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Company
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/company/<int:company_id>')
def company_detail(company_id):
    company = Company.query.get_or_404(company_id)
    return render_template('company_detail.html', company=company)


@main.route('/company/create', methods=['GET', 'POST'])
def company_create():
    if request.method == 'POST':
        name = request.form.get('name')
        reg_code = request.form.get('reg_code')

        if not name or not reg_code:
            flash("Palun täida kõik nõutud väljad!", "warning")
            return redirect(url_for('main.company_create'))

        company = Company(name=name, reg_code=reg_code)
        db.session.add(company)
        db.session.commit()

        flash("Osaühing lisatud edukalt!", "success")
        return redirect(url_for('main.company_detail', company_id=company.id))

    return render_template('company_create.html')
