from flask import Flask, render_template

app = Flask(__name__)

# Пример данных
categories = {
    'clothes': {
        'name': 'Одежда',
        'products': [
            {'id': 1, 'name': 'Куртка'},
            {'id': 2, 'name': 'Футболка'}
        ]
    },
    'shoes': {
        'name': 'Обувь',
        'products': [
            {'id': 3, 'name': 'Кроссовки'},
            {'id': 4, 'name': 'Ботинки'}
        ]
    }
}

products = {
    1: {'name': 'Куртка', 'price': 5000, 'description': 'Теплая зимняя куртка.'},
    2: {'name': 'Футболка', 'price': 1000, 'description': 'Легкая летняя футболка.'},
    3: {'name': 'Кроссовки', 'price': 3000, 'description': 'Удобные беговые кроссовки.'},
    4: {'name': 'Ботинки', 'price': 4000, 'description': 'Кожаные ботинки.'}
}

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/category/<category_name>')
def show_category(category_name):
    category = categories.get(category_name)
    if category:
        return render_template('category.html', category_name=category['name'], products=category['products'])
    return "Категория не найдена", 404

@app.route('/product/<int:product_id>')
def show_product(product_id):
    product = products.get(product_id)
    if product:
        return render_template('product.html', product=product)
    return "Товар не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
