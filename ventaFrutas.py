def mostrar_frutas(frutas):
    print("\nOpciones disponibles:")
    for fruta in frutas:
        print(f"- {fruta}")

def calcular_total(fruta, cantidad, precios):
    return precios[fruta] * cantidad

def main():
    precios_frutas = {
        'manzana': 1.80,
        'banana': 1.20,
        'naranja': 1.50,
        'sandia': 3.50,
        'mango': 2.80
    }
    
    while True:
        mostrar_frutas(precios_frutas.keys())
        
        seleccion = input("\n¿Qué fruta quieres? (o 'salir' para terminar) ").lower()
        
        if seleccion == 'salir':
            print("\n¡Gracias por tu compra!")
            break
            
        if seleccion not in precios_frutas:
            print("Esa fruta no está disponible")
            continue
            
        try:
            cantidad = int(input("¿Cuántas unidades? "))
            if cantidad < 1:
                print("Debe ser al menos 1")
                continue
        except:
            print("Ingresa un número válido")
            continue
            
        total = calcular_total(seleccion, cantidad, precios_frutas)
        print(f"\nTotal por {cantidad} {seleccion}(s): ${total:.2f}")

if __name__ == "__main__":
    main()