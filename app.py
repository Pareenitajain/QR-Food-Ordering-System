from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.Text)
    total_price = db.Column(db.Float)
    status = db.Column(db.String(50), default="Received")
    time = db.Column(db.DateTime, default=datetime.now)



@app.route('/')
def menu():
    foods = Food.query.all()
    return render_template('menu.html', foods=foods)

@app.route('/place_order', methods=['POST'])
def place_order():
    items = request.form['items']
    total = request.form['total']

    # Create order in database
    order = Order(
        items=items,
        total_price=float(total)
    )
    db.session.add(order)
    db.session.commit()

    # Pass order details to confirmation page
    return render_template('order_confirmation.html', 
                         order_id=order.id, 
                         items=items, 
                         total=total,
                         order_time=order.time)


@app.route('/admin')
def admin():
    orders = Order.query.order_by(Order.time.desc()).all()
    return render_template('admin.html', orders=orders)

@app.route('/update_order_status/<int:order_id>', methods=['POST'])
def update_order_status(order_id):
    """Update order status from admin dashboard"""
    data = request.get_json()
    new_status = data.get('status')
    
    order = Order.query.get(order_id)
    if order:
        order.status = new_status
        db.session.commit()
        return jsonify({'success': True, 'message': 'Order status updated!'})
    
    return jsonify({'success': False, 'message': 'Order not found'}), 404

@app.route('/api/orders-count')
def get_orders_count():
    """Get total number of orders"""
    count = Order.query.count()
    return jsonify({'count': count})

@app.route('/api/latest-orders')
def get_latest_orders():
    """Get orders as JSON for real-time updates"""
    orders = Order.query.order_by(Order.time.desc()).all()
    return jsonify([
        {
            'id': order.id,
            'items': order.items,
            'total_price': order.total_price,
            'status': order.status,
            'time': order.time.strftime('%d-%m-%Y %H:%M:%S'),
            'created_at': order.time.timestamp()
        }
        for order in orders
    ])


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    with app.app_context():
        db.create_all()

        # Add sample food items (only once)
        if Food.query.count() == 0:
            db.session.add(Food(name="Burger", price=120, description="Cheese Burger"))
            db.session.add(Food(name="Pizza", price=250, description="Veg Pizza"))
            db.session.add(Food(name="Pasta", price=180, description="White Sauce Pasta"))
            db.session.commit()

    app.run(host='0.0.0.0', port=port, debug=False)
