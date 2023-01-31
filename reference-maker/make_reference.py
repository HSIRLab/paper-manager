import pandas as pd
import time

from reference_maker import ReferenceMaker


if __name__ == '__main__':
    excel_name: str = "paper_manager.xlsm"
    reference_text_name: str = "reference_ids.txt"
    out_file_name: str = "references.txt"

    papers_data: pd.DataFrame = pd.read_excel(excel_name, sheet_name="List", index_col="ID")

    with open(reference_text_name, "r", encoding="utf-8") as f:
        reference_list: list[int] = [int(paper_id) for paper_id in f.readline().split(", ")]

    reference_maker = ReferenceMaker(papers_data, reference_list)
    reference_list: list[str] = reference_maker.get_footnotes()

    with open(out_file_name, "w", encoding="utf-8") as f:
        f.write("\n".join(reference_list))

    print("References were successfully created.")
    time.sleep(3)
