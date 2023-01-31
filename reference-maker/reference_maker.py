import pandas as pd


class ReferenceMaker:
    def __init__(self, papers_data: pd.DataFrame, reference_list: list[int]):
        self.__papers_data: pd.DataFrame = papers_data
        self.__reference_ids: list[int] = reference_list

    def get_footnotes(self) -> list[str]:
        foot_notes: list[str] = []
        for paper_id in self.__reference_ids:
            foot_notes.append(self.__make_footnote(paper_id))

        return foot_notes

    def __make_footnote(self, paper_id: int) -> str:
        paper_info: pd.Series = self.__papers_data.loc[paper_id]

        authors_list: list[str] = paper_info.at["Author"].split(", ")
        if len(authors_list) == 1:
            author: str = authors_list[0]
        elif len(authors_list) <= 4:
            author: str = f"{', '.join(authors_list[:-1])} and {authors_list[-1]}"
        else:
            author: str = f"{', '.join(authors_list[:2])} and {authors_list[2]} et al"

        publication_detail: str = f"{paper_info.at['Other Details']}, {paper_info.at['Year']}."

        footnote: str = ". ".join([author, paper_info.at["Title"], publication_detail])

        return footnote
