class StyleLoader():
    def load(self, filename):
        with open(filename, "r") as f:
            return f.read()

# Create a singleton instance for backward compatibility
style_loader = StyleLoader()
