Dist = 0
while True:
    
    Dist = float(input("Digite a qual a distância em quilometros da sua casa até o SuperMercado mais próximo: "))
    
    if Dist >= 2:
        Gasolina = Dist * 5
        print(f"O valor da gasolina será R${Gasolina:.2f}")

    elif (Dist >= 5) & (Dist < 10):
        Gasolina = Dist * 5
        print(f"O valor da gasolina será R${Gasolina:.2f}")

    elif Dist >= 10:
        Gasolina = Dist * 5
        print(f"O valor da gasolina será R${Gasolina:.2f}")

    print("Você chegou ao SuperMercado, escolha o produto que deseja comprar:")
    tabela = {"Óleo": 10.00,
            "Alho": 4.00,
            "Arroz": 9.30,
            "Farofa": 2.00,
            "Cebola": 4.99,
            "Tomate": 3.00,
            "Carne": 20.00}
    
    print(tabela)
    produto = input("Qual produto você deseja Comprar? ").capitalize()
      
    quantidade = int(input("Quantidade: "))
    valor_produto = (tabela[produto] * quantidade)
    valor_total = quantidade + valor_produto
    print(f"O valor da compra no mercado foi de: R${valor_total:.2f}")
    
    Gastos = Gasolina + valor_total
    print(f"Seus gastos ao todo foram de R${Gastos:.2f}")
    break