class SingletonMeta(type):
    _class_instances = dict()

    def __call__(cls, *args, **kwargs):
        if not cls in cls._class_instances:
            new_instance = super().__call__(*args, **kwargs)
            cls._class_instances[cls] = new_instance
        return cls._class_instances[cls]
