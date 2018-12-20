from peewee import *
from datetime import date

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


def create_and_connect():
    db.connect()
    db.create_tables([Person, Pet], safe=True)


def create_family_members():
##  Completand formulario de la tabla persona
    uncle_bob = Person(name="Ana", birthday=date(2000, 11, 11), is_relative=True)
    uncle_bob.save()
    grandma = Person.create(name="Grandama", birthday=date(1953, 3, 1), is_relative=False)
    herb = Person.create(name="Herb", birthday=date(1950, 5, 5), is_relative=True)

##  Completaando formulario de la table de Mascota
    bob_kitty = Pet.create(owner=uncle_bob, name="Kitty", animal_type="Cat")
    herb_fido = Pet.create(owner=herb, name="Fido", animal_type="Dog")
    herb_mittens = Pet.create(owner=herb, name="Mittens", animal_type="Cat")
    herb_mittens_jr = Pet.create(owner=herb, name="Mittens_Jr", animal_type="Cat")

def get_family_members():
    for person in Person.select():
        print("Nombre: {0} Fecha de nacimiento: {1} Is_relativa: {2} ".format(person.name, person.birthday,
                                                                              person.is_relative))

    print("\n")

    for pet in Pet.select():
        print("Nombre de la mascota: {} Tipo: {} Propietario: {}".format(pet.name, pet.animal_type, pet.owner))


def get_family_member():
    grandma_rosa = Person.select().where(Person.name == 'Grandama' ).get()
    print("Rosa cumple el: {}".format(grandma_rosa.birthday))

    Herb = Person.get( Person.name == 'Herb' )
    print( "Herb Cumple en: {}".format( Herb.birthday) )


def get_family_memeber_birthday(name):
    Ana = Person.get( Person.name == name )
    print( "El cumplea  de {} es {}".format( Ana.name, Ana.birthday ) )

def delete_family(name):
    query = Person.delete().where( Person.name == name )
    delete_enteries = query.execute()
    print("{} Registros borrados".format(delete_enteries))


def delete_pet(name):
    query = Pet.delete().where(Pet.name == name)
    delete_enteries = query.execute()
    print("{} Registros borrados".format(delete_enteries))

create_and_connect()
create_family_members()

get_family_members()
print("\n")
#get_family_member()
#get_family_memeber_birthday('Ana')
#Borrar Informacion
#delete_pet("Mittens_Jr") #Mascotas
#delete_family("Grandama") #Dueños de mascotas
