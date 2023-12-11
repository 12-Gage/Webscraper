from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def topic_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def url_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def run_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    topic = self.topic_box.text
    url = self.url_box.text
    
    anvil.server.call('raw_data', url)
    Notification("Feedback Submitted").show()

    self.url_box.text = ""
    self.topic_box.text = ""
    
