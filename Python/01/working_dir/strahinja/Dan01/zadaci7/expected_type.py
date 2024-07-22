def expected_type(*types):
    def check(f):
        def fn(*args, **kwargs):
            if len(args) != len(types):
                raise AttributeError("Incorrect number of arguments")

            for arg, expected_types in zip(args, types):
                if not any(isinstance(arg, expected) for expected in expected_types):
                    expected_type_names = ', '.join(t.__name__ for t in expected_types)
                    raise AttributeError(f"Invalid argument type: {type(arg).__name__} not in ({expected_type_names})")

            return f(*args, **kwargs)

        return fn

    return check