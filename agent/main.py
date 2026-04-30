from agents.data_agent import DataUnderstandingAgent
from agents.analysis_agent import AnalysisAgent
from agents.report_agent import ReportAgent

def run_pipeline(file_path):
    data_agent = DataUnderstandingAgent()
    analysis_agent = AnalysisAgent()
    report_agent = ReportAgent()

    df = data_agent.load_and_clean(file_path)
    analysis_results = analysis_agent.analyze(df)
    report = report_agent.generate_report(analysis_results)

    print(report)

if __name__ == "__main__":
    run_pipeline("data/sample.csv")
