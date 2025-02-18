from functools import reduce

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
    return last


def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    document = loader.load()
    full_text = reduce(lambda acc, obj: acc + obj.page_content, document, "")
    # print(full_text) # WARN: might be too long and be cutoff by the stdout.
    separator_regex = r"第 \d{1,3}-?\d{0,3} 條"
    splitter = RecursiveCharacterTextSplitter(
        separators=[separator_regex],
        chunk_size=0,
        chunk_overlap=0,
        is_separator_regex=True,
        keep_separator=True,
    )
    text_splitted = splitter.split_text(full_text)
    # for line in text_splitted:
    #     print(line + "\n")
    return len(text_splitted)


if __name__ == "__main__":
    print("============main start============")
    # print("output of hw02_1:\n" + str(hw02_1(q1_pdf)))
    print("output of hw02_2:\n" + str(hw02_2(q2_pdf)))
    print("============main end==============")
