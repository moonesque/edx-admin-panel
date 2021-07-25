"""
iknito_admin_panel Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    ProjectType, SettingsType, PluginURLs, PluginSettings, PluginContexts
)

class IknitoAdminPanelConfig(AppConfig):
    """
    Configuration for the iknito_admin_panel Django application.
    """

    name = "iknito_admin_panel"
    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        # Configuration setting for Plugin URLs for this app.
        PluginURLs.CONFIG: {
            # Configure the Plugin URLs for each project type, as needed.
            ProjectType.LMS: {
                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: "iknito_admin_panel",
                # The application namespace to provide to django's urls.include.
                # Optional; Defaults to None.
                PluginURLs.APP_NAME: "iknito_admin_panel",
                # The regex to provide to django's urls.url.
                # Optional; Defaults to r''.
                PluginURLs.REGEX: r"^api/iknito_admin_panel/",
                # The python path (relative to this app) to the URLs module to be plugged into the project.
                # Optional; Defaults to 'urls'.
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },

        

    }
