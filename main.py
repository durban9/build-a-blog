from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(700))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/')
def index():
    return redirect('/blog')

@app.route('/blog', methods = ['GET'])
def blog():
    blogs = Blog.query.all()
    blog=request.args.get('id')
    
    
    if blog:
        blog_id = Blog.query.get(int(blog))
        return render_template('single_entry.html', blog=blog_id)

    return render_template('blogs.html', title="Build-A-Blog", blogs=blogs)
    

@app.route('/newpost', methods = ['POST', 'GET'])
def add_new_post():
   
    if request.method == 'POST':
        error_message = ''
        title = request.form['title']
        body = request.form['blog']
    
    
         
        if title == '' or body == '':
            
            error_message = "Neither text field may be left blank. Please enter a title for your blog."
            return render_template('newpost.html', title= "Blogs", error_message=error_message)
        
        elif body == '':
            
            error_message = "Body of Blog may not be left blank. Please enter a statement for the body of your blog."        
        
        else: 
        
                    blog_title = request.form['title']
                    blog = request.form['blog']
                    blog_and_title = Blog(blog_title, blog)
                    db.session.add(blog_and_title)
                    db.session.commit()
                    return redirect('/')
    return render_template('newpost.html', title="Blogs")

    
        


        
   





        

if __name__ == '__main__':
  app.run()
