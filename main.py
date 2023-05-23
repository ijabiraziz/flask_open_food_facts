import openfoodfacts
from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/off', methods=['GET'])
def open_food_facts_query():
    product_name = "nestle"
    product = openfoodfacts.products.search(product_name)
    # barcode  = '8961008212289'
    # product = openfoodfacts.products.get_product(barcode)
    # print(product["product_name"])
    # for product in openfoodfacts.products.search_all("mighty zinger"):
    #     print(product,"********************************")
    #     return jsonify(product)
    return jsonify(product)

    # search_result = openfoodfacts.products.search(productname)
    # return jsonify(search_result)

if __name__ == '__main__':
    app.run(debug=True)