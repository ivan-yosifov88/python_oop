from project.kitten import Kitten
from project.tomcat import Tomcat

tomcat = Tomcat("vani", 33)
print(tomcat.make_sound())
print(tomcat)
kitten = Kitten("Bibi", 34)
print(kitten.make_sound())
print(kitten)