class SpectrumEncoder:
    def encode(self, ranking, top_k=10):
        return '\n'.join([f"{e}: {s:.4f}" for e, s in ranking[:top_k]])
