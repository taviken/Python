from .generated.IDLListener import IDLListener
from collections import OrderedDict
from pprint import pprint
from io import StringIO
from .generated.IDLParser import IDLParser


class Obj(OrderedDict):

    def __getattr__(self, name):
        return self.get(name)

    def __setattr__(self, name, value):
        return self.update({name: value})

    def __format__(self, format_spec):
        if format_spec.lower() == "pretty":
            s = StringIO()
            pprint(self, s)
            return s.getvalue()
        else:
            return super().__format__(format_spec)


class PythonListener(IDLListener):
    def __init__(self):
        super().__init__()
        self.root = Obj("root", "root")
        self.depth = [self.root]
        # self._current_obj = self.root

    def _handle_exit(self):
        last_obj = self.depth.pop()
        obj = self.depth[-1]
        setattr(obj, last_obj.name, last_obj)

    def enterModule(self, ctx: IDLParser.ModuleContext):
        ID = ctx.identifier().getText()
        obj = Obj(ID, "module")
        self.depth.append(obj)

    def exitModule(self, ctx):
        self._handle_exit()

    def enterInterface_decl(self, ctx: IDLParser.Interface_declContext):
        ID = ctx.interface_header().identifier().getText()
        obj = Obj(ID, "interface")
        self.depth.append(obj)

    def exitInterface_decl(self, ctx):
        self._handle_exit()

    def enterOp_decl(self, ctx: IDLParser.Op_declContext):
        ID = ctx.identifier().getText()
        obj = Obj(ID, "function")

        obj.has_oneway = ctx.op_attribute() is not None
        obj.type_spec = ctx.op_type_spec().getText()

        self.depth.append(obj)

    def exitOp_decl(self, ctx):
        self._handle_exit()

    def enterParameter_decls(self, ctx: IDLParser.Parameter_declsContext):

        params = []
        for param in ctx.param_decl():
            ID = param.simple_declarator().getText()
            obj = Obj(ID, "parameter")
            obj.inout = param.param_attribute().getText()
            obj.type_spec = param.param_type_spec().getText()
            params.append(obj)
        parameters = Obj("parameters", "parameters")
        parameters.params = params
        self.depth.append(parameters)

    def exitParameter_decls(self, ctx):
        self._handle_exit()


__all__ = [
    "Obj",
    "PythonListener",
]
