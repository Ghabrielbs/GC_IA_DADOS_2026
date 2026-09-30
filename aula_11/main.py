import random

cardapio = {
    "chocolate": 5.00,
    "baunilha": 4.50,
    "morango": 3.00,
    "flocos": 9.00,
}

brindes = ["canudo","copo personalizado","gelo","badge"]

def mostrar_cardapio():
    print("--cardapio de sorvetes--")
    for sabor, preco in cardapio.items():
        print(f"{sabor}: R${preco:.2f}")


def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor_escolhido = input("\n Digite o sabor do sorvete que deseja (ou 'sair' para finalizar):")
        if sabor_escolhido == "sair":
            break
        elif sabor_escolhido in cardapio:
            total += cardapio[sabor_escolhido]
            pedido.append(sabor_escolhido)
            print(f"{sabor_escolhido} adicionado ao pedido!. Total: R${total:.2f}")
        else:
            print("sabor não está no cardapio.")
    return pedido, total   

mostrar_cardapio()  
pedido, total = fazer_pedido()

print(f"\n Seu pedido: {pedido}")
print(f"Total a pagar: R${total:.2f}")

if total>15:
    print(f"Parabéns! Você ganhou um brinde: {random.choice(brindes)}")