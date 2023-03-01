# Copyright 2023 Leonardo J. Caballero G.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Sales Quotations Custom',
    'description': """
        A Sales Quotations View Custom. This module is part of the
        Introduction To Owl and JavaScript with Odoo v15 from Oocademy.

        https://www.oocademy.com/v15.0/tutorial/introduction-to-owl-115
    """,
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Leonardo J. Caballero G.',
    'website': 'https://github.com/macagua',
    'category': 'Tutorials',
    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'data': [
        'views/sales_order_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sales_quotations_custom/static/src/components/PartnerOrderSummary/partner_order_summary.js',
        ],
        'web.assets_qweb': [
            'sales_quotations_custom/static/src/components/PartnerOrderSummary/partner_order_summary.xml',
        ],
    },
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
}
