from App.Template import Template
from PIL import Image

dexter_image = Image.open("plantillas/dexter.jpg")
calamardo_silla_imagen = Image.open("plantillas/calamardo_silla.jpg")
bob_esponja_imagen = Image.open("plantillas/bobEsponjaMeme.jpg")
cita_imagen = Image.open("plantillas/citaPlantilla.jpg")
simpson_imagen = Image.open("plantillas/losSimpsonPlantilla.jpg")
frozen_imagen = Image.open("plantillas/frozen.jpeg")
ex_novia_imagen = Image.open("plantillas/fotoDeExnovia.jpeg")
alabanza_imagen = Image.open("plantillas/alabanza.jpg")
milicia_imagen = Image.open("plantillas/milicia.jpeg")
vas_al_cielo_imagen = Image.open("plantillas/vasAlCielo.jpeg")
padre_abandona_imagen = Image.open("plantillas/tuPapaNosAbandono.jpeg")
smash_imagen = Image.open("plantillas/smashX.jpeg")
mochila_imagen = Image.open("plantillas/mochila.jpeg")
la_que_me_gusta_imagen = Image.open("plantillas/laQueMeGusta.jpeg")
rick_dormido_imagen = Image.open("plantillas/rickDormido.jpg")

dexter_ubicacion = [{"scale": (250, 200), "location": (650, 220)}]
calamardo_Ubicacion = [{"scale": (900, 900), "location": (900, 900)}, {"scale": (900, 900), "location": (900, 0)}]
bob_esponja_ubicacion = [{"scale": (163, 182), "location": (50, 100)}]
cita_ubicacion = [{"scale": (671, 449), "location": (600, 500)}]
simpson_ubicacion = [{"scale":(164,109),"location":(750,318)}]
frozen_ubicacion = [{"scale": (450,450), "location": (50,520)}]
ex_novia_ubicacion = [{"scale": (500,500), "location": (550,550)}]
alabanza_ubicacion = [{"scale": (108,119), "location": (310,50)}]
milicia_ubicacion = [{"scale": (186,182), "location": (150,700)}]
vas_al_cielo_ubicacion = [{"scale": (652,316), "location": (90,70)}]
padre_abandona_ubicacion = [{"scale": (358,321), "location": (50,500)}]
smash_ubicacion = [{"scale": (312,283), "location": (400,30)}]
mochila_ubicacion = [{"scale": (230,272), "location": (120,300)}]
la_que_me_gusta_ubicacion = [{"scale": (152,123), "location": (500,500)}]
rick_dormido_ubicacion = [{"scale":(140,140),"location":(630,50)}]

dexter_plantilla = Template(template_image=dexter_image, place_images=dexter_ubicacion)
calamardo_plantilla = Template(template_image=calamardo_silla_imagen, place_images=calamardo_Ubicacion)
bob_esponja_plantilla = Template(template_image=bob_esponja_imagen, place_images=bob_esponja_ubicacion)
cita_plantilla = Template(template_image=cita_imagen, place_images=cita_ubicacion)
simpson_plantilla = Template(template_image=simpson_imagen,place_images=simpson_ubicacion)
frozen_plantilla = Template(template_image=frozen_imagen,place_images=frozen_ubicacion)
ex_novia_plantilla = Template(template_image=ex_novia_imagen,place_images=ex_novia_ubicacion)
alabanza_plantilla = Template(template_image=alabanza_imagen,place_images=alabanza_ubicacion)
milicia_plantilla = Template(template_image=milicia_imagen,place_images=milicia_ubicacion)
vas_al_cielo_plantilla = Template(template_image=vas_al_cielo_imagen,place_images=vas_al_cielo_ubicacion)
padre_abandona_plantilla = Template(template_image=padre_abandona_imagen,place_images=padre_abandona_ubicacion)
smash_plantilla = Template(template_image=smash_imagen,place_images=smash_ubicacion)
mochila_plantilla = Template(template_image=mochila_imagen,place_images=mochila_ubicacion)
la_que_me_gusta_plantilla = Template(template_image=la_que_me_gusta_imagen,place_images=la_que_me_gusta_ubicacion)
rick_dormido_platilla = Template(template_image=rick_dormido_imagen ,place_images= rick_dormido_ubicacion)

plantillas = [dexter_plantilla, calamardo_plantilla, bob_esponja_plantilla, cita_plantilla,simpson_plantilla,
              frozen_plantilla,ex_novia_plantilla,alabanza_plantilla,milicia_plantilla,vas_al_cielo_plantilla,
              padre_abandona_plantilla,smash_plantilla,mochila_plantilla,la_que_me_gusta_plantilla,rick_dormido_platilla]
