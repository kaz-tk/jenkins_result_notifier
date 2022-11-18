from ..applications.containers import ApplicationContainer
from ..applications.controllers.notifier_controller import gauge, event

def gauge():
    container = ApplicationContainer()
    container.config.from_dict({
        "metrics_service": "datadog"
    })
    container.wire(modules=[
        "jenkins_result_notifier.applications.controllers.notifier_controller"
    ])
    gauge()


if __name__ == '__main__':
    gauge()
