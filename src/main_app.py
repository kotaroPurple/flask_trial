
from datetime import datetime

import sqlalchemy
from flask import (render_template, request)

from core.app import (app, db)
from core.models import (Customer, Item, Purchase)


# top page
@app.route("/")
def index():
    customers = Customer.query.all()
    return render_template("1_index.html", customers=customers)


# 商品登録
@app.route("/item")
def item():
    return render_template("2_item.html")


# 購入登録
@app.route("/purchase")
def purchase():
    customers = Customer.query.all()
    items = Item.query.all()
    return render_template("3_purchase.html", customers=customers, items=items)


# チェックボックス等
@app.route("/trial")
def trial():
    members = ['北海道', '東京', '京都']
    genre_list = ['中華', '和食', 'イタリアン', 'フレンチ', 'アメリカン']
    return render_template("trial.html", members=members, genre_list=genre_list)


# 機能系
# 1.1 顧客登録
@app.route("/add_customer", methods=["POST"])
def add_customer():
    customer_id = request.form["input-customer-id"]
    customer_name = request.form["input-customer-name"]
    customter_age = request.form["input-age"]
    customer_gender = request.form["input-gender"]
    gender = (customer_gender == '女性')

    customer = Customer(
        customer_id=customer_id,
        customer_name=customer_name,
        age=customter_age,
        gender=gender)

    try:
        db.session.add(customer)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return render_template("error.html")

    return render_template("1-1_confirm_added_customer.html", customer=customer)


# 2.1 商品登録
@app.route("/add_item", methods=["POST"])
def add_item():
    item_name = request.form["input-item-name"]
    price = request.form["input-price"]

    item = Item(
        item_name=item_name,
        price=price)

    try:
        db.session.add(item)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return render_template("error.html")

    return render_template("2-1_confirm_added_item.html", item=item)


# 3.1 購入情報登録
@app.route("/add_purchase", methods=["POST"])
def add_purchase():
    customer_name = request.form["input-customer-name"]

    # item_name1 = request.form["input-item-name1"]
    # quantity1 = request.form["input-quantity1"]
    date = request.form["input-date"]
    date = datetime.strptime(date, "%Y-%m-%d")

    customer = Customer.query.filter_by(customer_name=customer_name).first()
    purchase = Purchase(
        customer_id=customer.customer_id,
        date=date)

    try:
        db.session.add(purchase)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return render_template("error.html")

    return render_template("3-1_confirm_purchase.html", purchase=purchase)


# GUI Trial
@app.route("/trial_function", methods=['POST'])
def trial_function():
    # チェックされたチェックボックスの値を取得
    selected_members = request.form.getlist('input_members')
    genres = request.form.getlist('input_genres')

    if selected_members:
        # 取得した値を処理（ここでは単に表示）
        return f"選択されたメンバー: {', '.join(selected_members)}" + ' : ' + ', '.join(genres)
    else:
        return "メンバーが選択されていません。"


if __name__ == '__main__':
    app.run(debug=True)
