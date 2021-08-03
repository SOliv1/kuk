from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
@register.filter()
def currency(value):
    currency_in = 'lb'
    currency_out = 'USD'
    import urllib2
    req = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s='+currency_in+currency_out+'=X')
    result = req.read()