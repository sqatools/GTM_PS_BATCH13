"""
Generate HTML Report
"""

from datetime import datetime
import os


class GenerateReport:

    @staticmethod
    def create_report(test_name,
                      status,
                      assigned_team,
                      root_cause,
                      resolution):

        os.makedirs("reports", exist_ok=True)

        html = f"""

        <html>

        <head>

        <title>Telecom AI Report</title>

        </head>

        <body>

        <h1>Agentic AI Test Report</h1>

        <table border="1">

        <tr>

        <td>Test Name</td>

        <td>{test_name}</td>

        </tr>

        <tr>

        <td>Status</td>

        <td>{status}</td>

        </tr>

        <tr>

        <td>Assigned Team</td>

        <td>{assigned_team}</td>

        </tr>

        <tr>

        <td>Root Cause</td>

        <td>{root_cause}</td>

        </tr>

        <tr>

        <td>Resolution</td>

        <td>{resolution}</td>

        </tr>

        <tr>

        <td>Execution Time</td>

        <td>{datetime.now()}</td>

        </tr>

        </table>

        </body>

        </html>

        """

        file_name = f"reports/{test_name}.html"

        with open(file_name, "w") as file:

            file.write(html)

        return file_name