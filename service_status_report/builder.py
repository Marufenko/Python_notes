from enum import Enum


class Container:
    def __init__(self, host, service, space, sessions):
        self.host = host
        self.service = service
        self.space = space
        self.sessions = sessions


class Host:
    def __init__(self, name, status):
        self.name = name
        self.status = status


class Service:
    def __init__(self, status):
        self.status = status


class Space:
    def __init__(self, data, status):
        self.data = data
        self.status = status


class Sessions:
    def __init__(self, sessions):
        self.sessions = sessions


element = """
<div class="container oneline" style="border-color: var({});">
      <div class="host oneline">{}</div>
      <span class="service" style="background-color: var({});"></span>
      <div class="sessions">
        <div class="space oneline" style="color:  var({});">{}</div>
        <span class="session oneline session_n" style="background-color: var({});"></span>
        <span class="session oneline session_n-1" style="background-color: var({});"></span>
        <span class="session oneline session_n-2" style="background-color: var({});"></span>
        <span class="session oneline session_n-3" style="background-color: var({});"></span>
        <span class="session oneline session_n-4" style="background-color: var({});"></span>
      </div>
    </div>
"""


class Element:
    def __init__(self, input_data_set):
        self.element = self.compose_element(input_data_set)

    @staticmethod
    def compose_element(input_data_set):
        data = input_data_set
        return element.format(
            data.host.status,
            data.host.name,
            data.service.status,
            data.space.status,
            data.space.data,
            data.sessions.sessions[0],
            data.sessions.sessions[1],
            data.sessions.sessions[2],
            data.sessions.sessions[3],
            data.sessions.sessions[4],
        )


class Status(Enum):
    DOWN = 0
    UP = 1
    INACTIVE = 2
    OK = 4
    ERROR = 5


def main():
    data_set = get_data()
    body_element = Element(data_set)
    print(body_element.element)


def get_data():
    return Container(
        host=Host(name="all up", status=get_host_status_in_css(Status.UP)),
        service=Service(status=get_status_in_css(Status.UP)),
        space=Space(data="7% opt used", status=get_space_status_in_css(Status.OK)),
        sessions=Sessions(
            sessions=[
                get_status_in_css(Status.UP),
                get_status_in_css(Status.UP),
                get_status_in_css(Status.UP),
                get_status_in_css(Status.UP),
                get_status_in_css(Status.UP),
            ]
        ),
    )


def get_status_in_css(status):
    return {
        Status.DOWN: "--down",
        Status.UP: "--up",
        Status.INACTIVE: "--inactive"
    }[status]


def get_host_status_in_css(status):
    return {
        Status.DOWN: "--error",
        Status.UP: "--surface",
        Status.INACTIVE: "--surface",
    }[status]


def get_space_status_in_css(status):
    return {
        Status.DOWN: "--down",
        Status.UP: "--up",
        Status.INACTIVE: "--inactive",
        Status.OK: "--white",
        Status.ERROR: "--error",
    }[status]


if __name__ == "__main__":
    main()
