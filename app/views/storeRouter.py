import cloudinary.uploader
from app.model.storeModel import Store,Item
from _init_ import db
from flask import Blueprint,request,jsonify
import cloudinary

store_bp = Blueprint("store_bp",__name__,url_prefix="/api/v1")


@store_bp.route("/create_store", methods=['POST'])
def create_store():
    store_data = request.get_json()
    store_name = store_data["name"]

    if Store.query.filter_by(name=store_name).first():
        return jsonify({"message":"Store already exists"}), 400
    
    new_store = Store(name=store_name)
    db.session.add(new_store)
    db.session.commit()

    return jsonify(new_store.to_dict()),201


@store_bp.route("/getonestore/<int:store_id>",methods=['GET'])
def get_store(store_id):
    store = Store.query.get(store_id)

    if not store:
        return jsonify({"message":"Store not found"}),404
    return jsonify({
        "message":"Store gotten successfully",
        "id": store.id,
        "name":store.name,
        "items": [item.to_dict() for item in store.items]
    }),200


@store_bp.route("/add_an_item/<int:store_id>/item",methods=['POST'])
def add_item(store_id):
    store = Store.query.get(store_id)

    if not store:
        return jsonify({"message":"Store not found"}),404
    
    store_data = request.get_json()
    item_name = store_data["name"]
    item_price = store_data["price"]

    existing_item = Item.query.filter_by(name = item_name, store_id=store_id).first()

    if existing_item:
        return jsonify({"message":"Item already exists in this store"}),404
    
    if 'item_image' not in request.files:
        return jsonify({"message":"No file path"}),400
    
    file = request.files['item_image']
    

    if file.filename == "":
        return jsonify({"message":"No selected file"}),400
    
    if file:
        upload_result = cloudinary.uploader.upload(file)
        image_url = upload_result.get("secure_url")
    
    new_item =  Item(name = item_name,price=item_price,store_id=store_id,item_image=image_url)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({
        "message":"Item added successfully",
        "id": store.id,
        "name":store.name,
        "items": [item.to_dict() for item in store.items]
    }),200


@store_bp.route("/getallstores",methods=['GET'])
def getallUsers():
    store = Store.query.all()
 
    jsonify({"message":"Gotten successflly","store":[stores.to_dict for stores in store]})