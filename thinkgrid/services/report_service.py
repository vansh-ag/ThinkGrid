from pathlib import Path


class ReportService:

    REPORT_DIR = Path(
        "data/reports"
    )

    @classmethod
    def save_report(
        cls,
        topic: str,
        report: str
    ):
        """
        Save markdown report.
        """

        cls.REPORT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        filename = (
            topic.replace(" ", "_")
            + ".md"
        )

        filepath = cls.REPORT_DIR / filename

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        return str(filepath)

    @classmethod
    def load_report(
        cls,
        filename: str
    ):
        """
        Load saved report.
        """

        filepath = cls.REPORT_DIR / filename

        if not filepath.exists():
            raise FileNotFoundError(
                f"{filename} not found"
            )

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    @classmethod
    def list_reports(cls):
        """
        List all reports.
        """

        cls.REPORT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        return [
            file.name
            for file in cls.REPORT_DIR.glob("*.md")
        ]

    @classmethod
    def delete_report(
        cls,
        filename: str
    ):
        """
        Delete report.
        """

        filepath = cls.REPORT_DIR / filename

        if filepath.exists():

            filepath.unlink()

            return True

        return False