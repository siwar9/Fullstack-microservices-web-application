from flask import redirect,render_template,url_for,flash,request,session,current_app
from marketplace import db, app
from marketplace.products.models import Addproduct


def MagerDicts(dict1,dict2):
    if isinstance(dict1, list) and isinstance(dict2,list):
        return dict1  + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    else:
        return False

@app.route('/addcart',methods=['POST'])
def AddCart():
    try:
        product_id=request.form.get('product_id')
        quantity = request.form.get('quantity')
        product = Addproduct.query.filter_by(id=product_id).first()
        
        if request.method=="POST" and quantity and product_id:
            dict={product_id:{'name':product.name,'price':product.price, 'quantity':quantity, 'image':product.file}}
            
            if 'cart' in session:
                print(session['cart'])
                
                if product_id in session['cart']:
                    print("This item is already in cart")
                    for key, item in session['cart'].items():
                            if int(key) == int(product_id):
                                session.modified = True
                                item['quantity'] += 1

                else:
                    session['cart']=MagerDicts(session['cart'], dict)
                    return redirect(request.referrer)
            else:
                    session['cart'] = dict
                    return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@app.route('/carts')
def getCart():
    if 'cart' not in session:
        return redirect(request.referrer)
    sum=0
    for key, product in session['cart'].items():
        sum+=float(product['price'])*int(product['quantity'])  

    return render_template('products/carts.html',sum=sum)


@app.route('/deleteitem/<int:id>')
def deleteitem(id):
    if 'cart' not in session and len(session['cart']) <= 0:
        return redirect(url_for('home'))
    try:
        session.modified = True
        for key , item in session['cart'].items():
            if int(key) == id:
                session['cart'].pop(key, None)
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))

