class Notebook:

    def __init__(self, nr_of_pages, color):
        self.nr_of_pages = nr_of_pages
        self.color = color
        self.content = []


    def write_to_notebook(self, content):
        if self.empty_pages() != 0:
            self.content.append(content)

    def empty_pages(self):
        return self.nr_of_pages - len(self.content)

    def written_pages(self):
        return len(self.content)