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

```
flowchart TD
    subgraph UI
        A1[Add System Form]
        A2[Update System Form]
        A3[Add POA&M Entry Form]
        A4[Update POA&M Entry Form]
        A5[Search Systems Form]
        A6[Search POA&M Entries Form]
    end

    subgraph BackendAPI
        B1[Add System Endpoint]
        B2[Update System Endpoint]
        B3[Add POA&M Entry Endpoint]
        B4[Update POA&M Entry Endpoint]
        B5[Search Systems Endpoint]
        B6[Search POA&M Entries Endpoint]
    end

    subgraph Database
        D1[Systems]
        D2[POAM]
    end

    A1 --> B1
    A2 --> B2
    A3 --> B3
    A4 --> B4
    A5 --> B5
    A6 --> B6

    B1 --> D1
    B2 --> D1
    B3 --> D2
    B4 --> D2
    B5 --> D1
    B6 --> D2

    click A1 "javascript:void(0)" "Add System Form"
    click A2 "javascript:void(0)" "Update System Form"
    click A3 "javascript:void(0)" "Add POA&M Entry Form"
    click A4 "javascript:void(0)" "Update POA&M Entry Form"
    click A5 "javascript:void(0)" "Search Systems Form"
    click A6 "javascript:void(0)" "Search POA&M Entries Form"
    click B1 "javascript:void(0)" "Add System Endpoint"
    click B2 "javascript:void(0)" "Update System Endpoint"
    click B3 "javascript:void(0)" "Add POA&M Entry Endpoint"
    click B4 "javascript:void(0)" "Update POA&M Entry Endpoint"
    click B5 "javascript:void(0)" "Search Systems Endpoint"
    click B6 "javascript:void(0)" "Search POA&M Entries Endpoint"
    click D1 "javascript:void(0)" "Systems"
    click D2 "javascript:void(0)" "POAM"

```



```
digraph G {
    subgraph cluster_ui {
        label = "UI";
        "Add System Form";
        "Update System Form";
        "Add POA&M Entry Form";
        "Update POA&M Entry Form";
        "Search Systems Form";
        "Search POA&M Entries Form";
    }

    subgraph cluster_backend {
        label = "Backend API";
        "Add System Endpoint";
        "Update System Endpoint";
        "Add POA&M Entry Endpoint";
        "Update POA&M Entry Endpoint";
        "Search Systems Endpoint";
        "Search POA&M Entries Endpoint";
    }

    subgraph cluster_db {
        label = "Database";
        Systems [
            label = "Systems\n- id : int\n- csp_name : varchar\n- cso_name : varchar\n- fedramp_package_id : varchar\n- service_model : varchar\n- dil_determination : varchar\n- fips_pub_199_level : varchar\n- fully_operational : date\n- deployment_model : varchar\n- authorization_path : varchar\n- general_system_description : text"
        ];
        POAM [
            label = "POAM\n- id : int\n- system_id : int\n- date_identified : date\n- control_identifier : varchar\n- deviations : varchar\n- findings : text\n- action_plan : jsonb\n- milestones : jsonb"
        ];
    }

    "Add System Form" -> "Add System Endpoint";
    "Update System Form" -> "Update System Endpoint";
    "Add POA&M Entry Form" -> "Add POA&M Entry Endpoint";
    "Update POA&M Entry Form" -> "Update POA&M Entry Endpoint";
    "Search Systems Form" -> "Search Systems Endpoint";
    "Search POA&M Entries Form" -> "Search POA&M Entries Endpoint";

    "Add System Endpoint" -> Systems;
    "Update System Endpoint" -> Systems;
    "Add POA&M Entry Endpoint" -> POAM;
    "Update POA&M Entry Endpoint" -> POAM;
    "Search Systems Endpoint" -> Systems;
    "Search POA&M Entries Endpoint" -> POAM;
}

```









