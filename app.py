from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import cloudinary

app = Flask(__name__)

cloudinary.config(
    cloud_name = "dn3mokfxz",
    api_key = "386857267759241",
    api_secret = "jHH0hQ7vm1j-lCtkuY_qxO91JEU"
)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///newstore.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "caty123"

db = SQLAlchemy(app)
migrate = Migrate(app,db)

with app.app_context():
    from myapp.model.storeModel import Store,Item
    db.create_all()



from myapp.model.storeModel import store_bp
app.register_blueprint(store_bp)