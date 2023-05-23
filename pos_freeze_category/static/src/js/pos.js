odoo.define('pos_freeze_category.FixedProductControlWidget', function(require) {
    'use strict';

    const { useState } = owl.hooks;
    const ProductsWidget = require('point_of_sale.ProductsWidget');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    const FixedProductControlWidget = ProductsWidget =>
        class extends ProductsWidget {
            get subcategories() {
                return this.env.pos.db
                    .get_category_childs_ids(0)
                    .map(id => this.env.pos.db.get_category_by_id(id));
            }
        };

    Registries.Component.extend(ProductsWidget, FixedProductControlWidget);

    return ProductsWidget;
});
