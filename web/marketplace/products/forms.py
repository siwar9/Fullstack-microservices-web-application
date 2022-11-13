from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, validators

class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price',[validators.DataRequired()])
    stock = IntegerField('Stock',[validators.DataRequired()])  
    file = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','JPG','png','PNG','gif','GIF','jpeg','JPEG'])])
    
