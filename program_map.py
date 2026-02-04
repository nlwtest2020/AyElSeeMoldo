PROGRAM_MAP = {

    # =====================
    # REVENUE
    # =====================
    410000: {"category": "tuition_revenue", "type": "revenue"},
    421000: {"category": "grants_non_federal", "type": "revenue"},
    423000: {"category": "rental_revenue", "type": "revenue"},
    442000: {"category": "miscellaneous_income", "type": "revenue"},

    # =====================
    # EXPENSES — PAYROLL & PEOPLE
    # =====================
    510100: {"category": "salaries_non_us", "type": "expense"},
    510120: {"category": "post_differential_bonus", "type": "expense"},
    510150: {"category": "severance_pay", "type": "expense"},
    510300: {"category": "leave_non_us_payroll", "type": "expense"},
    517550: {"category": "fringe_benefits_allocation", "type": "expense"},
    517650: {"category": "other_taxes_licenses", "type": "expense"},
    518000: {"category": "honoraria", "type": "expense"},
    518200: {"category": "staff_training", "type": "expense"},
    519000: {"category": "per_diem", "type": "expense"},

    # =====================
    # EXPENSES — TRAVEL
    # =====================
    520500: {"category": "travel_staff", "type": "expense"},
    520600: {"category": "travel_consultant_non_staff", "type": "expense"},
    520700: {"category": "business_meals", "type": "expense"},
    621500: {"category": "participant_travel", "type": "expense"},

    # =====================
    # EXPENSES — PROGRAM & DELIVERY
    # =====================
    611000: {"category": "education_materials_books", "type": "expense"},
    660550: {"category": "teaching_materials", "type": "expense"},
    667000: {"category": "tuition_expenses", "type": "expense"},
    667200: {"category": "room_board", "type": "expense"},

    # =====================
    # EXPENSES — FACILITIES & OPERATIONS
    # =====================
    664000: {"category": "room_rental", "type": "expense"},
    670000: {"category": "office_rental", "type": "expense"},
    686300: {"category": "repairs_maintenance", "type": "expense"},

    # =====================
    # EXPENSES — IT / EQUIPMENT / SUPPLIES
    # =====================
    668000: {"category": "expendable_equipment_software", "type": "expense"},
    668500: {"category": "equipment_rental", "type": "expense"},
    680000: {"category": "supplies", "type": "expense"},
    680100: {"category": "subscriptions", "type": "expense"},
    680200: {"category": "books", "type": "expense"},
    683000: {"category": "copying", "type": "expense"},
    684000: {"category": "printing", "type": "expense"},
    677000: {"category": "postage", "type": "expense"},
    678000: {"category": "shipping", "type": "expense"},

    # =====================
    # EXPENSES — COMMS / SERVICES
    # =====================
    673000: {"category": "telephone", "type": "expense"},
    673600: {"category": "email_internet", "type": "expense"},

    # =====================
    # EXPENSES — ADMIN / OTHER
    # =====================
    526000: {"category": "staff_visas", "type": "expense"},
    630000: {"category": "bank_charges", "type": "expense"},
    640100: {"category": "cultural_enrichment", "type": "expense"},
    653000: {"category": "conference_expenses", "type": "expense"},
    674060: {"category": "dues_memberships", "type": "expense"},
    674110: {"category": "fines_penalties", "type": "expense"},
    691000: {"category": "audit", "type": "expense"},
    693000: {"category": "bank_charges", "type": "expense"},
    694000: {"category": "advertising", "type": "expense"},
    697000: {"category": "consultants", "type": "expense"},
    697100: {"category": "administrative_support", "type": "expense"},
    698100: {"category": "indirect_costs", "type": "expense"},

    # =====================
    # EXPENSES — PAYROLL (ADDITIONAL)
    # =====================
    517630: {"category": "tax_withholding_expenses", "type": "expense"},

    # =====================
    # KNOWN ZEROING ERROR — IGNORE
    # =====================
    510000: {"category": "ignore", "type": "ignore"},
}
