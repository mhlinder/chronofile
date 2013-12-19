from flask import Flask, render_template, request, redirect, url_for, flash
from forms import MainForm
from utils import *
from time import asctime

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    if request.method == 'POST' and form.validate_on_submit():
        db = get_db()
        posts = db.posts

        post = {
                "rectype": str(form.rectype.data),
                "book_title": str(form.book_title.data),
                "book_author": str(form.book_author.data),
                "bevtype": str(form.bevtype.data),
                "bevtype_other": str(form.bevtype_other.data),
                "time": asctime()
                }

        if post['bevtype'] == 'bevtype':
            post['bevtype'] = ""

        posts.insert(post)
        flash('Successfully saved!')
    return render_template('index.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)
