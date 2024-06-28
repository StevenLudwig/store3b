from rest_framework import exceptions


def product_not_found():  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'product_001',
                'message': 'Invalid product_id, product not found.'
            }
        },
        code='product_not_found'
    )


def out_of_stock(sku, name):  # 400
    return exceptions.ValidationError(
        detail={
            'error': {
                'code': 'inventory_001',
                'message': f'Product {name}/{sku} out of stock.'
            }
        },
        code='out_of_stock'
    )
