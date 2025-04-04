from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, FormField, FieldList, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, Optional

class ShareholderForm(FlaskForm):
    """Vorm osaniku andmete sisestamiseks."""
    shareholder_type = SelectField(
        'Osaniku tüüp',
        choices=[('physical', 'Füüsiline isik'), ('legal', 'Juriidiline isik')],
        validators=[DataRequired()]
    )
    # Füüsilise isiku andmed
    first_name = StringField(
        'Eesnimi',
        validators=[Optional(), Length(min=1, max=50)]
    )
    last_name = StringField(
        'Perenimi',
        validators=[Optional(), Length(min=1, max=50)]
    )
    personal_code = StringField(
        'Isikukood',
        validators=[Optional(), Length(min=1, max=20)]
    )
    # Juriidilise isiku andmed
    legal_name = StringField(
        'Juriidilise isiku nimi',
        validators=[Optional(), Length(min=1, max=100)]
    )
    legal_reg_code = StringField(
        'Registrikood',
        validators=[Optional(), Length(min=1, max=20)]
    )
    # Üldised osaniku andmed
    share_amount = IntegerField(
        'Osaniku osa suurus eurodes',
        validators=[DataRequired(), NumberRange(min=1, message="Osaniku osa peab olema vähemalt 1€")]
    )
    founder = BooleanField(
        'Asutaja',
        default=True,
        description="Osanik märgitakse automaatselt asutajaks"
    )

class CompanyForm(FlaskForm):
    """Vorm uue osaühingu loomise andmete sisestamiseks."""
    name = StringField(
        'Osaühingu nimi',
        validators=[DataRequired(), Length(min=3, max=100)]
    )
    reg_code = StringField(
        'Registrikood',
        validators=[DataRequired(), Regexp('^\d{7}$', message="Registrikood peab olema 7 numbrit")]
    )
    established_date = DateField(
        'Asutamiskuupäev',
        format='%Y-%m-%d',
        validators=[DataRequired()]
    )
    capital = IntegerField(
        'Kogukapital (eurodes)',
        validators=[DataRequired(), NumberRange(min=2500, message="Kogukapital peab olema vähemalt 2500€")]
    )
    # Väli osanike andmete jaoks: lubab sisestada ühe või mitu osanikku
    shareholders = FieldList(
        FormField(ShareholderForm),
        min_entries=1,
        max_entries=10,
        label="Osanikud"
    )
    submit = SubmitField('Loo osaühing')
