class JenkinsTestResultMetricsData:
    test_name: str
    environment_name: str
    result: bool

class JenkinsResultIn(JenkinsTestResultMetricsData):
    pass

class JenkinsFailedTestEventData:
    environment_name: str
    job_result_url: str

class JenkinsFailedTestEventIn(JenkinsFailedTestEventData):
    pass
