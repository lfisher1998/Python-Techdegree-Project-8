import os, json

from django.db import migrations
from django.conf import settings
from minerals.models import Mineral

def load_data(apps, schema_editor):
	  # migration way of linking to your Model.
    Mineral = apps.get_model("minerals", "Mineral")
    filepath = os.path.join(settings.BASE_DIR, 'minerals', 'migrations', 'minerals.json')
    with open(filepath, encoding="utf-8") as file:
        minerals = json.load(file) 
        for mineral in minerals:
            Mineral.objects.create(
            name=mineral['name'],
            image_filename=mineral['name'] + ".jpg",
            image_caption=mineral['image caption'],
            category=mineral['category'],
            formula=mineral.get('formula', ''),
            strunz_classification=mineral.get('strunz classification', ''),
            crystal_system=mineral.get('crystal system', ''),
            unit_cell=mineral.get('unit cell', ''),
            color=mineral.get('color', ''),
            crystal_symmetry=mineral.get('crystal symmetry', ''),
            cleavage=mineral.get('cleavage', ''),
            mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
            luster=mineral.get('luster', ''),
            streak=mineral.get('streak', ''),
            diaphaneity=mineral.get('diaphaneity', ''),
            optical_properties=mineral.get('optical properties', ''),
            refractive_index=mineral.get('refractive index', ''),
            crystal_habit=mineral.get('crystal habit', ''),
            specific_gravity=mineral.get('specific gravity', ''),
            group=mineral.get('group', ''),
            )
        


class Migration(migrations.Migration):
	  # Our data cannot be loaded unless 0001_initial ran first.
    dependencies = [
		('minerals', '0001_initial'),
	]

    operations = [
		# we pass in the name of the function that will be called when
		# python manage.py migrate runs this migration.
        migrations.RunPython(load_data),
    ]