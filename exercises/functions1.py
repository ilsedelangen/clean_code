from datetime import datetime, timedelta


class FunctionExample1:
    """
    ## Original function that we have seen in the slides
    """

    def dir_path(self, start: datetime) -> str:
        # Dummy Function for demonstration purposes
        return start.strftime('%Y_%M_%D_%H')

    def data_paths(self, start: datetime, stop: datetime = None) -> list:
        paths = [self.dir_path(start)]
        if stop is not None:
            one_hour = timedelta(hours=1)
            interim = start + one_hour
            while interim.hour <= stop.hour or interim.day < stop.day:
                paths.append(self.dir_path(interim))
                interim += one_hour
        return paths
