"""
iknito_admin_panel Django application initialization.
"""

from django.apps import AppConfig


class IknitoAdminPanelConfig(AppConfig):
    """
    Configuration for the iknito_admin_panel Django application.
    """

    name = "iknito_admin_panel"
    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "iknito_admin_panel",
                "regex": "^api/iknito_admin_panel/",
                "relative_path": "urls",
            }
        }
    }
