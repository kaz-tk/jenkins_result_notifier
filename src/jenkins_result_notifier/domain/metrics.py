from dependency_injector.wiring  import inject


class MetricsService:
    @inject
    def __init__(self, api_client):
        self.api_client = api_client
        pass

    def notify(self):
        raise NotImplementedError()
