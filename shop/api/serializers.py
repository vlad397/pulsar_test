from PIL import Image
from rest_framework import serializers

from shop.settings import MEDIA_ROOT

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta(object):
        model = Item
        fields = '__all__'

    def get_image(self, obj):
        path = f'{MEDIA_ROOT}/{obj.image}'
        im_format = path.split('.')[-1]
        no_format = path.split('.')[0]

        im = Image.open(path).convert('RGB')
        im.save(f'{no_format}.webp', 'WEBP')

        path_for_response = '/' + path.split('\\')[-1].replace(f'.{im_format}', '')

        return {'path': path_for_response, 'formats': [im_format, 'webp']}
