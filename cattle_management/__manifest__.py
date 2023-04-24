{
    "name": "Cattle Management",
    "summary": """Cattle Management System to Buy & Sell Cattle""",
    "description": """Cattle Management System to Buy & Sell Cattle""",
    "author": "Atul",
    "category": "Buy/Sale",
    "version": "15.0",
    # T00316 any module necessary for this one to work correctly
    "depends": ["base", "sale", "account", "product", "purchase", "sale_purchase"],
    # T00316 always loaded
    "data": [
        "security/ir.model.access.csv",
        "security/security_access_right.xml",
        "data/ir_sequence_data.xml",
        "views/cattle_detail_views.xml",
        "views/cattle_health_views.xml",
        "views/cattle_housing_views.xml",
        "views/cattle_milk_views.xml",
        "views/cattle_feed_views.xml",
        "views/cattle_admin_views.xml",
        "views/cattle_doctor_views.xml",
        "views/product_product_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": "True",
}
