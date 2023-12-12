import psutil

# Script Name:                  pyutil.py
# Author:                       Michael Sineiro
# Date of latest revision:      12/11/2023
# Purpose:                      use psutil methods to grab info,
#########                       filters it, and prints.
# Execution:                    python3 pyutil.py

class CpuTimeAnalyzer:
    """Class for CPU time retrieval and analysis."""

    def __init__(self):
        """Gets cpu times and assigns them to a variable"""
        self.cpu_times = psutil.cpu_times()

    def get_system_info(self):
        """Returns formatted CPU time breakdown."""
        formatInfo = "\t**CPU Time Breakdown:**\n"

        # Access values using namedtuple attributes
        for key in self.cpu_times._fields:
            formatInfo += f"\t- {key.title()}: {getattr(self.cpu_times, key):.2f} seconds\n"

        return formatInfo

if __name__ == "__main__":
    analyzer = CpuTimeAnalyzer()
    print(analyzer.get_system_info())
