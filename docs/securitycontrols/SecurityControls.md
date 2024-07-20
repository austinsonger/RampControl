# Security Controls

- Each control must have a header describing its implementation requirements and status.
- For control origination include all that apply and delete those that do not apply. 
- Each control must have at least one responsible role.  If more than one, enter as separate list items.
- If the control origination is inherited, the uuid of the leveraged authorization must be provided.


```
  control-origination:
    - sp-corporate
    - sp-system
    - customer-configured
    - customer-provided
    - inherited: uuid of leveraged authorization
  implementation-status:
    - implemented
    - partial: describe gap
    - planned: describe plan
      completion-date: date_string
    - alternative: describe alternative
    - not-applicable: provide justification
  responsible-roles:
    - role-id
```

