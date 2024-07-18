from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SystemForm(FlaskForm):
    csp_name = StringField('CSP Name', validators=[DataRequired()])
    cso_name = StringField('CSO Name', validators=[DataRequired()])
    fedramp_package_id = StringField('FedRAMP Package ID', validators=[DataRequired()])
    service_model = StringField('Service Model', validators=[DataRequired()])
    dil_determination = StringField('DIL Determination', validators=[DataRequired()])
    fips_pub_199_level = StringField('FIPS PUB 199 Level', validators=[DataRequired()])
    fully_operational = DateField('Fully Operational Date', validators=[DataRequired()])
    deployment_model = StringField('Deployment Model', validators=[DataRequired()])
    authorization_path = StringField('Authorization Path', validators=[DataRequired()])
    general_system_description = TextAreaField('General System Description', validators=[DataRequired()])
    submit = SubmitField('Add System')

class POAMForm(FlaskForm):
    system_id = StringField('System ID', validators=[DataRequired()])
    date_identified = DateField('Date Identified', validators=[DataRequired()])
    control_identifier = StringField('Control Identifier', validators=[DataRequired()])
    findings = TextAreaField('Findings', validators=[DataRequired()])
    action_plan = TextAreaField('Action Plan', validators=[DataRequired()])
    milestones = TextAreaField('Milestones', validators=[DataRequired()])
    submit = SubmitField('Add POAM')

class SourceForm(FlaskForm):
    source_name = StringField('Source Name', validators=[DataRequired()])
    source_description = TextAreaField('Source Description', validators=[DataRequired()])
    submit = SubmitField('Add Source')

class SecurityControlForm(FlaskForm):
    control_id = StringField('Control ID', validators=[DataRequired()])
    control_name = StringField('Control Name', validators=[DataRequired()])
    control_description = TextAreaField('Control Description', validators=[DataRequired()])
    control_implementation = TextAreaField('Control Implementation', validators=[DataRequired()])
    control_status = StringField('Control Status', validators=[DataRequired()])
    responsible_roles = TextAreaField('Responsible Roles', validators=[DataRequired()])
    control_origination = TextAreaField('Control Origination', validators=[DataRequired()])
    submit = SubmitField('Add Security Control')
