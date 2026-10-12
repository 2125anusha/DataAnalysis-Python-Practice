def apply_discount(price,discount):
    if type(price) != int and type(price) != float:
        return "The price should be a number"
    elif type(discount) != int and type(discount) != float:
        return "The discount should be a number"
    elif price<=0:
        return "The price should be greater than 0"
    elif discount>100 or discount<0:
        return "The discount should be between 0 and 100"
    else:
        discount_amount=(discount/100)*price
        total=price-discount_amount
        return total
final_price=apply_discount(100,10)
print(final_price)