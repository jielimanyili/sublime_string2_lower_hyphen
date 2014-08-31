import sublime, sublime_plugin
import unicodedata

# http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
# For example 'Frédér8ic café' to 'freder8ic-cafe'.
def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

class String2LowerHyphenCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    # it should return the selected
    sels = self.view.sel()
    for sel in sels:
        # replace spaces with hyphens
        newString = "-".join(self.view.substr(sel).lower().split())

        # replace accents with ascii representation
        newString = remove_accents(newString)

        # replace input selections
        self.view.replace(edit, sel, newString)