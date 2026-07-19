"""
Generate AI Test Report
"""

from datetime import datetime


class ReportManager:

    @staticmethod
    def generate_report(test_name, status, summary):

        report = f"""
=================================

Telecom Agentic AI Report

=================================

Test Name : {test_name}

Status    : {status}

Executed  : {datetime.now()}

Summary

{summary}

=================================
"""

        with open(

            f"reports/{test_name}.txt",

            "w"

        ) as file:

            file.write(report)

        return report