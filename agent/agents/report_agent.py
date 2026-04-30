class ReportAgent:
    def generate_report(self, analysis_results):
        report = "Data Analysis Report\n"
        report += "="*30 + "\n"
        for col, stats in analysis_results.items():
            report += f"\nColumn: {col}\n"
            report += f"Mean: {stats['mean']:.2f}\n"
            report += f"Max: {stats['max']}\n"
            report += f"Min: {stats['min']}\n"
        return report
