import json

from peewee import *

DATABASE = SqliteDatabase('minerals.db')


class Mineral(Model):
    name = CharField(max_length=255)
    image_filename = CharField(max_length=255, null=True)
    image_caption = CharField(max_length=255, null=True)
    category = CharField(max_length=255, null=True)
    formula = CharField(max_length=255, null=True)
    strunz_classification = CharField(max_length=255, null=True)
    crystal_system = CharField(max_length=255, null=True)
    unit_cell = CharField(max_length=255, null=True)
    color = CharField(max_length=255, null=True)
    crystal_symmetry = CharField(max_length=255, null=True)
    cleavage = CharField(max_length=255, null=True)
    mohs_scale_hardness = CharField(max_length=255, null=True)
    luster = CharField(max_length=255, null=True)
    streak = CharField(max_length=255, null=True)
    diaphaneity = CharField(max_length=255, null=True)
    optical_properties = CharField(max_length=255, null=True)
    refractive_index = CharField(max_length=255, null=True)
    crystal_habit = CharField(max_length=255, null=True)
    specific_gravity = CharField(max_length=255, null=True)
    group = CharField(max_length=255, null=True)

    class Meta:
        database = DATABASE
        db_table = 'minerals_mineral'
        
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Mineral], safe=True)
    
    
def mineral_data_dict(mineral):
    full_mineral_dict = {
        'name': None,
        'image filename': None,
        'image caption': None,
        'category': None,
        'formula': None,
        'strunz classification': None,
        'crystal system': None,
        'unit cell': None,
        'color': None,
        'crystal symmetry': None,
        'cleavage': None,
        'mohs scale hardness': None,
        'luster': None,
        'streak': None,
        'diaphaneity': None,
        'optical properties': None,
        'refractive index': None,
        'crystal habit': None,
        'specific gravity': None,
        'group': None,
    }
    for key, value in mineral.items():
        full_mineral_dict[key] = value
    return full_mineral_dict


def json_to_db():
    with open('minerals.json', encoding='utf-8') as file:
        minerals = json.load(file) 
        for mineral in minerals:
            mineral_data = mineral_data_dict(mineral=mineral)
            Mineral.create(
                name = mineral_data['name'],
                img_filename = mineral_data['image filename'],
                img_caption = mineral_data['image caption'],
                category = mineral_data['category'],
                formula = mineral_data['formula'],
                strunz_classification = mineral_data['strunz classification'],
                crystal_system = mineral_data['crystal system'],
                unit_cell = mineral_data['unit cell'],
                color = mineral_data['color'],
                crystal_symmetry = mineral_data['crystal symmetry'],
                cleavage = mineral_data['cleavage'],
                mohs_hardness = mineral_data['mohs scale hardness'],
                luster = mineral_data['luster'],
                streak = mineral_data['streak'],
                diaphaneity = mineral_data['diaphaneity'],
                optical_properties = mineral_data['optical properties'],
                refractive_index = mineral_data['refractive index'],
                crystal_habit = mineral_data['crystal habit'],
                specific_gravity = mineral_data['specific gravity'],
                group = mineral_data['group']
            )
        
if __name__ == '__main__':
    initialize()
    json_to_db()