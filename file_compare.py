from pyautocad import Autocad

def main():
    cad = Autocad(create_if_not_exists = True)
    open_docs = cad.app.documents
    for open_doc in open_docs:
        print(open_doc.path + "\\" + open_doc.name)
        

if __name__ == '__main__':
    main()