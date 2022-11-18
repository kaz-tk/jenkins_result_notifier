from ...domain.metrics import MetricsService
from ...applications.containers import ApplicationContainer
from dependency_injector.wiring  import Provide, inject
from ..models.jenkins_result import JenkinsFailedTestEventIn, JenkinsResultIn
@inject
def gauge(
    data: JenkinsResultIn,
    metrics_service: MetricsService=Provide[ApplicationContainer.metrics_service]
    ):
    # ToDo: validate request data
    # it is better to convert to domain model
    metrics_service.notify(data)

@inject
def event(
    data: JenkinsFailedTestEventIn,
    event_service: EventService=Provide[ApplicationContainer.event_service]
    ):
    # ToDo: validate request data
    # it is better to convert to domain model
    event_service.event(data)
