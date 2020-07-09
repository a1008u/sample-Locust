from locust import HttpLocust, TaskSet, task

class UserTaskSet(TaskSet):
    def on_start(self):
        """
        タスクセットの開始時に1回のみ呼ばれます。
        """
        # self.client.post("/login", {"username": "ellen_key", "password": "education"})
        self.client.get("/")

    @task
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserTaskSet

    # task実行の最短待ち時間
    min_wait = 1000
    # task実行の最大待ち時間
    max_wait = 1000


# import uuid

# from datetime import datetime
# from locust import HttpLocust, TaskSet, task


# class MetricsTaskSet(TaskSet):
#     _deviceid = None

#     def on_start(self):
#         self._deviceid = str(uuid.uuid4())

#     @task(1)
#     def login(self):
#         self.client.post(
#             '/login', {"deviceid": self._deviceid})

#     @task(999)
#     def post_metrics(self):
#         self.client.post(
#             "/metrics", {"deviceid": self._deviceid, "timestamp": datetime.now()})


# class MetricsLocust(HttpLocust):
#     task_set = MetricsTaskSet
