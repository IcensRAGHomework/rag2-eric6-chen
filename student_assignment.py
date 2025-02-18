from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)

q1_pdf = r"OpenSourceLicenses.pdf"
q2_pdf = r"勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    document = loader.load()
    last = document[-1]
    return str(last.page_content) + str(last.metadata)


def hw02_2(q2_pdf):
    pass


if __name__ == "__main__":
    print("============main start============")
    print("result of hw02_1:\n" + hw02_1(q1_pdf))
    print("============main end==============")
