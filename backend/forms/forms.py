from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class AddForm(FlaskForm):
    input_item = TextAreaField(
        'Add new item', 
        validators=[DataRequired()], 
        render_kw={
            "class": "form-control",
            "placeholder": \
            "enter an 'item' consisting of 1-3 arguments separated by commas"
            }
        )
    add_item = SubmitField('Add', render_kw={"class":"btn btn-primary"})

    def validate_input_item(form, field):
        try:
            split_data = list(map(lambda x: x.strip(), field.data.split(',')))
        except:
            raise ValidationError("incorrect input")
        if len(split_data) > 3:
            raise ValidationError("too many arguments")
        if split_data[0].isdigit():
            raise ValidationError("1'st argument must be string")
        if len(split_data) == 3:
            if split_data[1].isdigit() == True:
                raise ValidationError("2'nd argument must be string")
            if split_data[2].isdigit() == False:
                raise ValidationError("3'rd argument must be digit")


class SearchForm(FlaskForm):
    input_search = TextAreaField(
        'Search',
        render_kw={
            "class": "form-control",
            "placeholder": \
            "enter arguments separated by commas"
            }
        )
    search_item = SubmitField('Search', render_kw={"class":"btn btn-primary"})
