class Document:
    def __init__(self, id, category_id, topic_id, file_name):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    def __repr__(self):
        tags = ', '.join(self.tags)
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {tags}"

    @classmethod
    def from_instances(cls, id, category, topic, file_name):
        return cls(id, category.customer_id, topic.customer_id, file_name)

    @staticmethod
    def is_tag(tag, tags):
        return tag in tags

    def add_tag(self, tag_content):
        if not self.is_tag(tag_content, self.tags):
            self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        if self.is_tag(tag_content, self.tags):
            self.tags.remove(tag_content)

    def edit(self, file_name):
        self.file_name = file_name

