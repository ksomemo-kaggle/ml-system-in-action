import enum


class PLATFORM_ENUM(enum.Enum):
    DOCKER_COMPOSE = 'docker_compose'
    KUBERNETES = 'kubernetes'


class PHYSICAL_SAVE_DATA(enum.Enum):
    NO_SAVE = 0
    SAVE = 1


class PREDICTION_TYPE(enum.Enum):
    CLASSIFICATION = 'classification'
    REGRESSION = 'regression'


class MODEL_RUNTIME(enum.Enum):
    SKLEARN = 'sklearn'
    ONNX_RUNTIME = 'onnx_runtime'


class DATA_TYPE(enum.Enum):
    ARRAY = 'array'
    IMAGE = 'image'
    STRING = 'string'


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


class _Constants(object):
    @constant
    def MODEL_DIRECTORY():
        return '/serving_patterns/app/ml/models/'

    @constant
    def DATA_DIRECTORY():
        return '/serving_patterns/app/data/'

    @constant
    def DATA_FILE_DIRECTORY():
        return '/serving_patterns/app/data/file/'

    @constant
    def MODEL_EXTENTIONS():
        return ['pkl', 'h5', 'hdf5']

    @constant
    def REDIS_INCREMENTS():
        return 'increments'

    @constant
    def REDIS_QUEUE():
        return 'queue'

    @constant
    def PREDICTION_DEFAULT():
        return -1

    @constant
    def SEPARATOR():
        return ';'


CONSTANTS = _Constants()