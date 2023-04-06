{
    "name": "Library Management",
    "author": "atul",
    "description": "library management project",
    "sequence": 0,
    "depends": ["base", "mail","sale","sale_management",],
    "data": [
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
        "security/security_access_right.xml",
        "views/readers_detail_views.xml",
        "views/library_report_views.xml",
        "views/borrow_books_views.xml",
        "views/books_detail_views.xml",
        "views/library_management_views.xml",
        "wizard/sale_order_wizard_views.xml"
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
