# AssureFlow

The AssureFlow is designed to manage and track security compliance in accordance with FedRAMP requirements. It enables users to add new system security plans and manage Plan of Action and Milestones (POA&M) entries. The application also provides functionalities to produce exports in OSCAL (Open Security Controls Assessment Language) formats, which is a standardized format for documenting security controls and assessments.

## Functionality  

### System Security Plan (SSP)

- Users can navigate to the "Systems" section and add new systems by providing essential details such as CSP name, CSO name, FedRAMP package ID, service model (e.g., IaaS, PaaS, SaaS), Digital Identity Level (DIL) determination, FIPS PUB 199 level, fully operational date, deployment model (e.g., public cloud, hybrid cloud), authorization path (e.g., Joint Authorization Board, Provisional Authorization), and a general system description.

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











