def loose_change(cantidad_introducida:int=0) -> dict:
    resto_cantidad = cantidad_introducida
    llave_moneda = ["Quarters", "Dimes", "Pennies", "Nickels"]
    valor_moneda = [25, 10, 5, 1]

    moneda_dict = dict(zip(llave_moneda, valor_moneda))
    cambio = {}
    for llave, valor in moneda_dict.items():
        cambio[llave] = resto_cantidad // valor
        resto_cantidad -= cambio[llave]
    
    return cambio



if __name__ == "__main__":

    print(loose_change(29))

    assert loose_change() == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) ==  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}