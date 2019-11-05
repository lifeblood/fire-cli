from pywinauto.application import Application


class Winauto(object):
    def __init__(self):
        pass

    def test(self):
        # Run a target application
        app = Application().start("notepad.exe")
        # Select a menu item
        notepad = u'帮助->关于记事本'
        app.UntitledNotepad.menu_select(notepad)
        # Click on a button
        out_note = u'关于记事本'
        button_name_ok = '确定'
        app[out_note][button_name_ok].click()
        # Type a text string
        app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)


