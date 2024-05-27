# This is a file used for keeping utility functions organized in a separate file.

import os
from django.utils.deconstruct import deconstructible

#Renaming the user uploaded files in the formate of "UserIcons/{User.pk}icon.png"
@deconstructible
class CustomUpload:
    def __call__(self, instance, filename):
        # Get the file extension
        ext = filename.split('.')[-1]
        # Create the new file name
        filename = f"{instance.pk}icon.{ext}"
        # Return the whole path to the file
        return os.path.join('Account/UserIcons/', filename)

custom_upload = CustomUpload()
