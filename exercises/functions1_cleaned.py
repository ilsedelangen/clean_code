from datetime import datetime, timedelta


class CleanedFunctionExample1:
    """
    ## Cleaned version that we have seen in the slides

    - IOSP compliant
    - Structure is visible
    - Method names are verbs now
    - Methods do one thing
    - Still not perfect:
        - Extract _generate_hourly_steps to another class (it is fully independent now)
        - Local steps variable
    """

    def generate_path(self, start: datetime) -> str:
        # Dummy Function for demonstration purposes
        return start.strftime('%Y_%M_%D_%H')

    def generate_paths_for_timespan(self, start: datetime, stop: datetime = None) -> list:
        steps = self._generate_hourly_steps(start, stop)
        return self._generate_paths(steps)

    def _generate_paths(self, times: list) -> list:
        return [self.generate_path(t) for t in times]

    def _generate_hourly_steps(self, start: datetime, stop: datetime = None) -> list:
        time_steps = [start]
        if stop is None:
            return time_steps

        one_hour = timedelta(hours=1)
        current_step = start + one_hour
        while current_step.hour <= stop.hour or current_step.day < stop.day:
            time_steps.append(current_step)
            current_step += one_hour
        return time_steps