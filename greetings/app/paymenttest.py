import stripe

stripe.api_key = "sk_test_51L2zmwKwkYYi9AWLSIJsVOufhWiaJ9t3rL9cPufq26GT74DhaYZhzR7KbXIJt1xIUEMhj6ubmMXMSdFhgYvjTBZv00M5KxgZ8n"


#a = stripe.PaymentIntent.list(limit=500)

b = stripe.checkout.Session.list(limit=10)

customer_id = b.data[2]['id']

for items in b:
    customer_id = b.data[2]['id']
    print(b)
    line_items = stripe.checkout.Session.list_line_items(customer_id, limit=5)
    print(line_items.data[0]['description'])



