import psutil

class CpuTimeAnalyzer:
    """Class for CPU time retrieval and analysis."""

    def __init__(self):
        self.cpu_times = psutil.cpu_times()

    def get_system_info(self):
        """Returns formatted CPU time breakdown."""
        formatInfo = "**CPU Time Breakdown:**\n"

        # Access values using namedtuple attributes
        for key in self.cpu_times._fields:
            formatInfo += f"\t- {key.title()}: {getattr(self.cpu_times, key):.2f} seconds\n"

        return formatInfo

if __name__ == "__main__":
    analyzer = CpuTimeAnalyzer()
    print(analyzer.get_system_info())
