from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    ordered_at = db.Column(db.DateTime, default=datetime.now())
    first_name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(15))
    tours = db.relationship("Tour", secondary=orderdetails, backref="orders")

class Tour(db.Model):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"))

class city(db.Model):
    __tablename__ ="cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    tours = db.relationship("Tour", backref="city")

orderdetails = db.Table("orderdetails", db.Column("order_id"), db.Integer, db.ForeignKey("orders.id"), db.Column("tour_id", db.Integer, db.ForeignKey("tours.id")), db.PrimaryKeyConstraint("order_id"))
