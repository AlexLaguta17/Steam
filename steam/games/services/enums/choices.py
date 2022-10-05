from django.db import models


class ItemTypeChoices(models.TextChoices):
    CONSUMER_GRADE = 'CONSUMER_GRADE', 'Consumer grade'
    INDUSTRIAL_GRADE = 'INDUSTRIAL_GRADE', 'Industrial grade'
    MIL_SPEC = 'MIL_SPEC', 'Mil-spec'
    RESTRICTED = 'RESTRICTED', 'Restricted'
    CLASSIFIED = 'CLASSIFIED', 'Classified'
    COVERT = 'COVERT', 'Covert'


class ItemQualityChoices(models.TextChoices):
    BATTLE_SCARRED = 'BATTLE_SCARRED', 'Battle-Scarred'
    WELL_WORN = 'WELL_WORN', 'Well-Worn'
    FIELD_TESTED = 'FIELD_TESTED', 'Field-Tested'
    MINIMAL_WEAR = 'MINIMAL_WEAR', 'Minimal Wear'
    FACTORY_NEW = 'FACTORY_NEW', 'Factory new'


class GameCategoryChoices(models.TextChoices):
    ACTION = 'ACTION', 'Action'
    SHOOTER = 'SHOOTER', 'Shooter'
    ADVENTURES = 'ADVENTURES', 'Adventures'
    PUZZLE = 'PUZZLE', 'Puzzle'
    CASUAL = 'CASUAL', 'Casual'
    ROLE_PLAYING = 'ROLE_PLAYING', 'Role-playing'
    SIMULATOR = 'SIMULATOR', 'Simulator'
    STRATEGY = 'STRATEGY', 'Strategy'
    SPORTS = 'SPORTS', 'Sports'
    RACE = 'RACE', 'Race'
    CARD = 'CARD', 'Card'
