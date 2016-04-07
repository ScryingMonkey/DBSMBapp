from application import db

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	social_id = db.Column(db.Integer, nullable=True) #<-------------Change nullable to false when Oauth is implemented
	name = db.Column(db.String(250), nullable=False)
	email = db.Column(db.String(250), unique=True, nullable=False)
	password = db.Column(db.String(250), nullable=False)
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
	def __repr__(self):
		return '<Users %r>' % self.name
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id'           : self.id,
			'social_id     : self.social_id,
			'name'         : self.name,
			'email'        : self.email,
		}

class Messages(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Coumn(db.String(250), nullable=False)
	text = db.Column(db.String(250), nullable = False)
	def __init__(self, title, text):
		self.title = title
		self.text = text
	def __repr__(self):
		return '<Messages %r>' % self.title
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id'         : self.id,
			'title'      : self.title,
			'text'       : self.test
		}
 
class Inventory(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=False)
	price = db.Column(db.Integer, nullable=False)
	quantityAvailable = db.Column(db.Integer, nullable=False)
	def __init__(self, name, description, price, quantityAvaliable):
		self.name = name
		self.description = description
		self.price = price
		self.quantityAvailable = quantityAvailable
	def __repr__(self):
		return '<Inventory %r>' % self.name
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id'                : self.id,
			'name'              : self.name,
			'description'       : self.description,
			'price'             : self.price,
			'quantityAvailable' : self.quantityAvailable
        }

class Orders(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
	users = db.relationship('Users', backref=db.backref('posts', lazy='dynamic'))
	item_id = db.Column(db.Integer,db.ForeignKey('inventory.id'))
	inventory = db.relationship('Inventory', backref=db.backref('posts', lazy='dynamic'))
	price = db.Column(db.Integer, nullable=False)
	quantityOrdered = db.Column(db.Integer, nullable=False)
	def __init__(self, user_id, item_id, price, quantityOrdered):
		self.user_id = user_id
		self.item_id = item_id
		self.price = price
		self.quantityOrdered = quantityOrdered
	def __repr__(self):
		return '<Ordered %r>' % self.id
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id'                : self.id,
			'user_id'           : self.user_id,
			'item_id'           : self.item_id,
			'price'             : self.price,
			'quantityOrdered'   : self.quantityOrdered
		}