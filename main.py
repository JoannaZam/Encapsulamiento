from classWindow import Window

ventana = Window()
ventana.setDimensions(500, 500)
ventana.setTitulo("Mi primer App")
ventana.setResize(True)

print(ventana.getDimensions())
print(ventana.getResize())
print(ventana.getTitulo())

ventana.crear_ventana()