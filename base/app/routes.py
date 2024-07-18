import json
from flask import url_for, flash, redirect, request, send_file, make_response
from flask import Blueprint, render_template
from io import BytesIO
from . import db
from .models import System, POAM, Source, SecurityControl
from .forms import SystemForm, POAMForm, SourceForm, SecurityControlForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/systems', methods=['GET', 'POST'])
def manage_systems():
    form = SystemForm()
    if form.validate_on_submit():
        system = System(
            csp_name=form.csp_name.data,
            cso_name=form.cso_name.data,
            fedramp_package_id=form.fedramp_package_id.data,
            service_model=form.service_model.data,
            dil_determination=form.dil_determination.data,
            fips_pub_199_level=form.fips_pub_199_level.data,
            fully_operational=form.fully_operational.data,
            deployment_model=form.deployment_model.data,
            authorization_path=form.authorization_path.data,
            general_system_description=form.general_system_description.data
        )
        db.session.add(system)
        db.session.commit()
        if request.headers.get('HX-Request'):
            return render_template('manage_systems.html', form=form, systems=System.query.all())
        flash('System added successfully!', 'success')
        return redirect(url_for('main.manage_systems'))
    systems = System.query.all()
    return render_template('manage_systems.html', form=form, systems=systems)

@main.route('/poam', methods=['GET', 'POST'])
def manage_poam():
    form = POAMForm()
    if form.validate_on_submit():
        poam = POAM(
            system_id=form.system_id.data,
            date_identified=form.date_identified.data,
            control_identifier=form.control_identifier.data,
            findings=form.findings.data,
            action_plan=form.action_plan.data,
            milestones=form.milestones.data
        )
        db.session.add(poam)
        db.session.commit()
        if request.headers.get('HX-Request'):
            return render_template('manage_poam.html', form=form, poams=POAM.query.all())
        flash('POAM entry added successfully!', 'success')
        return redirect(url_for('main.manage_poam'))
    poams = POAM.query.all()
    return render_template('manage_poam.html', form=form, poams=poams)

@main.route('/sources', methods=['GET', 'POST'])
def manage_sources():
    form = SourceForm()
    if form.validate_on_submit():
        source = Source(
            source_name=form.source_name.data,
            source_description=form.source_description.data
        )
        db.session.add(source)
        db.session.commit()
        if request.headers.get('HX-Request'):
            return render_template('manage_sources.html', form=form, sources=Source.query.all())
        flash('Source added successfully!', 'success')
        return redirect(url_for('main.manage_sources'))
    sources = Source.query.all()
    return render_template('manage_sources.html', form=form, sources=sources)

@main.route('/security_controls', methods=['GET', 'POST'])
def manage_security_controls():
    form = SecurityControlForm()
    if form.validate_on_submit():
        control = SecurityControl(
            control_id=form.control_id.data,
            control_name=form.control_name.data,
            control_description=form.control_description.data,
            control_implementation=form.control_implementation.data,
            control_status=form.control_status.data,
            responsible_roles=form.responsible_roles.data,
            control_origination=form.control_origination.data
        )
        db.session.add(control)
        db.session.commit()
        if request.headers.get('HX-Request'):
            return render_template('manage_security_controls.html', form=form, controls=SecurityControl.query.all())
        flash('Security Control added successfully!', 'success')
        return redirect(url_for('main.manage_security_controls'))
    controls = SecurityControl.query.all()
    return render_template('manage_security_controls.html', form=form, controls=controls)

@main.route('/export/oscal', methods=['GET'])
def export_oscal():
    systems = System.query.all()
    poams = POAM.query.all()
    sources = Source.query.all()
    controls = SecurityControl.query.all()

    oscal_data = {
        "system_security_plan": [],
        "poam_entries": [],
        "sources": [],
        "security_controls": []
    }

    for system in systems:
        oscal_data["system_security_plan"].append({
            "csp_name": system.csp_name,
            "cso_name": system.cso_name,
            "fedramp_package_id": system.fedramp_package_id,
            "service_model": system.service_model,
            "dil_determination": system.dil_determination,
            "fips_pub_199_level": system.fips_pub_199_level,
            "fully_operational": str(system.fully_operational),
            "deployment_model": system.deployment_model,
            "authorization_path": system.authorization_path,
            "general_system_description": system.general_system_description
        })

    for poam in poams:
        oscal_data["poam_entries"].append({
            "system_id": poam.system_id,
            "date_identified": str(poam.date_identified),
            "control_identifier": poam.control_identifier,
            "findings": poam.findings,
            "action_plan": poam.action_plan,
            "milestones": poam.milestones
        })

    for source in sources:
        oscal_data["sources"].append({
            "source_name": source.source_name,
            "source_description": source.source_description
        })

    for control in controls:
        oscal_data["security_controls"].append({
            "control_id": control.control_id,
            "control_name": control.control_name,
            "control_description": control.control_description,
            "control_implementation": control.control_implementation,
            "control_status": control.control_status,
            "responsible_roles": control.responsible_roles,
            "control_origination": control.control_origination
        })

    json_data = json.dumps(oscal_data, indent=4)
    buffer = BytesIO()
    buffer.write(json_data.encode('utf-8'))
    buffer.seek(0)

    response = make_response(send_file(buffer, mimetype='application/json', as_attachment=True, download_name='oscal_export.json'))
    return response
