from app import db


class Store(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),unique=True,nullable=False)
    items = db.relationship("Item", backref ='store', lazy=True)


    def to_dict(self):
        return {
             "message":"Created Successfully",
            "id":self.id,
            "name":self.name,
            "items":[item.to_dict() for item in self.items]
        }
    
class Item(db.Model):
        id = db.Column(db.Integer,primary_key = True)
        name = db.Column(db.String(255),unique=True,nullable=False)
        price = db.Column(db.Float,nullable=False)
        item_image = db.Column(db.String(255))
        store_id = db.Column(db.Integer,db.ForeignKey('store.id'),nullable=False)


        __table_args__ = (db.UniqueConstraint("name","store_id",name="_store_item_uc"),)

        def to_dict(self):
            return {
                "id":self.id,
                "name":self.name,
                "price":self.price,
                "item_image":self.item_image
        }