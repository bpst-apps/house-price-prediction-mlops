
class Experiment:

    running_status = False

    def __init__(self, experiment_id):
        self.experiment_id = experiment_id

    def __new__(cls, *args, **kwargs):
        if Experiment.running_status:
            raise Exception('Unable to create new experiment as some experiment is already running')
        return super(Experiment, cls).__new__(cls, *args, **kwargs)
    