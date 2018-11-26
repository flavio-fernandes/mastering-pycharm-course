from pyramid.view import view_config

import fake_data


@view_config(route_name='home', renderer="templates/mytemplate.pt")
def my_view(_):
    orders = fake_data.get_orders()
    return {
        'project': 'Demo project from PyCharm!',
        'orders': orders,
    }
