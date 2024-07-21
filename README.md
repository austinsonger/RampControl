# RampControl


The RampControl is designed to manage and track security compliance in accordance with FedRAMP requirements. It enables users to add new system security plans and manage Plan of Action and Milestones (POA&M) entries. The application also provides functionalities to produce exports in OSCAL (Open Security Controls Assessment Language) formats, which is a standardized format for documenting security controls and assessments.

## Functionality  

### System Security Plan (SSP)

- Users can navigate to the "Systems" section and add new systems by providing essential details such as CSP name, CSO name, FedRAMP package ID, service model (e.g., IaaS, PaaS, SaaS), Digital Identity Level (DIL) determination, FIPS PUB 199 level, fully operational date, deployment model (e.g., public cloud, hybrid cloud), authorization path (e.g., Joint Authorization Board, Provisional Authorization), and a general system description.


```
rampcontrol-evidence:
  named-evidence: location
rampcontrol-dependent-on:
  - control-id:
    profile:
reviewed-by:
  - named:
    date:
rampcontrol-fedramp-props:
  control-origination:
    - Service provider Corporate
    - Service provider System Specific
    - Service Provider Hybrid (Corporate and System Specific)
    - Configured by Customer (Customer System Specific) 
    - Provided by Customer (Customer System Specific)
    - Shared (Service Provider and Customer Responsibility)
    - Inherited from pre-existing FedRAMP Authorization [Enter text here], Date of Authorization 
  implementation-status:
    - Implemented
    - Partially implemented
    - Planned
    - Alternative implementation
    - Not Applicable
  responsible-roles:
```


### POA&M Management
- Create and Update POA&M Entries: Users can navigate to the "POA&M" section to add new entries or update existing ones. Each entry includes basic information such as the system name, date identified, control identifier, deviation types (functional, operational, risk assessment), detailed findings, action plans, and milestones.
- View Existing Entries: The application displays existing POA&M entries for a selected system, allowing users to choose whether to create a new entry or update an existing one.

## Key Components of OSCAL
- Catalogs: Define security controls.
- Profiles: Tailor controls to specific needs.
- Component Definitions (CDEF): Supplier-provided documentation describing how a component that is a building block of a larger information system can be used to implement controls.
- System Security Plans (SSP): Document how controls are implemented.
- Assessment Plans (SAP): Define how assessments are conducted.
- Assessment Results (SAR): Document the outcomes of assessments.
- Plan of Action and Milestones (POA&M): Track issues and remediation plans.

**Workflow for Responsibility Modeling in OSCAL**

- CSP has PROVIDED a capability.
- CSP explains what may be inherited in a description.
- CSP defines the RESPONSIBLE-ROLE for inheriting.
- CSP also defines the RESPONSIBILITIY associated with the PROVIDED capability.
- CSP links the RESPONSIBILITY to the PROVIDED capability.
- CUSTOMER will INHERIT as desired.
- The CUSTOMER INHERITED description may be a verbatim copy from the CSP.
- The INHERITED capability will be LINKED to the CSP by UUID from the CSP.
- CUSTOMER will explain SATISFACTION of any RESPONSIBILITY associated with the INHERITED CAPABILITY.


**Critical Elements**
Critical Elements

The following information will be REQUIRED to communicate capabilities provided, or a responsibilities shared:

- Export: Provided
- Export: Responsibilities
- Responsibility: Responsible-Role
- UUIDs from SSP related to Provided Capabilities
- Originating SSP UUID
- Implementation Status



## User Interface
- Forms for Data Entry: Intuitive forms for adding and updating system information, POA&M entries, and security controls.
- Search and Filter Capabilities: Easy search and filter options to locate existing entries and systems.
- Dashboard: Overview dashboard displaying key metrics and statuses of systems, POA&M entries, and security controls.


### Dashboard

![](/docs/poam/Dashboard.png)




### Security Controls

![](/docs/securitycontrols/ecurity%20Controls.png)



### POA&M

![](/docs/poam/POA&M%20-%20Open.png)


![](/docs/poam/POA&M%20-%20Closed.png)


![](/docs/poam/POA&M%20-%20Deviation%20Request%20-%20OR.png)


![](/docs/poam/POA&M%20-%20Deviation%20Request%20-%20FP.png)



## Backend API
- Data Validation and Storage: Handles data validation to ensure consistency and accuracy before storing in the database.
- CRUD Operations: Manages Create, Read, Update, and Delete operations for systems, POA&M entries, security controls, and sources.

## Database Schema
- Systems Table: Stores details about the security systems plans being added.
- POAM Table: Stores entries related to Plan of Action and Milestones (POA&M) for each system.
- SecurityControls Table: Stores details about the security controls, including implementation status and responsible roles.
- Sources Table: Stores information about different sources used for security assessments.

## OSCAL Exports
- Export Functionality: Allows exporting of data in OSCAL format for use in compliance documentation.








## Project Structure

```
AssureFlow/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── manage_systems.html
│   │   ├── manage_poam.html
│   │   ├── manage_sources.html
│   │   ├── manage_security_controls.html
│   ├── static/
│   │   ├── styles.css
│   │   ├── uswds.min.css (if not using CDN)
│   │   ├── uswds.min.js (if not using CDN)
│   │   ├── htmx.min.js (if not using CDN)
│   │   ├── fonts/
│   │   ├── img/
│
├── migrations/
│
├── tests/
│   ├── test_export_oscal.py
│
├── venv/
│
├── config.py
│
├── run.py
│
├── requirements.txt
│
└── README.md

```






