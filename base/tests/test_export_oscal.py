import unittest
from app import create_app, db
from app.models import System, POAM, Source, SecurityControl

class OscalExportTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.populate_db()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def populate_db(self):
        system = System(
            csp_name="CSP1",
            cso_name="CSO1",
            fedramp_package_id="FPID1",
            service_model="IaaS",
            dil_determination="Low",
            fips_pub_199_level="Moderate",
            fully_operational="2023-01-01",
            deployment_model="Public Cloud",
            authorization_path="JAB",
            general_system_description="A description"
        )
        db.session.add(system)
        db.session.commit()

        poam = POAM(
            system_id=system.id,
            date_identified="2023-01-02",
            control_identifier="AC-1",
            findings="Finding 1",
            action_plan="Action Plan 1",
            milestones="Milestone 1"
        )
        db.session.add(poam)
        db.session.commit()

        source = Source(
            source_name="Nessus",
            source_description="Nessus Description"
        )
        db.session.add(source)
        db.session.commit()

        control = SecurityControl(
            control_id="AC-2",
            control_name="Access Control",
            control_description="Control Description",
            control_implementation="Implementation Details",
            control_status="Implemented",
            responsible_roles="Role 1",
            control_origination="Origination Details"
        )
        db.session.add(control)
        db.session.commit()

    def test_export_oscal(self):
        response = self.client.get('/export/oscal')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')

        oscal_data = json.loads(response.data)
        self.assertIn('system_security_plan', oscal_data)
        self.assertIn('poam_entries', oscal_data)
        self.assertIn('sources', oscal_data)
        self.assertIn('security_controls', oscal_data)

        self.assertEqual(len(oscal_data['system_security_plan']), 1)
        self.assertEqual(len(oscal_data['poam_entries']), 1)
        self.assertEqual(len(oscal_data['sources']), 1)
        self.assertEqual(len(oscal_data['security_controls']), 1)

if __name__ == '__main__':
    unittest.main()
