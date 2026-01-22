# Generated from ./IDL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IDLParser import IDLParser
else:
    from IDLParser import IDLParser

# This class defines a complete listener for a parse tree produced by IDLParser.
class IDLListener(ParseTreeListener):

    # Enter a parse tree produced by IDLParser#specification.
    def enterSpecification(self, ctx:IDLParser.SpecificationContext):
        pass

    # Exit a parse tree produced by IDLParser#specification.
    def exitSpecification(self, ctx:IDLParser.SpecificationContext):
        pass


    # Enter a parse tree produced by IDLParser#definition.
    def enterDefinition(self, ctx:IDLParser.DefinitionContext):
        pass

    # Exit a parse tree produced by IDLParser#definition.
    def exitDefinition(self, ctx:IDLParser.DefinitionContext):
        pass


    # Enter a parse tree produced by IDLParser#module.
    def enterModule(self, ctx:IDLParser.ModuleContext):
        pass

    # Exit a parse tree produced by IDLParser#module.
    def exitModule(self, ctx:IDLParser.ModuleContext):
        pass


    # Enter a parse tree produced by IDLParser#interface_or_forward_decl.
    def enterInterface_or_forward_decl(self, ctx:IDLParser.Interface_or_forward_declContext):
        pass

    # Exit a parse tree produced by IDLParser#interface_or_forward_decl.
    def exitInterface_or_forward_decl(self, ctx:IDLParser.Interface_or_forward_declContext):
        pass


    # Enter a parse tree produced by IDLParser#interface_decl.
    def enterInterface_decl(self, ctx:IDLParser.Interface_declContext):
        pass

    # Exit a parse tree produced by IDLParser#interface_decl.
    def exitInterface_decl(self, ctx:IDLParser.Interface_declContext):
        pass


    # Enter a parse tree produced by IDLParser#forward_decl.
    def enterForward_decl(self, ctx:IDLParser.Forward_declContext):
        pass

    # Exit a parse tree produced by IDLParser#forward_decl.
    def exitForward_decl(self, ctx:IDLParser.Forward_declContext):
        pass


    # Enter a parse tree produced by IDLParser#interface_header.
    def enterInterface_header(self, ctx:IDLParser.Interface_headerContext):
        pass

    # Exit a parse tree produced by IDLParser#interface_header.
    def exitInterface_header(self, ctx:IDLParser.Interface_headerContext):
        pass


    # Enter a parse tree produced by IDLParser#interface_body.
    def enterInterface_body(self, ctx:IDLParser.Interface_bodyContext):
        pass

    # Exit a parse tree produced by IDLParser#interface_body.
    def exitInterface_body(self, ctx:IDLParser.Interface_bodyContext):
        pass


    # Enter a parse tree produced by IDLParser#export_.
    def enterExport_(self, ctx:IDLParser.Export_Context):
        pass

    # Exit a parse tree produced by IDLParser#export_.
    def exitExport_(self, ctx:IDLParser.Export_Context):
        pass


    # Enter a parse tree produced by IDLParser#interface_inheritance_spec.
    def enterInterface_inheritance_spec(self, ctx:IDLParser.Interface_inheritance_specContext):
        pass

    # Exit a parse tree produced by IDLParser#interface_inheritance_spec.
    def exitInterface_inheritance_spec(self, ctx:IDLParser.Interface_inheritance_specContext):
        pass


    # Enter a parse tree produced by IDLParser#interface_name.
    def enterInterface_name(self, ctx:IDLParser.Interface_nameContext):
        pass

    # Exit a parse tree produced by IDLParser#interface_name.
    def exitInterface_name(self, ctx:IDLParser.Interface_nameContext):
        pass


    # Enter a parse tree produced by IDLParser#a_scoped_name.
    def enterA_scoped_name(self, ctx:IDLParser.A_scoped_nameContext):
        pass

    # Exit a parse tree produced by IDLParser#a_scoped_name.
    def exitA_scoped_name(self, ctx:IDLParser.A_scoped_nameContext):
        pass


    # Enter a parse tree produced by IDLParser#scoped_name.
    def enterScoped_name(self, ctx:IDLParser.Scoped_nameContext):
        pass

    # Exit a parse tree produced by IDLParser#scoped_name.
    def exitScoped_name(self, ctx:IDLParser.Scoped_nameContext):
        pass


    # Enter a parse tree produced by IDLParser#value.
    def enterValue(self, ctx:IDLParser.ValueContext):
        pass

    # Exit a parse tree produced by IDLParser#value.
    def exitValue(self, ctx:IDLParser.ValueContext):
        pass


    # Enter a parse tree produced by IDLParser#value_forward_decl.
    def enterValue_forward_decl(self, ctx:IDLParser.Value_forward_declContext):
        pass

    # Exit a parse tree produced by IDLParser#value_forward_decl.
    def exitValue_forward_decl(self, ctx:IDLParser.Value_forward_declContext):
        pass


    # Enter a parse tree produced by IDLParser#value_box_decl.
    def enterValue_box_decl(self, ctx:IDLParser.Value_box_declContext):
        pass

    # Exit a parse tree produced by IDLParser#value_box_decl.
    def exitValue_box_decl(self, ctx:IDLParser.Value_box_declContext):
        pass


    # Enter a parse tree produced by IDLParser#value_abs_decl.
    def enterValue_abs_decl(self, ctx:IDLParser.Value_abs_declContext):
        pass

    # Exit a parse tree produced by IDLParser#value_abs_decl.
    def exitValue_abs_decl(self, ctx:IDLParser.Value_abs_declContext):
        pass


    # Enter a parse tree produced by IDLParser#value_decl.
    def enterValue_decl(self, ctx:IDLParser.Value_declContext):
        pass

    # Exit a parse tree produced by IDLParser#value_decl.
    def exitValue_decl(self, ctx:IDLParser.Value_declContext):
        pass


    # Enter a parse tree produced by IDLParser#value_header.
    def enterValue_header(self, ctx:IDLParser.Value_headerContext):
        pass

    # Exit a parse tree produced by IDLParser#value_header.
    def exitValue_header(self, ctx:IDLParser.Value_headerContext):
        pass


    # Enter a parse tree produced by IDLParser#value_inheritance_spec.
    def enterValue_inheritance_spec(self, ctx:IDLParser.Value_inheritance_specContext):
        pass

    # Exit a parse tree produced by IDLParser#value_inheritance_spec.
    def exitValue_inheritance_spec(self, ctx:IDLParser.Value_inheritance_specContext):
        pass


    # Enter a parse tree produced by IDLParser#value_name.
    def enterValue_name(self, ctx:IDLParser.Value_nameContext):
        pass

    # Exit a parse tree produced by IDLParser#value_name.
    def exitValue_name(self, ctx:IDLParser.Value_nameContext):
        pass


    # Enter a parse tree produced by IDLParser#value_element.
    def enterValue_element(self, ctx:IDLParser.Value_elementContext):
        pass

    # Exit a parse tree produced by IDLParser#value_element.
    def exitValue_element(self, ctx:IDLParser.Value_elementContext):
        pass


    # Enter a parse tree produced by IDLParser#state_member.
    def enterState_member(self, ctx:IDLParser.State_memberContext):
        pass

    # Exit a parse tree produced by IDLParser#state_member.
    def exitState_member(self, ctx:IDLParser.State_memberContext):
        pass


    # Enter a parse tree produced by IDLParser#init_decl.
    def enterInit_decl(self, ctx:IDLParser.Init_declContext):
        pass

    # Exit a parse tree produced by IDLParser#init_decl.
    def exitInit_decl(self, ctx:IDLParser.Init_declContext):
        pass


    # Enter a parse tree produced by IDLParser#init_param_decls.
    def enterInit_param_decls(self, ctx:IDLParser.Init_param_declsContext):
        pass

    # Exit a parse tree produced by IDLParser#init_param_decls.
    def exitInit_param_decls(self, ctx:IDLParser.Init_param_declsContext):
        pass


    # Enter a parse tree produced by IDLParser#init_param_decl.
    def enterInit_param_decl(self, ctx:IDLParser.Init_param_declContext):
        pass

    # Exit a parse tree produced by IDLParser#init_param_decl.
    def exitInit_param_decl(self, ctx:IDLParser.Init_param_declContext):
        pass


    # Enter a parse tree produced by IDLParser#init_param_attribute.
    def enterInit_param_attribute(self, ctx:IDLParser.Init_param_attributeContext):
        pass

    # Exit a parse tree produced by IDLParser#init_param_attribute.
    def exitInit_param_attribute(self, ctx:IDLParser.Init_param_attributeContext):
        pass


    # Enter a parse tree produced by IDLParser#const_decl.
    def enterConst_decl(self, ctx:IDLParser.Const_declContext):
        pass

    # Exit a parse tree produced by IDLParser#const_decl.
    def exitConst_decl(self, ctx:IDLParser.Const_declContext):
        pass


    # Enter a parse tree produced by IDLParser#const_type.
    def enterConst_type(self, ctx:IDLParser.Const_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#const_type.
    def exitConst_type(self, ctx:IDLParser.Const_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#const_exp.
    def enterConst_exp(self, ctx:IDLParser.Const_expContext):
        pass

    # Exit a parse tree produced by IDLParser#const_exp.
    def exitConst_exp(self, ctx:IDLParser.Const_expContext):
        pass


    # Enter a parse tree produced by IDLParser#or_expr.
    def enterOr_expr(self, ctx:IDLParser.Or_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#or_expr.
    def exitOr_expr(self, ctx:IDLParser.Or_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#xor_expr.
    def enterXor_expr(self, ctx:IDLParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#xor_expr.
    def exitXor_expr(self, ctx:IDLParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#and_expr.
    def enterAnd_expr(self, ctx:IDLParser.And_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#and_expr.
    def exitAnd_expr(self, ctx:IDLParser.And_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#shift_expr.
    def enterShift_expr(self, ctx:IDLParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#shift_expr.
    def exitShift_expr(self, ctx:IDLParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#add_expr.
    def enterAdd_expr(self, ctx:IDLParser.Add_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#add_expr.
    def exitAdd_expr(self, ctx:IDLParser.Add_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#mult_expr.
    def enterMult_expr(self, ctx:IDLParser.Mult_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#mult_expr.
    def exitMult_expr(self, ctx:IDLParser.Mult_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#unary_expr.
    def enterUnary_expr(self, ctx:IDLParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#unary_expr.
    def exitUnary_expr(self, ctx:IDLParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#unary_operator.
    def enterUnary_operator(self, ctx:IDLParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by IDLParser#unary_operator.
    def exitUnary_operator(self, ctx:IDLParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by IDLParser#primary_expr.
    def enterPrimary_expr(self, ctx:IDLParser.Primary_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#primary_expr.
    def exitPrimary_expr(self, ctx:IDLParser.Primary_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#literal.
    def enterLiteral(self, ctx:IDLParser.LiteralContext):
        pass

    # Exit a parse tree produced by IDLParser#literal.
    def exitLiteral(self, ctx:IDLParser.LiteralContext):
        pass


    # Enter a parse tree produced by IDLParser#positive_int_const.
    def enterPositive_int_const(self, ctx:IDLParser.Positive_int_constContext):
        pass

    # Exit a parse tree produced by IDLParser#positive_int_const.
    def exitPositive_int_const(self, ctx:IDLParser.Positive_int_constContext):
        pass


    # Enter a parse tree produced by IDLParser#type_decl.
    def enterType_decl(self, ctx:IDLParser.Type_declContext):
        pass

    # Exit a parse tree produced by IDLParser#type_decl.
    def exitType_decl(self, ctx:IDLParser.Type_declContext):
        pass


    # Enter a parse tree produced by IDLParser#type_declarator.
    def enterType_declarator(self, ctx:IDLParser.Type_declaratorContext):
        pass

    # Exit a parse tree produced by IDLParser#type_declarator.
    def exitType_declarator(self, ctx:IDLParser.Type_declaratorContext):
        pass


    # Enter a parse tree produced by IDLParser#type_spec.
    def enterType_spec(self, ctx:IDLParser.Type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#type_spec.
    def exitType_spec(self, ctx:IDLParser.Type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#simple_type_spec.
    def enterSimple_type_spec(self, ctx:IDLParser.Simple_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#simple_type_spec.
    def exitSimple_type_spec(self, ctx:IDLParser.Simple_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#bitfield_type_spec.
    def enterBitfield_type_spec(self, ctx:IDLParser.Bitfield_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#bitfield_type_spec.
    def exitBitfield_type_spec(self, ctx:IDLParser.Bitfield_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#base_type_spec.
    def enterBase_type_spec(self, ctx:IDLParser.Base_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#base_type_spec.
    def exitBase_type_spec(self, ctx:IDLParser.Base_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#template_type_spec.
    def enterTemplate_type_spec(self, ctx:IDLParser.Template_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#template_type_spec.
    def exitTemplate_type_spec(self, ctx:IDLParser.Template_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#constr_type_spec.
    def enterConstr_type_spec(self, ctx:IDLParser.Constr_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#constr_type_spec.
    def exitConstr_type_spec(self, ctx:IDLParser.Constr_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#simple_declarators.
    def enterSimple_declarators(self, ctx:IDLParser.Simple_declaratorsContext):
        pass

    # Exit a parse tree produced by IDLParser#simple_declarators.
    def exitSimple_declarators(self, ctx:IDLParser.Simple_declaratorsContext):
        pass


    # Enter a parse tree produced by IDLParser#declarators.
    def enterDeclarators(self, ctx:IDLParser.DeclaratorsContext):
        pass

    # Exit a parse tree produced by IDLParser#declarators.
    def exitDeclarators(self, ctx:IDLParser.DeclaratorsContext):
        pass


    # Enter a parse tree produced by IDLParser#declarator.
    def enterDeclarator(self, ctx:IDLParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by IDLParser#declarator.
    def exitDeclarator(self, ctx:IDLParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by IDLParser#simple_declarator.
    def enterSimple_declarator(self, ctx:IDLParser.Simple_declaratorContext):
        pass

    # Exit a parse tree produced by IDLParser#simple_declarator.
    def exitSimple_declarator(self, ctx:IDLParser.Simple_declaratorContext):
        pass


    # Enter a parse tree produced by IDLParser#complex_declarator.
    def enterComplex_declarator(self, ctx:IDLParser.Complex_declaratorContext):
        pass

    # Exit a parse tree produced by IDLParser#complex_declarator.
    def exitComplex_declarator(self, ctx:IDLParser.Complex_declaratorContext):
        pass


    # Enter a parse tree produced by IDLParser#floating_pt_type.
    def enterFloating_pt_type(self, ctx:IDLParser.Floating_pt_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#floating_pt_type.
    def exitFloating_pt_type(self, ctx:IDLParser.Floating_pt_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#integer_type.
    def enterInteger_type(self, ctx:IDLParser.Integer_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#integer_type.
    def exitInteger_type(self, ctx:IDLParser.Integer_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#signed_int.
    def enterSigned_int(self, ctx:IDLParser.Signed_intContext):
        pass

    # Exit a parse tree produced by IDLParser#signed_int.
    def exitSigned_int(self, ctx:IDLParser.Signed_intContext):
        pass


    # Enter a parse tree produced by IDLParser#signed_tiny_int.
    def enterSigned_tiny_int(self, ctx:IDLParser.Signed_tiny_intContext):
        pass

    # Exit a parse tree produced by IDLParser#signed_tiny_int.
    def exitSigned_tiny_int(self, ctx:IDLParser.Signed_tiny_intContext):
        pass


    # Enter a parse tree produced by IDLParser#signed_short_int.
    def enterSigned_short_int(self, ctx:IDLParser.Signed_short_intContext):
        pass

    # Exit a parse tree produced by IDLParser#signed_short_int.
    def exitSigned_short_int(self, ctx:IDLParser.Signed_short_intContext):
        pass


    # Enter a parse tree produced by IDLParser#signed_long_int.
    def enterSigned_long_int(self, ctx:IDLParser.Signed_long_intContext):
        pass

    # Exit a parse tree produced by IDLParser#signed_long_int.
    def exitSigned_long_int(self, ctx:IDLParser.Signed_long_intContext):
        pass


    # Enter a parse tree produced by IDLParser#signed_longlong_int.
    def enterSigned_longlong_int(self, ctx:IDLParser.Signed_longlong_intContext):
        pass

    # Exit a parse tree produced by IDLParser#signed_longlong_int.
    def exitSigned_longlong_int(self, ctx:IDLParser.Signed_longlong_intContext):
        pass


    # Enter a parse tree produced by IDLParser#unsigned_int.
    def enterUnsigned_int(self, ctx:IDLParser.Unsigned_intContext):
        pass

    # Exit a parse tree produced by IDLParser#unsigned_int.
    def exitUnsigned_int(self, ctx:IDLParser.Unsigned_intContext):
        pass


    # Enter a parse tree produced by IDLParser#unsigned_tiny_int.
    def enterUnsigned_tiny_int(self, ctx:IDLParser.Unsigned_tiny_intContext):
        pass

    # Exit a parse tree produced by IDLParser#unsigned_tiny_int.
    def exitUnsigned_tiny_int(self, ctx:IDLParser.Unsigned_tiny_intContext):
        pass


    # Enter a parse tree produced by IDLParser#unsigned_short_int.
    def enterUnsigned_short_int(self, ctx:IDLParser.Unsigned_short_intContext):
        pass

    # Exit a parse tree produced by IDLParser#unsigned_short_int.
    def exitUnsigned_short_int(self, ctx:IDLParser.Unsigned_short_intContext):
        pass


    # Enter a parse tree produced by IDLParser#unsigned_long_int.
    def enterUnsigned_long_int(self, ctx:IDLParser.Unsigned_long_intContext):
        pass

    # Exit a parse tree produced by IDLParser#unsigned_long_int.
    def exitUnsigned_long_int(self, ctx:IDLParser.Unsigned_long_intContext):
        pass


    # Enter a parse tree produced by IDLParser#unsigned_longlong_int.
    def enterUnsigned_longlong_int(self, ctx:IDLParser.Unsigned_longlong_intContext):
        pass

    # Exit a parse tree produced by IDLParser#unsigned_longlong_int.
    def exitUnsigned_longlong_int(self, ctx:IDLParser.Unsigned_longlong_intContext):
        pass


    # Enter a parse tree produced by IDLParser#char_type.
    def enterChar_type(self, ctx:IDLParser.Char_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#char_type.
    def exitChar_type(self, ctx:IDLParser.Char_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#wide_char_type.
    def enterWide_char_type(self, ctx:IDLParser.Wide_char_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#wide_char_type.
    def exitWide_char_type(self, ctx:IDLParser.Wide_char_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#boolean_type.
    def enterBoolean_type(self, ctx:IDLParser.Boolean_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#boolean_type.
    def exitBoolean_type(self, ctx:IDLParser.Boolean_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#octet_type.
    def enterOctet_type(self, ctx:IDLParser.Octet_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#octet_type.
    def exitOctet_type(self, ctx:IDLParser.Octet_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#any_type.
    def enterAny_type(self, ctx:IDLParser.Any_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#any_type.
    def exitAny_type(self, ctx:IDLParser.Any_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#object_type.
    def enterObject_type(self, ctx:IDLParser.Object_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#object_type.
    def exitObject_type(self, ctx:IDLParser.Object_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_decl.
    def enterAnnotation_decl(self, ctx:IDLParser.Annotation_declContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_decl.
    def exitAnnotation_decl(self, ctx:IDLParser.Annotation_declContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_def.
    def enterAnnotation_def(self, ctx:IDLParser.Annotation_defContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_def.
    def exitAnnotation_def(self, ctx:IDLParser.Annotation_defContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_header.
    def enterAnnotation_header(self, ctx:IDLParser.Annotation_headerContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_header.
    def exitAnnotation_header(self, ctx:IDLParser.Annotation_headerContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_inheritance_spec.
    def enterAnnotation_inheritance_spec(self, ctx:IDLParser.Annotation_inheritance_specContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_inheritance_spec.
    def exitAnnotation_inheritance_spec(self, ctx:IDLParser.Annotation_inheritance_specContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_body.
    def enterAnnotation_body(self, ctx:IDLParser.Annotation_bodyContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_body.
    def exitAnnotation_body(self, ctx:IDLParser.Annotation_bodyContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_member.
    def enterAnnotation_member(self, ctx:IDLParser.Annotation_memberContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_member.
    def exitAnnotation_member(self, ctx:IDLParser.Annotation_memberContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_forward_dcl.
    def enterAnnotation_forward_dcl(self, ctx:IDLParser.Annotation_forward_dclContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_forward_dcl.
    def exitAnnotation_forward_dcl(self, ctx:IDLParser.Annotation_forward_dclContext):
        pass


    # Enter a parse tree produced by IDLParser#bitset_type.
    def enterBitset_type(self, ctx:IDLParser.Bitset_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#bitset_type.
    def exitBitset_type(self, ctx:IDLParser.Bitset_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#bitfield.
    def enterBitfield(self, ctx:IDLParser.BitfieldContext):
        pass

    # Exit a parse tree produced by IDLParser#bitfield.
    def exitBitfield(self, ctx:IDLParser.BitfieldContext):
        pass


    # Enter a parse tree produced by IDLParser#bitfield_spec.
    def enterBitfield_spec(self, ctx:IDLParser.Bitfield_specContext):
        pass

    # Exit a parse tree produced by IDLParser#bitfield_spec.
    def exitBitfield_spec(self, ctx:IDLParser.Bitfield_specContext):
        pass


    # Enter a parse tree produced by IDLParser#bitmask_type.
    def enterBitmask_type(self, ctx:IDLParser.Bitmask_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#bitmask_type.
    def exitBitmask_type(self, ctx:IDLParser.Bitmask_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#bit_values.
    def enterBit_values(self, ctx:IDLParser.Bit_valuesContext):
        pass

    # Exit a parse tree produced by IDLParser#bit_values.
    def exitBit_values(self, ctx:IDLParser.Bit_valuesContext):
        pass


    # Enter a parse tree produced by IDLParser#struct_type.
    def enterStruct_type(self, ctx:IDLParser.Struct_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#struct_type.
    def exitStruct_type(self, ctx:IDLParser.Struct_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#member_list.
    def enterMember_list(self, ctx:IDLParser.Member_listContext):
        pass

    # Exit a parse tree produced by IDLParser#member_list.
    def exitMember_list(self, ctx:IDLParser.Member_listContext):
        pass


    # Enter a parse tree produced by IDLParser#member.
    def enterMember(self, ctx:IDLParser.MemberContext):
        pass

    # Exit a parse tree produced by IDLParser#member.
    def exitMember(self, ctx:IDLParser.MemberContext):
        pass


    # Enter a parse tree produced by IDLParser#union_type.
    def enterUnion_type(self, ctx:IDLParser.Union_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#union_type.
    def exitUnion_type(self, ctx:IDLParser.Union_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#switch_type_spec.
    def enterSwitch_type_spec(self, ctx:IDLParser.Switch_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#switch_type_spec.
    def exitSwitch_type_spec(self, ctx:IDLParser.Switch_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#switch_body.
    def enterSwitch_body(self, ctx:IDLParser.Switch_bodyContext):
        pass

    # Exit a parse tree produced by IDLParser#switch_body.
    def exitSwitch_body(self, ctx:IDLParser.Switch_bodyContext):
        pass


    # Enter a parse tree produced by IDLParser#case_stmt.
    def enterCase_stmt(self, ctx:IDLParser.Case_stmtContext):
        pass

    # Exit a parse tree produced by IDLParser#case_stmt.
    def exitCase_stmt(self, ctx:IDLParser.Case_stmtContext):
        pass


    # Enter a parse tree produced by IDLParser#case_label.
    def enterCase_label(self, ctx:IDLParser.Case_labelContext):
        pass

    # Exit a parse tree produced by IDLParser#case_label.
    def exitCase_label(self, ctx:IDLParser.Case_labelContext):
        pass


    # Enter a parse tree produced by IDLParser#element_spec.
    def enterElement_spec(self, ctx:IDLParser.Element_specContext):
        pass

    # Exit a parse tree produced by IDLParser#element_spec.
    def exitElement_spec(self, ctx:IDLParser.Element_specContext):
        pass


    # Enter a parse tree produced by IDLParser#enum_type.
    def enterEnum_type(self, ctx:IDLParser.Enum_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#enum_type.
    def exitEnum_type(self, ctx:IDLParser.Enum_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#enumerator.
    def enterEnumerator(self, ctx:IDLParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by IDLParser#enumerator.
    def exitEnumerator(self, ctx:IDLParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by IDLParser#sequence_type.
    def enterSequence_type(self, ctx:IDLParser.Sequence_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#sequence_type.
    def exitSequence_type(self, ctx:IDLParser.Sequence_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#set_type.
    def enterSet_type(self, ctx:IDLParser.Set_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#set_type.
    def exitSet_type(self, ctx:IDLParser.Set_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#map_type.
    def enterMap_type(self, ctx:IDLParser.Map_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#map_type.
    def exitMap_type(self, ctx:IDLParser.Map_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#string_type.
    def enterString_type(self, ctx:IDLParser.String_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#string_type.
    def exitString_type(self, ctx:IDLParser.String_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#wide_string_type.
    def enterWide_string_type(self, ctx:IDLParser.Wide_string_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#wide_string_type.
    def exitWide_string_type(self, ctx:IDLParser.Wide_string_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#array_declarator.
    def enterArray_declarator(self, ctx:IDLParser.Array_declaratorContext):
        pass

    # Exit a parse tree produced by IDLParser#array_declarator.
    def exitArray_declarator(self, ctx:IDLParser.Array_declaratorContext):
        pass


    # Enter a parse tree produced by IDLParser#fixed_array_size.
    def enterFixed_array_size(self, ctx:IDLParser.Fixed_array_sizeContext):
        pass

    # Exit a parse tree produced by IDLParser#fixed_array_size.
    def exitFixed_array_size(self, ctx:IDLParser.Fixed_array_sizeContext):
        pass


    # Enter a parse tree produced by IDLParser#attr_decl.
    def enterAttr_decl(self, ctx:IDLParser.Attr_declContext):
        pass

    # Exit a parse tree produced by IDLParser#attr_decl.
    def exitAttr_decl(self, ctx:IDLParser.Attr_declContext):
        pass


    # Enter a parse tree produced by IDLParser#except_decl.
    def enterExcept_decl(self, ctx:IDLParser.Except_declContext):
        pass

    # Exit a parse tree produced by IDLParser#except_decl.
    def exitExcept_decl(self, ctx:IDLParser.Except_declContext):
        pass


    # Enter a parse tree produced by IDLParser#op_decl.
    def enterOp_decl(self, ctx:IDLParser.Op_declContext):
        pass

    # Exit a parse tree produced by IDLParser#op_decl.
    def exitOp_decl(self, ctx:IDLParser.Op_declContext):
        pass


    # Enter a parse tree produced by IDLParser#op_attribute.
    def enterOp_attribute(self, ctx:IDLParser.Op_attributeContext):
        pass

    # Exit a parse tree produced by IDLParser#op_attribute.
    def exitOp_attribute(self, ctx:IDLParser.Op_attributeContext):
        pass


    # Enter a parse tree produced by IDLParser#op_type_spec.
    def enterOp_type_spec(self, ctx:IDLParser.Op_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#op_type_spec.
    def exitOp_type_spec(self, ctx:IDLParser.Op_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#parameter_decls.
    def enterParameter_decls(self, ctx:IDLParser.Parameter_declsContext):
        pass

    # Exit a parse tree produced by IDLParser#parameter_decls.
    def exitParameter_decls(self, ctx:IDLParser.Parameter_declsContext):
        pass


    # Enter a parse tree produced by IDLParser#param_decl.
    def enterParam_decl(self, ctx:IDLParser.Param_declContext):
        pass

    # Exit a parse tree produced by IDLParser#param_decl.
    def exitParam_decl(self, ctx:IDLParser.Param_declContext):
        pass


    # Enter a parse tree produced by IDLParser#param_attribute.
    def enterParam_attribute(self, ctx:IDLParser.Param_attributeContext):
        pass

    # Exit a parse tree produced by IDLParser#param_attribute.
    def exitParam_attribute(self, ctx:IDLParser.Param_attributeContext):
        pass


    # Enter a parse tree produced by IDLParser#raises_expr.
    def enterRaises_expr(self, ctx:IDLParser.Raises_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#raises_expr.
    def exitRaises_expr(self, ctx:IDLParser.Raises_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#context_expr.
    def enterContext_expr(self, ctx:IDLParser.Context_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#context_expr.
    def exitContext_expr(self, ctx:IDLParser.Context_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#param_type_spec.
    def enterParam_type_spec(self, ctx:IDLParser.Param_type_specContext):
        pass

    # Exit a parse tree produced by IDLParser#param_type_spec.
    def exitParam_type_spec(self, ctx:IDLParser.Param_type_specContext):
        pass


    # Enter a parse tree produced by IDLParser#fixed_pt_type.
    def enterFixed_pt_type(self, ctx:IDLParser.Fixed_pt_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#fixed_pt_type.
    def exitFixed_pt_type(self, ctx:IDLParser.Fixed_pt_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#fixed_pt_const_type.
    def enterFixed_pt_const_type(self, ctx:IDLParser.Fixed_pt_const_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#fixed_pt_const_type.
    def exitFixed_pt_const_type(self, ctx:IDLParser.Fixed_pt_const_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#value_base_type.
    def enterValue_base_type(self, ctx:IDLParser.Value_base_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#value_base_type.
    def exitValue_base_type(self, ctx:IDLParser.Value_base_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#constr_forward_decl.
    def enterConstr_forward_decl(self, ctx:IDLParser.Constr_forward_declContext):
        pass

    # Exit a parse tree produced by IDLParser#constr_forward_decl.
    def exitConstr_forward_decl(self, ctx:IDLParser.Constr_forward_declContext):
        pass


    # Enter a parse tree produced by IDLParser#import_decl.
    def enterImport_decl(self, ctx:IDLParser.Import_declContext):
        pass

    # Exit a parse tree produced by IDLParser#import_decl.
    def exitImport_decl(self, ctx:IDLParser.Import_declContext):
        pass


    # Enter a parse tree produced by IDLParser#imported_scope.
    def enterImported_scope(self, ctx:IDLParser.Imported_scopeContext):
        pass

    # Exit a parse tree produced by IDLParser#imported_scope.
    def exitImported_scope(self, ctx:IDLParser.Imported_scopeContext):
        pass


    # Enter a parse tree produced by IDLParser#type_id_decl.
    def enterType_id_decl(self, ctx:IDLParser.Type_id_declContext):
        pass

    # Exit a parse tree produced by IDLParser#type_id_decl.
    def exitType_id_decl(self, ctx:IDLParser.Type_id_declContext):
        pass


    # Enter a parse tree produced by IDLParser#type_prefix_decl.
    def enterType_prefix_decl(self, ctx:IDLParser.Type_prefix_declContext):
        pass

    # Exit a parse tree produced by IDLParser#type_prefix_decl.
    def exitType_prefix_decl(self, ctx:IDLParser.Type_prefix_declContext):
        pass


    # Enter a parse tree produced by IDLParser#readonly_attr_spec.
    def enterReadonly_attr_spec(self, ctx:IDLParser.Readonly_attr_specContext):
        pass

    # Exit a parse tree produced by IDLParser#readonly_attr_spec.
    def exitReadonly_attr_spec(self, ctx:IDLParser.Readonly_attr_specContext):
        pass


    # Enter a parse tree produced by IDLParser#readonly_attr_declarator.
    def enterReadonly_attr_declarator(self, ctx:IDLParser.Readonly_attr_declaratorContext):
        pass

    # Exit a parse tree produced by IDLParser#readonly_attr_declarator.
    def exitReadonly_attr_declarator(self, ctx:IDLParser.Readonly_attr_declaratorContext):
        pass


    # Enter a parse tree produced by IDLParser#attr_spec.
    def enterAttr_spec(self, ctx:IDLParser.Attr_specContext):
        pass

    # Exit a parse tree produced by IDLParser#attr_spec.
    def exitAttr_spec(self, ctx:IDLParser.Attr_specContext):
        pass


    # Enter a parse tree produced by IDLParser#attr_declarator.
    def enterAttr_declarator(self, ctx:IDLParser.Attr_declaratorContext):
        pass

    # Exit a parse tree produced by IDLParser#attr_declarator.
    def exitAttr_declarator(self, ctx:IDLParser.Attr_declaratorContext):
        pass


    # Enter a parse tree produced by IDLParser#attr_raises_expr.
    def enterAttr_raises_expr(self, ctx:IDLParser.Attr_raises_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#attr_raises_expr.
    def exitAttr_raises_expr(self, ctx:IDLParser.Attr_raises_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#get_excep_expr.
    def enterGet_excep_expr(self, ctx:IDLParser.Get_excep_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#get_excep_expr.
    def exitGet_excep_expr(self, ctx:IDLParser.Get_excep_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#set_excep_expr.
    def enterSet_excep_expr(self, ctx:IDLParser.Set_excep_exprContext):
        pass

    # Exit a parse tree produced by IDLParser#set_excep_expr.
    def exitSet_excep_expr(self, ctx:IDLParser.Set_excep_exprContext):
        pass


    # Enter a parse tree produced by IDLParser#exception_list.
    def enterException_list(self, ctx:IDLParser.Exception_listContext):
        pass

    # Exit a parse tree produced by IDLParser#exception_list.
    def exitException_list(self, ctx:IDLParser.Exception_listContext):
        pass


    # Enter a parse tree produced by IDLParser#component.
    def enterComponent(self, ctx:IDLParser.ComponentContext):
        pass

    # Exit a parse tree produced by IDLParser#component.
    def exitComponent(self, ctx:IDLParser.ComponentContext):
        pass


    # Enter a parse tree produced by IDLParser#component_forward_decl.
    def enterComponent_forward_decl(self, ctx:IDLParser.Component_forward_declContext):
        pass

    # Exit a parse tree produced by IDLParser#component_forward_decl.
    def exitComponent_forward_decl(self, ctx:IDLParser.Component_forward_declContext):
        pass


    # Enter a parse tree produced by IDLParser#component_decl.
    def enterComponent_decl(self, ctx:IDLParser.Component_declContext):
        pass

    # Exit a parse tree produced by IDLParser#component_decl.
    def exitComponent_decl(self, ctx:IDLParser.Component_declContext):
        pass


    # Enter a parse tree produced by IDLParser#component_header.
    def enterComponent_header(self, ctx:IDLParser.Component_headerContext):
        pass

    # Exit a parse tree produced by IDLParser#component_header.
    def exitComponent_header(self, ctx:IDLParser.Component_headerContext):
        pass


    # Enter a parse tree produced by IDLParser#supported_interface_spec.
    def enterSupported_interface_spec(self, ctx:IDLParser.Supported_interface_specContext):
        pass

    # Exit a parse tree produced by IDLParser#supported_interface_spec.
    def exitSupported_interface_spec(self, ctx:IDLParser.Supported_interface_specContext):
        pass


    # Enter a parse tree produced by IDLParser#component_inheritance_spec.
    def enterComponent_inheritance_spec(self, ctx:IDLParser.Component_inheritance_specContext):
        pass

    # Exit a parse tree produced by IDLParser#component_inheritance_spec.
    def exitComponent_inheritance_spec(self, ctx:IDLParser.Component_inheritance_specContext):
        pass


    # Enter a parse tree produced by IDLParser#component_body.
    def enterComponent_body(self, ctx:IDLParser.Component_bodyContext):
        pass

    # Exit a parse tree produced by IDLParser#component_body.
    def exitComponent_body(self, ctx:IDLParser.Component_bodyContext):
        pass


    # Enter a parse tree produced by IDLParser#component_export.
    def enterComponent_export(self, ctx:IDLParser.Component_exportContext):
        pass

    # Exit a parse tree produced by IDLParser#component_export.
    def exitComponent_export(self, ctx:IDLParser.Component_exportContext):
        pass


    # Enter a parse tree produced by IDLParser#provides_decl.
    def enterProvides_decl(self, ctx:IDLParser.Provides_declContext):
        pass

    # Exit a parse tree produced by IDLParser#provides_decl.
    def exitProvides_decl(self, ctx:IDLParser.Provides_declContext):
        pass


    # Enter a parse tree produced by IDLParser#interface_type.
    def enterInterface_type(self, ctx:IDLParser.Interface_typeContext):
        pass

    # Exit a parse tree produced by IDLParser#interface_type.
    def exitInterface_type(self, ctx:IDLParser.Interface_typeContext):
        pass


    # Enter a parse tree produced by IDLParser#uses_decl.
    def enterUses_decl(self, ctx:IDLParser.Uses_declContext):
        pass

    # Exit a parse tree produced by IDLParser#uses_decl.
    def exitUses_decl(self, ctx:IDLParser.Uses_declContext):
        pass


    # Enter a parse tree produced by IDLParser#emits_decl.
    def enterEmits_decl(self, ctx:IDLParser.Emits_declContext):
        pass

    # Exit a parse tree produced by IDLParser#emits_decl.
    def exitEmits_decl(self, ctx:IDLParser.Emits_declContext):
        pass


    # Enter a parse tree produced by IDLParser#publishes_decl.
    def enterPublishes_decl(self, ctx:IDLParser.Publishes_declContext):
        pass

    # Exit a parse tree produced by IDLParser#publishes_decl.
    def exitPublishes_decl(self, ctx:IDLParser.Publishes_declContext):
        pass


    # Enter a parse tree produced by IDLParser#consumes_decl.
    def enterConsumes_decl(self, ctx:IDLParser.Consumes_declContext):
        pass

    # Exit a parse tree produced by IDLParser#consumes_decl.
    def exitConsumes_decl(self, ctx:IDLParser.Consumes_declContext):
        pass


    # Enter a parse tree produced by IDLParser#home_decl.
    def enterHome_decl(self, ctx:IDLParser.Home_declContext):
        pass

    # Exit a parse tree produced by IDLParser#home_decl.
    def exitHome_decl(self, ctx:IDLParser.Home_declContext):
        pass


    # Enter a parse tree produced by IDLParser#home_header.
    def enterHome_header(self, ctx:IDLParser.Home_headerContext):
        pass

    # Exit a parse tree produced by IDLParser#home_header.
    def exitHome_header(self, ctx:IDLParser.Home_headerContext):
        pass


    # Enter a parse tree produced by IDLParser#home_inheritance_spec.
    def enterHome_inheritance_spec(self, ctx:IDLParser.Home_inheritance_specContext):
        pass

    # Exit a parse tree produced by IDLParser#home_inheritance_spec.
    def exitHome_inheritance_spec(self, ctx:IDLParser.Home_inheritance_specContext):
        pass


    # Enter a parse tree produced by IDLParser#primary_key_spec.
    def enterPrimary_key_spec(self, ctx:IDLParser.Primary_key_specContext):
        pass

    # Exit a parse tree produced by IDLParser#primary_key_spec.
    def exitPrimary_key_spec(self, ctx:IDLParser.Primary_key_specContext):
        pass


    # Enter a parse tree produced by IDLParser#home_body.
    def enterHome_body(self, ctx:IDLParser.Home_bodyContext):
        pass

    # Exit a parse tree produced by IDLParser#home_body.
    def exitHome_body(self, ctx:IDLParser.Home_bodyContext):
        pass


    # Enter a parse tree produced by IDLParser#home_export.
    def enterHome_export(self, ctx:IDLParser.Home_exportContext):
        pass

    # Exit a parse tree produced by IDLParser#home_export.
    def exitHome_export(self, ctx:IDLParser.Home_exportContext):
        pass


    # Enter a parse tree produced by IDLParser#factory_decl.
    def enterFactory_decl(self, ctx:IDLParser.Factory_declContext):
        pass

    # Exit a parse tree produced by IDLParser#factory_decl.
    def exitFactory_decl(self, ctx:IDLParser.Factory_declContext):
        pass


    # Enter a parse tree produced by IDLParser#finder_decl.
    def enterFinder_decl(self, ctx:IDLParser.Finder_declContext):
        pass

    # Exit a parse tree produced by IDLParser#finder_decl.
    def exitFinder_decl(self, ctx:IDLParser.Finder_declContext):
        pass


    # Enter a parse tree produced by IDLParser#event.
    def enterEvent(self, ctx:IDLParser.EventContext):
        pass

    # Exit a parse tree produced by IDLParser#event.
    def exitEvent(self, ctx:IDLParser.EventContext):
        pass


    # Enter a parse tree produced by IDLParser#event_forward_decl.
    def enterEvent_forward_decl(self, ctx:IDLParser.Event_forward_declContext):
        pass

    # Exit a parse tree produced by IDLParser#event_forward_decl.
    def exitEvent_forward_decl(self, ctx:IDLParser.Event_forward_declContext):
        pass


    # Enter a parse tree produced by IDLParser#event_abs_decl.
    def enterEvent_abs_decl(self, ctx:IDLParser.Event_abs_declContext):
        pass

    # Exit a parse tree produced by IDLParser#event_abs_decl.
    def exitEvent_abs_decl(self, ctx:IDLParser.Event_abs_declContext):
        pass


    # Enter a parse tree produced by IDLParser#event_decl.
    def enterEvent_decl(self, ctx:IDLParser.Event_declContext):
        pass

    # Exit a parse tree produced by IDLParser#event_decl.
    def exitEvent_decl(self, ctx:IDLParser.Event_declContext):
        pass


    # Enter a parse tree produced by IDLParser#event_header.
    def enterEvent_header(self, ctx:IDLParser.Event_headerContext):
        pass

    # Exit a parse tree produced by IDLParser#event_header.
    def exitEvent_header(self, ctx:IDLParser.Event_headerContext):
        pass


    # Enter a parse tree produced by IDLParser#annapps.
    def enterAnnapps(self, ctx:IDLParser.AnnappsContext):
        pass

    # Exit a parse tree produced by IDLParser#annapps.
    def exitAnnapps(self, ctx:IDLParser.AnnappsContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_appl.
    def enterAnnotation_appl(self, ctx:IDLParser.Annotation_applContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_appl.
    def exitAnnotation_appl(self, ctx:IDLParser.Annotation_applContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_appl_params.
    def enterAnnotation_appl_params(self, ctx:IDLParser.Annotation_appl_paramsContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_appl_params.
    def exitAnnotation_appl_params(self, ctx:IDLParser.Annotation_appl_paramsContext):
        pass


    # Enter a parse tree produced by IDLParser#annotation_appl_param.
    def enterAnnotation_appl_param(self, ctx:IDLParser.Annotation_appl_paramContext):
        pass

    # Exit a parse tree produced by IDLParser#annotation_appl_param.
    def exitAnnotation_appl_param(self, ctx:IDLParser.Annotation_appl_paramContext):
        pass


    # Enter a parse tree produced by IDLParser#identifier.
    def enterIdentifier(self, ctx:IDLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by IDLParser#identifier.
    def exitIdentifier(self, ctx:IDLParser.IdentifierContext):
        pass



del IDLParser