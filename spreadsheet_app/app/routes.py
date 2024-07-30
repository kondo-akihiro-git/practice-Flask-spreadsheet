from flask import render_template, request, redirect, url_for
from app import db
from app.models import Spreadsheet

def register_routes(app):
    @app.route('/')
    def index():
        spreadsheets = Spreadsheet.query.all()
        return render_template('index.html', spreadsheets=spreadsheets)

    @app.route('/create', methods=['POST'])
    def create():
        name = request.form['name']
        new_spreadsheet = Spreadsheet(name=name, data='')
        db.session.add(new_spreadsheet)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        spreadsheet = Spreadsheet.query.get_or_404(id)
        if request.method == 'POST':
            spreadsheet.data = request.form['data']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit.html', spreadsheet=spreadsheet)
