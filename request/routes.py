from datetime import datetime
import json

from flask import (render_template, jsonify, request, 
                    flash, url_for, redirect)

from . import app, models, forms, db

@app.route('/', methods=['GET', 'POST'])
def index():
    clients=models.Client.query.all()
    request_form = forms.RequestForm()
    if request.method == 'POST':
        if request_form.validate_on_submit():
            data = models.Request.query.filter(
                        models.Request.priority>=request_form.priority.data, 
                        models.Request.client_id==request_form.client.data).all()
            for obj in data:
                obj.priority = obj.priority + 1
            priority = request_form.priority.data
            request_count = models.Request.query.filter(
                        models.Request.client_id==request_form.client.data).count()
            if priority >= request_count:
                priority = request_count + 1

            new_request = models.Request(
                    title=request_form.title.data,
                    description=request_form.description.data,
                    client_id=request_form.client.data,
                    priority=priority,
                    target_date=request_form.target_date.data,
                    product=request_form.product.data,
            )
            data.append(new_request)
            db.session.add_all(data)
            db.session.commit()
            flash('Request successfully recorded #winks', 'success')
            return redirect(url_for('index'))
        else:
            flash('Oops!!! Something went wrong', 'error')
    return render_template('index.html', request_form=request_form, clients=clients)

@app.route('/get-request-data/')
def get_request_data():
    clients = [{"id":x.id, "name":x.name, "requests": x.request.count()} for x in models.Client.query.all()]
    products = [[x.name, x.name.capitalize()] for x in models.ProductEnum]
    return jsonify(clients=clients, products=products)