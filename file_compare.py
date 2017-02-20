"""python tools for autocad
"""
from pyautocad import Autocad


def main():
    """main program function"""
    cad = Autocad(create_if_not_exists = True)
    open_docs = cad.app.documents
    doc_list = []
    for open_doc in open_docs:
        print(open_doc.path + "\\" + open_doc.name)
        doc_list.append(open_doc)
    if open_docs.__sizeof__ != 2:
        print("only two drawings can be comparred")
        print(len(doc_list))


if __name__ == '__main__':
    main()
