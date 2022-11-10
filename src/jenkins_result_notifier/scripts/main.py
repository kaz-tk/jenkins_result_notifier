from ..applications.containers import ApplicationContainer
from ..applications.controllers.notifier_controller import notify

def main():
    container = ApplicationContainer()
    container.config.from_dict({
        "metrics_service": "datadog"
    })
    container.wire(modules=[
        "jenkins_result_notifier.applications.controllers.notifier_controller"
    ])
    notify()


if __name__ == '__main__':
    main()
