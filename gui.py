import functions
import PySimpleGUI as PY

label = PY.Text("Type in a to-do")
input_box = PY.InputText(tooltip="Enter to-do")
add_button = PY.Button("Add")


window = PY.Window("My To - Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()


