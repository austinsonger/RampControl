

# POAM Sequence

!()[src/POAM-Sequence.png]





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



## Add or Update POAM

```
flowchart TD
    A[Select System] --> B[Existing Entries Check]
    B --> |Create New| C[Initiate Entry Creation]
    B --> |Update Existing| D[Update Entry]
    C --> E[Input Basic Information]
    E --> F[Identify Deviations]
    F --> G[Details of Findings]
    G --> H[Action Plan]
    H --> I[Milestones]
    I --> J[Review and Save]
``



