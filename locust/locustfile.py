from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def test_index_page(self):
        self.client.get("/")

    @task
    def test_promotion_page(self):
        self.client.get("/elige-tu-avalon/santa-ana-8/")

    @task
    def test_tipology_page(self):
        self.client.get("/elige-tu-avalon/santa-ana-8/estudio/?promotion_id=a1r7Q0000008cIXQAY")
