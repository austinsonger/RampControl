# Components:

## User Interface (UI):
- Provides forms for adding and updating system information.
- Forms for adding and updating POA&M entries.
- Search and filter capabilities to locate existing entries.

## Backend API:
- Handles data validation and storage.
- Manages CRUD (Create, Read, Update, Delete) operations for systems and POA&M entries.


## Database:
- Stores system and POA&M entries with all related details.
- Example schema for systems and POA&M entries:

```sql
-- Create table for storing systems
CREATE TABLE Systems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    csp_name TEXT NOT NULL,
    cso_name TEXT NOT NULL,
    fedramp_package_id TEXT NOT NULL,
    service_model TEXT NOT NULL,
    dil_determination TEXT NOT NULL,
    fips_pub_199_level TEXT NOT NULL,
    fully_operational DATE NOT NULL,
    deployment_model TEXT NOT NULL,
    authorization_path TEXT NOT NULL,
    general_system_description TEXT NOT NULL
);

-- Create table for storing POA&M entries
CREATE TABLE POAM (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    system_id INTEGER NOT NULL,
    date_identified DATE NOT NULL,
    control_identifier TEXT NOT NULL,
    deviations TEXT NOT NULL,
    findings TEXT NOT NULL,
    action_plan TEXT NOT NULL, -- JSON encoded string for action plan details
    milestones TEXT NOT NULL,  -- JSON encoded string for milestones details
    FOREIGN KEY (system_id) REFERENCES Systems(id)
);

-- Create table for storing Security Controls
CREATE TABLE SecurityControls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    control_id TEXT NOT NULL,
    control_name TEXT NOT NULL,
    control_description TEXT NOT NULL,
    control_implementation TEXT NOT NULL, -- JSON encoded string for implementation details
    control_status TEXT NOT NULL,
    responsible_roles TEXT NOT NULL, -- JSON encoded string for roles responsible
    control_origination TEXT NOT NULL -- JSON encoded string for origination details
);

-- Create table for storing sources
CREATE TABLE Sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_name TEXT NOT NULL,
    source_description TEXT NOT NULL
);

```





