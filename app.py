from flask import Flask, render_template, request,redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'chave-secreta-aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/youtube'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.String(100))
    email = db.Column(db.String(100))


@app.route("/")
def index():
    lista=User.query.all()
    return render_template('index.html',lista=lista)


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method =='POST':
        nome = request.form['nome']
        idade = request.form['idade']
        email =request.form['email']
        novo_usuario = User(nome=nome, idade=idade, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('adiciona.html')

@app.route('/read/<int:id>')
def read(id):
    user = User.query.get(id)
    return render_template('update.html', user=user)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.nome = request.form['nome']
        user.idade= request.form['idade']
        user.email = request.form['email']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', user=user)
    
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')
    
    
    
    
    
if __name__=='__main__':
   app.run(debug=True) 