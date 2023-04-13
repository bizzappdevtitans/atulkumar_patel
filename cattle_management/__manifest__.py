{
    "name": "Cattle Management",
    "summary": """Cattle Management System to Buy & Sell Cattle""",
    "description": """Cattle Management System to Buy & Sell Cattle""",
    "author": "Atul",
    "category": "Buy/Sale",
    "version": "15.0",
    # T00316 any module necessary for this one to work correctly
    "depends": ["base", "sale_management", "purchase"],
    # T00316 always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/cattle_administrator_views.xml",
        "views/cattle_buyer_views.xml",
        "views/cattle_detail_views.xml",
        "views/cattle_seller_views.xml",
        "views/registration_detail_views.xml",
        "views/cattle_payment_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": "True",
}
