from django.test import TestCase
from html_export_helper import html_export_helper
from uuid import UUID
from pprint import pprint


class TestCreateTemplate(TestCase):

    def test_one_level_one_val(self):

        resource = {"@display_value": "value"}

        result = html_export_helper(resource, "resource")

        self.assertEqual(result, ['{{ resource|val_from_key:"@display_value" }}'])

    def test_one_level_multiple_keys(self):

        resource = {"@display_value": "value", "other_key": "value"}

        result = html_export_helper(resource, "resource")

        self.assertEqual(result, ['{{ resource|val_from_key:"@display_value" }}'])

    def test_two_level_single_val(self):

        resource = {"level_1": {"@display_value": "nested_value"}}

        result = html_export_helper(resource, "resource")

        self.assertEqual(
            result, ['{{ resource|val_from_key:"level_1"|val_from_key:"@display_value" }}']
        )

    def test_three_level_single_val(self):

        resource = {"level_1": {"level_2": {"@display_value": "nested_value"}}}

        result = html_export_helper(resource, "resource")

        self.assertEqual(
            result,
            ['{{ resource|val_from_key:"level_1"|val_from_key:"level_2"|val_from_key:"@display_value" }}']
        )

    def test_multiple_levels_multiple_keys_one_value(self):

        resource = {
            "level_1a": {
                "level_1a_2a": {"@display_value": "nested_value"},
                "level_1a_2b": "other value 1",
            },
            "level_1b": {"level_1b_2": "other value 2"},
        }

        result = html_export_helper(resource, "resource")

        self.assertEqual(
            result,
            ['{{ resource|val_from_key:"level_1a"|val_from_key:"level_1a_2a"|val_from_key:"@display_value" }}']
        )

    def test_two_layers_two_values(self):

        resource = {
            "level_1a": {"@display_value": "nested_value 1"},
            "level_1b": {"@display_value": "nested_value 2"},
        }

        result = html_export_helper(resource, "resource")

        self.assertEqual(
            result,
            [
                '{{ resource|val_from_key:"level_1a"|val_from_key:"@display_value" }}',
                '{{ resource|val_from_key:"level_1b"|val_from_key:"@display_value" }}',
            ],
        )

    def test_handle_array(self):

        resource = {
            "dict_arr": [
                {
                    "dict_1": {"@display_value": "nested_value 1"}
                },
                {
                    "dict_2": {"@display_value": "nested_value 2"}
                }
            ]
        }

        result = html_export_helper(resource, "resource")

        self.assertEqual(
            result,
            [
                '{% for x in resource|val_from_key:"dict_arr" %}',
                '{{ x|val_from_key:"dict_1"|val_from_key:"@display_value" }}',
                '{{ x|val_from_key:"dict_2"|val_from_key:"@display_value" }}',
                '{% endfor %}'
            ],
        )
