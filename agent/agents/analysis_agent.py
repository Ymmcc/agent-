class AnalysisAgent:
    def analyze(self, df):
        result = {}
        for col in df.select_dtypes(include='number').columns:
            result[col] = {
                "mean": df[col].mean(),
                "max": df[col].max(),
                "min": df[col].min()
            }
        return result
