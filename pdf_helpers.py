import os
import pypdfium2 as pdfium
import pypdfium2.raw as pdfium_c

def search_dir(likeness="pdf"):
    mypath = os.getcwd()
    files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    screens = [f for f in files if likeness in  f]
    #print(screens)
    return screens\

def rename_files(file_list=[], name="", extension='.jpeg'):
    n = 1
    for f in file_list:
            os.rename(f, f"{name}{n}.{extension}")
            n +=1

def pdf_jpeg(filename="youngcraftsmande00chicrich.pdf", n = 0):
    '''pdf_jpeg - convert pdf to jpeg images

    * file needs to be in same directory
    '''
    mypath = os.getcwd()
    myfile = os.path.join(mypath, filename)
    pdf = pdfium.PdfDocument(myfile)
    n_pages = len(pdf)

    for i in range(n_pages):
        page = pdf[i]
        image = page.render(scale=4).to_pil()
        image.save(f"{n}.jpeg")
        n += 1


if __name__ == "__main__":
    pdf_jpeg()