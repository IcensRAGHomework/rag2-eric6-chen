from functools import reduce

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
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


def page_content_merger(pg1: str, pg2: Document):
    """
    some page might not have newline on the end which will be very painful when splitting.
    so just workaround it by appending newline for them.
    """
    pg1_missing_newline_on_end = not pg1.endswith("\n")
    if pg1_missing_newline_on_end:
        return pg1 + "\n" + pg2.page_content
    else:
        return pg1 + pg2.page_content


def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    document = loader.load()
    full_text = reduce(page_content_merger, document, "")
    # print(full_text) # WARN: might be too long and be cutoff by the stdout.
    separator_regexs = [
        r"第 \d{1,3}-?\d{0,3} 條\n",
        r"第 [一二三四五六七八九十]{1,2} 章 .*\n",
    ]
    splitter = RecursiveCharacterTextSplitter(
        separators=separator_regexs,
        chunk_size=0,
        chunk_overlap=0,
        is_separator_regex=True,
        keep_separator=True,
    )
    chunks = splitter.split_text(full_text)
    # for chunk in chunks:
    #     print("---------------")
    #     print(chunk)
    return len(chunks)


if __name__ == "__main__":
    print("============main start============")
    # print("output of hw02_1:\n" + str(hw02_1(q1_pdf)))
    # print("output of hw02_2:\n" + str(hw02_2(q2_pdf)))
    print("============main end==============")
