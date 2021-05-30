class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return '\n'.join([f'{document}'for document in self.documents])

    @staticmethod
    def is_element_exist(element, list_of_elements):
        return element in list_of_elements

    @staticmethod
    def is_valid_id(id, list_id):
        ll = [element for element in list_id if element.customer_id == id]
        if ll:
            return ll[0]


    def add_category(self, category):
        if not self.is_element_exist(category, self.categories):
            self.categories.append(category)

    def add_topic(self, topic):
        if not self.is_element_exist(topic, self.topics):
            self.topics.append(topic)

    def add_document(self, document):
        if not self.is_element_exist(document, self.documents):
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        current_category = self.is_valid_id(category_id, self.categories)
        if current_category:
            current_category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        current_topic = self.is_valid_id(topic_id, self.topics)
        if current_topic:
            current_topic.topic = new_topic
            current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        current_document = self.is_valid_id(document_id, self.documents)
        if current_document:
            current_document.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = self.is_valid_id(category_id, self.categories)
        if current_category:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = self.is_valid_id(topic_id, self.topics)
        if current_topic:
            self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = self.is_valid_id(document_id, self.documents)
        if current_document:
            self.documents.remove(current_document)

    def get_document(self, document_id):
        current_document = self.is_valid_id(document_id, self.documents)
        if current_document:
            return current_document
