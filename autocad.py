"""Autocad testing
"""
from pyautocad import Autocad, APoint
from tkinter import *


def compare(cad):
    """main program function"""
    open_docs = cad.app.documents
    doc_list = []
    for open_doc in open_docs:
        print(open_doc.path + "\\" + open_doc.name)
        doc_list.append(open_doc)
    if len(doc_list) != 2:
        print("only two drawings can be comparred")


def load_att(cad):
    """reload attribute
    reload the attribute block located in the xref folder
    """
    is_att = False
    for block in cad.iter_objects_fast("block"):
        if block.name == "attribute" or block.name == "Attribute":
            block.delete()
            is_att = True
            break
    if not is_att:
        cad_path = cad.ActiveDocument.path()
        print(cad_path)
        for layouts in cad.iter_layouts(doc=None, skip_model=True):
            print(layouts.name)
            cad.doc.activelayout = layouts
            cad.doc.paperspace.InsertBlock(
                APoint(0, 0), cad_path + "\\xref\\Attribute.dwg", 1, 1, 1, 0)


def main():
    '''gui portion'''
    cad = Autocad(create_if_not_exists=True)
    root = Tk()
    root.geometry('300x100+1000+500')
    button_compare = Button(root, text='Compare', command=lambda: compare(cad))
    button_loadatt = Button(root, text='Load_att', command=lambda: load_att(cad))
    button_compare.pack(pady=10, padx=10)
    button_loadatt.pack(pady=10, padx=10)
    root.mainloop()

if __name__ == "__main__":
    main()
