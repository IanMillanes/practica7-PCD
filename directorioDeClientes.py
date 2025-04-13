clientes = {}
datosCliente = {}

datos_clientes = """nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

lista_clientes = datos_clientes.split("\n")
cabeceras = lista_clientes[0].split(";")[1:]  
datos = [cliente.split(";") for cliente in lista_clientes[1:]]


for fila in datos:
    nif = fila[0]
    datos_cliente = {}
    for i in range(len(cabeceras)):
        datos_cliente[cabeceras[i]] = fila[i+1] 
    datosCliente[nif] = datos_cliente

print(datosCliente)