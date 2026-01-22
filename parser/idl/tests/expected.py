from ..python_listener import Obj

expected = Obj(
    {
        "name": "root",
        "type": "root",
        "HelloApp": Obj(
            {
                "name": "HelloApp",
                "type": "module",
                "Hello": Obj(
                    {
                        "name": "Hello",
                        "type": "interface",
                        "sayHello": Obj(
                            {
                                "name": "sayHello",
                                "type": "function",
                                "has_oneway": False,
                                "type_spec": "string",
                                "parameters": Obj(
                                    {
                                        "name": "parameters",
                                        "type": "parameters",
                                        "params": [
                                            Obj(
                                                {
                                                    "name": "foo",
                                                    "type": "parameter",
                                                    "inout": "in",
                                                    "type_spec": "uint",
                                                }
                                            ),
                                            Obj(
                                                {
                                                    "name": "bar",
                                                    "type": "parameter",
                                                    "inout": "out",
                                                    "type_spec": "int",
                                                }
                                            ),
                                        ],
                                    }
                                ),
                            }
                        ),
                        "shutdown": Obj(
                            {
                                "name": "shutdown",
                                "type": "function",
                                "has_oneway": True,
                                "type_spec": "void",
                                "parameters": Obj(
                                    {
                                        "name": "parameters",
                                        "type": "parameters",
                                        "params": [],
                                    }
                                ),
                            }
                        ),
                    }
                ),
            }
        ),
    }
)
