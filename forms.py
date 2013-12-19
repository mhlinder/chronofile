from flask.ext.wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import Required, Optional
from werkzeug.datastructures import MultiDict

class MainForm(Form):
    rectype = SelectField(u'Record Type',
            choices=[
                (None,u'Record Type'),
                ('book',u'Book'),
                ('beverage',u'Beverage')],
            validators=[Required()])

    book_title = StringField(u'Book Title', validators=[Optional()])
    book_author = StringField(u'Book Author', validators=[Optional()])

    bevtype = SelectField(u'Beverage Type',
            choices=[
                ('bevtype',u'Record Type'),
                ('redbull',u'Redbull'),
                ('espresso',u'Espresso'),
                ('water',u'Water'),
                ('protein_shake',u'Protein Shake')],
            validators=[Optional()])
    bevtype_other = StringField(u'Other Beverage', validators=[Optional()])
