from controllers.settings_controller import SettingsController
from controllers.add_connection_controller import AddConnectionController
class MainController:
	def __init__(self, view, model):
		self.view = view
		self.model = model
		self.view.construct_view()
		self.construct_subcontrollers()
		self.set_events()
	
	def construct_subcontrollers(self):
		settings_view = self.view.getSettingsView()
		settings_view.setMainView(self.view)
		SettingsController(settings_view, self.model)
		
	def set_events(self):
		dropmenu = self.view.getWidget("Application_dropmenu")
		dropmenu.entryconfig(0, command = self.open_settings)
		dropmenu.entryconfig(1, command = self.open_add_connection)
		window = self.view.getWidget("window")
		window.protocol('WM_DELETE_WINDOW', self.close)
		
	
	def open_settings(self):
		settings_view = self.view.getSettingsView()
		settings_view.show()
	
	def open_add_connection(self):
		add_connection_view = self.view.getAddConnectionView()
		add_connection_view.show() #refresh
		add_connection_view.setMainView(self.view)
		AddConnectionController(add_connection_view, self.model)
	
	def close(self):
		self.model.close()
		add_connection_view = self.view.getAddConnectionView()
		window = add_connection_view.getWidget("toplevel_add_connection_window")
		window.destroy()
		
		settings_view = self.view.getSettingsView()
		window = settings_view.getWidget("toplevel_settings_window")
		window.destroy()
		
		message_view = self.view.getMessageView()
		window = message_view.getWidget("window")
		window.destroy()
		
		window = self.view.getWidget("window")
		window.destroy()

		
	
