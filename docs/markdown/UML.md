



```
classDiagram
    class Systems {
        +Integer id
        +String csp_name
        +String cso_name
        +String fedramp_package_id
        +String service_model
        +String dil_determination
        +String fips_pub_199_level
        +Date fully_operational
        +String deployment_model
        +String authorization_path
        +String general_system_description
        +String system_name
        +String system_acronym
        +String description
        +String cloud_service_model
        +String cloud_deployment_model
        +Integer identity_assurance_level
        +Integer authenticator_assurance_level
        +Integer federation_assurance_level
        +String authorization_type
        +String security_sensitivity_level
        +String information_types
    }
    class Locations {
        +Integer id
        +Integer system_id
        +String location_type
        +String address
    }
    class Parties {
        +Integer id
        +Integer system_id
        +String role_id
        +String party_name
        +String party_description
        +String party_email
        +String party_phone
        +String party_address
    }
    class POAM {
        +Integer id
        +Integer system_id
        +Date date_identified
        +String control_identifier
        +String findings
        +String action_plan
        +String milestones
    }
    class POAM_Deviations {
        +Integer id
        +Integer poam_id
        +String deviation_type
    }
    class SecurityControls {
        +Integer id
        +String control_id
        +String control_name
        +String control_description
        +String control_implementation
        +String control_status
        +String responsible_roles
        +String control_origination
    }
    class Sources {
        +Integer id
        +String source_name
        +String source_description
    }

    Systems <|-- Locations : "1..*"
    Systems <|-- Parties : "1..*"
    Systems <|-- POAM : "1..*"
    POAM <|-- POAM_Deviations : "1..*"
```
