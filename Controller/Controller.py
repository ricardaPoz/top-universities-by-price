from abc import abstractclassmethod, ABC


class ControllerDataBase(ABC):
    @abstractclassmethod
    def get(self, id: int):
        pass

    @abstractclassmethod
    def all(self):
        pass

    @abstractclassmethod
    def add(self, **params: dict):
        pass

    @abstractclassmethod
    def delete(self, id: int):
        pass

    @abstractclassmethod
    def update(self, id: int, **params: dict):
        pass

    @abstractclassmethod
    def all_to_json(self):
        pass

    def _parameter_check(self, name: list, params: dict):
        res = {value: "null" for value in name if value not in params.keys()}
        return (False, list(res.keys())) if len(res) > 0 else (True,)

    def _validation_check(self, **params: dict):
        dict_validation = {}
        for name, value in params.items():
            match value:
                case None:
                    dict_validation[name] = 0
                case str():
                    dict_validation[name] = len(value.strip())
                case int():
                    dict_validation[name] = 1
        return (
            (True,)
            if 0 not in dict_validation.values()
            else (
                False,
                list(
                    dict(
                        filter(lambda k_v: k_v[1] == 0, dict_validation.items())
                    ).keys()
                ),
            )
        )
