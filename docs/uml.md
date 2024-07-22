```
classDiagram
    class SSP {
        +uuid: UUID
        +metadata: Metadata
        +system-characteristics: SystemCharacteristics
        +system-security-plan: SystemSecurityPlan
    }
    class Profile {
        +uuid: UUID
        +metadata: Metadata
        +imports: Imports
        +merge: Merge
    }
    class Component {
        +uuid: UUID
        +metadata: Metadata
        +components: Components
    }
    class POAM {
        +uuid: UUID
        +metadata: Metadata
        +poams: POAMs
    }
    class Catalog {
        +uuid: UUID
        +metadata: Metadata
        +params: Parameters
        +controls: Controls
    }
    class AssessmentPlan {
        +uuid: UUID
        +metadata: Metadata
        +plan: Plan
    }
    class AssessmentResults {
        +uuid: UUID
        +metadata: Metadata
        +results: Results
    }
    class Metadata {
        +title: String
        +published: DateTime
        +last-modified: DateTime
        +version: String
        +oscal-version: String
    }
    class SystemCharacteristics {
        +system-name: String
        +system-description: String
        +security-sensitivity-level: String
    }
    class SystemSecurityPlan {
        +system-implementation: SystemImplementation
        +system-information: SystemInformation
    }
    class Imports {
        +href: URI
    }
    class Merge {
        +method: String
    }
    class Components {
        +component: Component
    }
    class POAMs {
        +poam: POAM
    }
    class Parameters {
        +param: Parameter
    }
    class Controls {
        +control: Control
    }
    class Plan {
        +tasks: Tasks
    }
    class Results {
        +findings: Findings
    }
    class SystemImplementation {
        +implementation-details: String
    }
    class SystemInformation {
        +system-roles: SystemRoles
    }
    class SystemRoles {
        +role: Role
    }
    class Role {
        +role-id: String
        +role-name: String
    }
    class Tasks {
        +task: Task
    }
    class Findings {
        +finding: Finding
    }
    class Parameter {
        +id: String
        +description: String
    }
    class Control {
        +id: String
        +description: String
    }
    class Task {
        +task-id: String
        +task-name: String
    }
    class Finding {
        +finding-id: String
        +description: String
    }

    SSP o-- Metadata
    SSP o-- SystemCharacteristics
    SSP o-- SystemSecurityPlan
    Profile o-- Metadata
    Profile o-- Imports
    Profile o-- Merge
    Component o-- Metadata
    Component o-- Components
    POAM o-- Metadata
    POAM o-- POAMs
    Catalog o-- Metadata
    Catalog o-- Parameters
    Catalog o-- Controls
    AssessmentPlan o-- Metadata
    AssessmentPlan o-- Plan
    AssessmentResults o-- Metadata
    AssessmentResults o-- Results
    SystemSecurityPlan o-- SystemImplementation
    SystemSecurityPlan o-- SystemInformation
    SystemInformation o-- SystemRoles
    SystemRoles o-- Role
    Plan o-- Tasks
    Results o-- Findings
    Tasks o-- Task
    Findings o-- Finding
```
