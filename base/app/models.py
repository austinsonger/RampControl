from . import db

class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    csp_name = db.Column(db.String(100), nullable=False)
    cso_name = db.Column(db.String(100), nullable=False)
    fedramp_package_id = db.Column(db.String(50), nullable=False)
    service_model = db.Column(db.String(50), nullable=False)
    dil_determination = db.Column(db.String(50), nullable=False)
    fips_pub_199_level = db.Column(db.String(50), nullable=False)
    fully_operational = db.Column(db.Date, nullable=False)
    deployment_model = db.Column(db.String(50), nullable=False)
    authorization_path = db.Column(db.String(50), nullable=False)
    general_system_description = db.Column(db.Text, nullable=False)

class POAM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    system_id = db.Column(db.Integer, db.ForeignKey('system.id'), nullable=False)
    date_identified = db.Column(db.Date, nullable=False)
    control_identifier = db.Column(db.String(50), nullable=False)
    findings = db.Column(db.Text, nullable=False)
    action_plan = db.Column(db.Text, nullable=False)
    milestones = db.Column(db.Text, nullable=False)

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_name = db.Column(db.String(100), nullable=False)
    source_description = db.Column(db.Text, nullable=False)

class SecurityControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    control_id = db.Column(db.String(50), nullable=False)
    control_name = db.Column(db.String(100), nullable=False)
    control_description = db.Column(db.Text, nullable=False)
    control_implementation = db.Column(db.Text, nullable=False)
    control_status = db.Column(db.String(50), nullable=False)
    responsible_roles = db.Column(db.Text, nullable=False)
    control_origination = db.Column(db.Text, nullable=False)
