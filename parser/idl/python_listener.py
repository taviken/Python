from .generated.IDLParser import IDLParser
from .generated.IDLListener import IDLListener
from pprint import pprint
from io import StringIO
from collections import OrderedDict


class Obj(OrderedDict):
    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, attr, value):
        self.update({attr: value})

    def __format__(self, format_spec):
        if format_spec.lower() == "pretty":
            s = StringIO()
            pprint(self, s)
            return s.getvalue()
        else:
            return super().__format__(format_spec)


class PythonIdlListener(IDLListener):
    def __init__(self):
        super().__init__()

        obj = Obj()

        self.root_obj = obj
        self.depth = [obj]

    def _handle_exit(self):
        last_obj = self.depth.pop()
        temp = self.depth[-1]
        setattr(temp, last_obj.name, last_obj)

    def enterModule(self, ctx: IDLParser.ModuleContext):

        ID = ctx.identifier().getText()
        newobj = Obj()

        setattr(newobj, "name", ID)
        setattr(newobj, "type", "module")
        self.depth.append(newobj)

    def exitModule(self, ctx):
        last_module = self.depth.pop()
        temp = self.depth[-1]
        setattr(temp, last_module.name, last_module)

    def enterInterface_decl(self, ctx: IDLParser.Interface_declContext):
        ID = ctx.interface_header().identifier().getText()
        newobj = Obj()
        newobj.name = ID
        newobj.type = "interface"
        self.depth.append(newobj)

    def exitInterface_decl(self, ctx):

        self._handle_exit()

    def enterOp_decl(self, ctx: IDLParser.Op_declContext):
        ID = ctx.identifier().getText()
        return_type = ctx.op_type_spec().getText()
        newobj = Obj()
        newobj.name = ID
        newobj.type = "operation"
        newobj.return_type = return_type

        self.depth.append(newobj)

    def exitOp_decl(self, ctx):
        ID = ctx.identifier().getText()
        self._handle_exit()

    def enterParameter_decls(self, ctx: IDLParser.Parameter_declsContext):

        params = []
        for param in ctx.param_decl():
            type_ = param.param_type_spec().getText()
            text = param.simple_declarator().getText()
            attr = param.param_attribute().getText()
            params.append({"type": type_, "identifier": text, "inout": attr})

        parameters = Obj()
        parameters.name = "parameters"
        parameters.type = "parameters"
        parameters.params = params
        self.depth.append(parameters)

    def exitParameter_decls(self, ctx):
        self._handle_exit()

    def enterType_declarator(self, ctx: IDLParser.Type_declaratorContext):
        type_spec = ctx.type_spec().getText()
        ID = ctx.declarators().getText()
        newobj = Obj()
        newobj.name = ID
        newobj.type = "typedef"
        newobj.type_spec = type_spec
        self.depth.append(newobj)

    def exitType_declarator(self, ctx):
        self._handle_exit()

    def enterStruct_type(self, ctx: IDLParser.Struct_typeContext):
        def handle_member(member: IDLParser.DeclaratorContext):
            memobj = Obj()
            type_spec = member.type_spec().getText()
            if member.declarators().declarator()[0].simple_declarator() is not None:
                memID = (
                    member.declarators().declarator()[0].simple_declarator().getText()
                )
            else:
                comp = (
                    member.declarators()
                    .declarator()[0]
                    .complex_declarator()
                    .array_declarator()
                )
                memID = comp.ID().getText()
                fixed_size = comp.fixed_array_size()
                memobj.fixed_array = [
                    int(x.positive_int_const().getText()) for x in fixed_size
                ]
                memobj.name = memID

            memobj.name = memID
            memobj.type = "struct_member"
            memobj.type_spec = type_spec
            return memobj

        ID = ctx.identifier().getText()
        newobj = Obj()
        newobj.name = ID
        newobj.type = "struct"
        members = Obj()
        for member in ctx.member_list().member():
            memobj = handle_member(member)
            members[memobj.name] = memobj
        newobj.members = members
        self.depth.append(newobj)

    def exitStruct_type(self, ctx):
        self._handle_exit()

    def enterAttr_decl(self, ctx):

        breakpoint()


__all__ = [
    "PythonIdlListener",
    "Obj",
]
