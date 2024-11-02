from rest_framework import serializers


class RaritySerializer(serializers.Serializer):
	index: int = serializers.IntegerField()
	name: str = serializers.CharField(max_length=50)


class QualitySerializer(serializers.Serializer):
	name: str = serializers.CharField(max_length=2)

class SkinSerializer(serializers.Serializer):
	is_statTrek: bool = serializers.BooleanField()
	is_souvenir: bool = serializers.BooleanField()
	quality: QualitySerializer = QualitySerializer()
	name: str = serializers.CharField(max_length=50)
	gun_name: str = serializers.CharField(max_length=50)
	path_to_icon: str = serializers.CharField(max_length=500)
	rarity: RaritySerializer = RaritySerializer()
	cost: int = serializers.IntegerField()

	class Meta:
		pass
