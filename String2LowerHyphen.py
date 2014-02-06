import sublime, sublime_plugin

class String2LowerHyphenCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # it should return the selected
    sels = self.view.sel()
    for sel in sels:
        newString = "-".join(self.view.substr(sel).lower().split())
        self.view.replace(edit, sel, newString)