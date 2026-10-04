from locust import HttpUser, task, between


class FlightUser(HttpUser):

    wait_time = between(1, 3)

    @task
    def search_flights(self):
        self.client.get(
            "/flights?from=DEL&to=JFK"
        )
