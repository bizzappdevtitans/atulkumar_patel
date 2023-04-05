{
    "name": "Sale Inheritance",
    "summary": """sale inheritance""",
    "description": """sale module""",
    "author": "Atul",
    "category": "Sales/Sales",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["sale","sale_management","stock","mrp","product","purchase","account","resource","sale_project"],
    # always loaded
    "data": [
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
        "security/security_access_right.xml",
        "views/sale_views.xml",
        "views/account_move_views.xml",
        "views/stock_picking_views.xml",
        "views/mrp_production_views.xml",
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "views/introduction_text_views.xml",
        "views/closing_text_views.xml",
        "views/product_product_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": "True",
}
