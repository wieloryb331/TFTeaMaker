from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class UnitForm(FlaskForm):
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    cost = IntegerField('cost', validators=[DataRequired()])
    class1 = StringField('class1',
                           validators=[DataRequired(), Length(min=2, max=20)])
    class2 = StringField('class2',
                           validators=[DataRequired(), Length(min=2, max=20)])
    class3 = StringField('class3',
                         validators=[Length(min=0, max=20)])
    
    submit = SubmitField("Create")