# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2007 PRONEXO (<https://www.pronexo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale Order Line Add Product EAN13',
    'version': '11.0.0.0.1',
    'license': 'AGPL-3',
    'author': 'pronexo.com',
    'website': 'https://www.pronexo.com',
    'category':	'Sales Management',
    'complexity': 'normal',
    'depends':	[
        'sale',

    ],
    'data': [
        'views/sale_order.xml',
    ],
    'images': [
        'static/description/number_codebar_order_sale.png',
    ],
}