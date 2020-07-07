from jinja2 import Template
from src.bingo import carton_definitivo

template = Template(open("jinja2/templatebingo.jinja2").read())

file = open("Bingo.html", "w")
file.write(template.render(carton = carton_definitivo()))
file.close()
print("Creando \"Bingo.html\". Para ver el carton generado abra el archivo.")