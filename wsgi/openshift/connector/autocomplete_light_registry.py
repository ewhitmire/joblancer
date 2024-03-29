import autocomplete_light
from connector.models import Tag

# This will generate a PersonAutocomplete class
autocomplete_light.register(Tag,
    # Just like in ModelAdmin.search_fields
    search_fields=['name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'eg. python, android, graphics',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 10,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)