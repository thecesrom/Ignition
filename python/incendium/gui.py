# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium GUI module."""

__all__ = [
    'confirm',
    'error',
    'info'
]

import system.gui
import system.util
from javax.swing import JOptionPane


def confirm(message, title, show_cancel=False):
    """Displays a confirmation dialog box to the user with "Yes", "No"
    and "Cancel" options, and a custom message.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale.
        title (str): A title for the message box. This will be
            translated to the selected Locale.
        show_cancel (bool): Show a cancel button in the dialog.
            Optional.

    Returns:
        bool: True if the user selected "Yes", False if the user
            selected "No", None if the user selected "Cancel".
    """
    return system.gui.confirm(system.util.translate(message),
                              system.util.translate(title),
                              show_cancel)


def error(message, title):
    """Displays an error-style message box to the user.

    Args:
        message (str): The message to display in an error box. This will
            be translated to the selected Locale.
        title (str): A title for the message box. This will be
            translated to the selected Locale.
    """
    JOptionPane.showMessageDialog(None,
                                  system.util.translate(message),
                                  system.util.translate(title),
                                  JOptionPane.ERROR_MESSAGE)


def info(message, title, detail=None):
    """Displays an informational-style message popup box to the user.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale.
        title (str): A title for the message box. This will be
            translated to the selected Locale.
        detail (str): Additional text to display. This will be
            translated to the selected Locale. Optional.
    """
    if detail is None:
        system.gui.messageBox(system.util.translate(message),
                              system.util.translate(title))
    else:
        msg = '%s %s' % (system.util.translate(message),
                         system.util.translate(detail))
        system.gui.messageBox(msg, system.util.translate(title))


def warning(message, title):
    """Displays a message to the user in a warning style pop-up dialog.

    Args:
        message (str): The message to display in an warning box. This
            will be translated to the selected Locale.
        title (str): A title for the warning box. This will be translated
            to the selected Locale.
    """
    JOptionPane.showMessageDialog(None,
                                  system.util.translate(message),
                                  system.util.translate(title),
                                  JOptionPane.WARNING_MESSAGE)
