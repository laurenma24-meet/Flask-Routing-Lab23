from flask import Flask, redirect, request, render_template, url_for


app = Flask( __name__,template_folder='templates',  static_folder='static' )

# Your code should be below

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/product2')
def product2():
    return render_template('product2.html')






# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
