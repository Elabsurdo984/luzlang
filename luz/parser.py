from .tokens import TokenType
from .exceptions import (
    UnexpectedTokenFault, UnexpectedEOFault, StructureFault,
    ParseFault, ExpressionFault, OperatorFault, SyntaxFault
)

class NumberNode:
    def __init__(self, token):
        self.token = token
    def __repr__(self): return f"{self.token.value}"

class StringNode:
    def __init__(self, token):
        self.token = token
    def __repr__(self): return f"\"{self.token.value}\""

class BooleanNode:
    def __init__(self, token):
        self.token = token
    def __repr__(self): return f"{self.token.type.name.lower()}"

class ListNode:
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self): return f"{self.elements}"

class DictNode:
    def __init__(self, pairs):
        self.pairs = pairs # List of (key_node, value_node)
    def __repr__(self): return f"{{{self.pairs}}}"

class IndexAccessNode:
    def __init__(self, base_node, index_node):
        self.base_node = base_node
        self.index_node = index_node
    def __repr__(self): return f"{self.base_node}[{self.index_node}]"

class IndexAssignNode:
    def __init__(self, base_node, index_node, value_node):
        self.base_node = base_node
        self.index_node = index_node
        self.value_node = value_node
    def __repr__(self): return f"({self.base_node}[{self.index_node}] = {self.value_node})"

class UnaryOpNode:
    def __init__(self, op_token, node):
        self.op_token = op_token
        self.node = node
    def __repr__(self): return f"({self.op_token.type.name} {self.node})"

class VarAccessNode:
    def __init__(self, token):
        self.token = token
    def __repr__(self): return f"{self.token.value}"

class VarAssignNode:
    def __init__(self, var_name_token, value_node):
        self.var_name_token = var_name_token
        self.value_node = value_node
    def __repr__(self): return f"({self.var_name_token.value} = {self.value_node})"

class BinOpNode:
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node
    def __repr__(self): return f"({self.left_node} {self.op_token.type.name} {self.right_node})"

class IfNode:
    def __init__(self, cases, else_case):
        self.cases = cases # List of (condition, block)
        self.else_case = else_case # Block

class WhileNode:
    def __init__(self, condition_node, block):
        self.condition_node = condition_node
        self.block = block

class ForNode:
    def __init__(self, var_name_token, start_value_node, end_value_node, block):
        self.var_name_token = var_name_token
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.block = block

class FuncDefNode:
    def __init__(self, name_token, arg_tokens, block):
        self.name_token = name_token
        self.arg_tokens = arg_tokens
        self.block = block

class ReturnNode:
    def __init__(self, expression_node):
        self.expression_node = expression_node

class ImportNode:
    def __init__(self, file_path_token):
        self.file_path_token = file_path_token

class AttemptRescueNode:
    def __init__(self, try_block, error_var_token, catch_block):
        self.try_block = try_block
        self.error_var_token = error_var_token
        self.catch_block = catch_block

class AlertNode:
    def __init__(self, expression_node):
        self.expression_node = expression_node

class BreakNode:
    def __repr__(self): return "break"

class ContinueNode:
    def __repr__(self): return "continue"

class PassNode:
    def __repr__(self): return "pass"

class CallNode:
    def __init__(self, func_name_token, arguments):
        self.func_name_token = func_name_token
        self.arguments = arguments
    def __repr__(self): return f"{self.func_name_token.value}({self.arguments})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]

    def parse(self):
        try:
            return self.statements()
        except UnexpectedTokenFault as e:
            raise e
        except SyntaxFault as e:
            raise e
        except Exception as e:
            raise ParseFault(f"Error while parsing code: {str(e)}")

    def statements(self):
        statements = []
        while self.current_token.type != TokenType.EOF and self.current_token.type != TokenType.RBRACE:
            statements.append(self.statement())
        return statements

    def statement(self):
        if self.current_token.type == TokenType.IF:
            return self.if_expr()
        
        if self.current_token.type == TokenType.WHILE:
            return self.while_expr()
        
        if self.current_token.type == TokenType.FOR:
            return self.for_expr()
        
        if self.current_token.type == TokenType.FUNCTION:
            return self.func_def()
        
        if self.current_token.type == TokenType.RETURN:
            line = self.current_token.line
            self.advance()
            expr = None
            if self.current_token.type not in (TokenType.EOF, TokenType.RBRACE):
                expr = self.expr()
            node = ReturnNode(expr); node.line = line
            return node

        if self.current_token.type == TokenType.IMPORT:
            line = self.current_token.line
            self.advance()
            if self.current_token.type != TokenType.STRING:
                raise UnexpectedTokenFault(f"Expected module path string after 'import', received {self.current_token}")
            path_token = self.current_token
            self.advance()
            node = ImportNode(path_token); node.line = line
            return node

        if self.current_token.type == TokenType.ATTEMPT:
            return self.attempt_rescue_expr()

        if self.current_token.type == TokenType.ALERT:
            line = self.current_token.line
            self.advance()
            expr = self.expr()
            node = AlertNode(expr); node.line = line
            return node

        if self.current_token.type == TokenType.BREAK:
            line = self.current_token.line
            self.advance()
            node = BreakNode(); node.line = line
            return node

        if self.current_token.type == TokenType.CONTINUE:
            line = self.current_token.line
            self.advance()
            node = ContinueNode(); node.line = line
            return node

        if self.current_token.type == TokenType.PASS:
            line = self.current_token.line
            self.advance()
            node = PassNode(); node.line = line
            return node

        if self.current_token.type == TokenType.IDENTIFIER:
            # Lookahead for assignment
            next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            if next_token and next_token.type == TokenType.ASSIGN:
                var_name = self.current_token
                self.advance() # identifier
                self.advance() # =
                expr = self.expr()
                node = VarAssignNode(var_name, expr); node.line = var_name.line
                return node

        node = self.expr()

        # Check for indexing assignment: lista[0] = 5 or dict["key"] = val
        if isinstance(node, IndexAccessNode) and self.current_token.type == TokenType.ASSIGN:
            line = node.line
            self.advance() # =
            value = self.expr()
            assign_node = IndexAssignNode(node.base_node, node.index_node, value)
            assign_node.line = line
            return assign_node

        return node

    def attempt_rescue_expr(self):
        line = self.current_token.line
        self.advance() # attempt
        if self.current_token.type != TokenType.LBRACE:
            raise StructureFault("Expected '{' after attempt")
        self.advance()
        
        try_block = self.statements()
        
        if self.current_token.type == TokenType.EOF:
            raise UnexpectedEOFault("Unexpected end of file in attempt block")
        if self.current_token.type != TokenType.RBRACE:
            raise UnexpectedTokenFault(f"Expected '}}' at the end of attempt block, received {self.current_token}")
        self.advance()
        
        if self.current_token.type != TokenType.RESCUE:
            raise StructureFault("Expected 'rescue' after attempt block")
        self.advance()
        
        if self.current_token.type != TokenType.LPAREN:
            raise StructureFault("Expected '(' after rescue")
        self.advance()
        
        if self.current_token.type != TokenType.IDENTIFIER:
            raise UnexpectedTokenFault("Expected error variable name in rescue")
        error_var = self.current_token
        self.advance()
        
        if self.current_token.type != TokenType.RPAREN:
            raise UnexpectedTokenFault("Expected ')'")
        self.advance()
        
        if self.current_token.type != TokenType.LBRACE:
            raise StructureFault("Expected '{' for rescue block")
        self.advance()
        
        catch_block = self.statements()
        
        if self.current_token.type == TokenType.EOF:
            raise UnexpectedEOFault("Unexpected end of file in rescue block")
        if self.current_token.type != TokenType.RBRACE:
            raise UnexpectedTokenFault(f"Expected '}}' at the end of rescue block, received {self.current_token}")
        self.advance()
        
        node = AttemptRescueNode(try_block, error_var, catch_block); node.line = line
        return node

    def func_def(self):
        line = self.current_token.line
        self.advance() # function
        if self.current_token.type != TokenType.IDENTIFIER:
            raise UnexpectedTokenFault("Expected function name")
        name_token = self.current_token
        self.advance()
        
        if self.current_token.type != TokenType.LPAREN:
            raise StructureFault("Expected '('")
        self.advance()
        
        arg_tokens = []
        if self.current_token.type == TokenType.IDENTIFIER:
            arg_tokens.append(self.current_token)
            self.advance()
            while self.current_token.type == TokenType.COMMA:
                self.advance()
                if self.current_token.type != TokenType.IDENTIFIER:
                    raise UnexpectedTokenFault("Expected argument name")
                arg_tokens.append(self.current_token)
                self.advance()
        
        if self.current_token.type != TokenType.RPAREN:
            raise UnexpectedTokenFault("Expected ')'")
        self.advance()
        
        if self.current_token.type != TokenType.LBRACE:
            raise StructureFault("Expected '{'")
        self.advance()
        
        block = self.statements()
        
        if self.current_token.type == TokenType.EOF:
            raise UnexpectedEOFault("Unexpected end of file in function definition")
        if self.current_token.type != TokenType.RBRACE:
            raise UnexpectedTokenFault("Expected '}'")
        self.advance()
        
        node = FuncDefNode(name_token, arg_tokens, block); node.line = line
        return node

    def if_expr(self):
        line = self.current_token.line
        cases = []
        else_case = None

        self.advance()
        condition = self.expr()
        if self.current_token.type != TokenType.LBRACE:
            raise StructureFault("Expected '{' after if condition")
        self.advance()
        block = self.statements()
        if self.current_token.type != TokenType.RBRACE:
            raise UnexpectedTokenFault("Expected '}' after if block")
        self.advance()
        cases.append((condition, block))

        while self.current_token.type == TokenType.ELIF:
            self.advance()
            condition = self.expr()
            if self.current_token.type != TokenType.LBRACE:
                raise StructureFault("Expected '{' after elif condition")
            self.advance()
            block = self.statements()
            if self.current_token.type != TokenType.RBRACE:
                raise UnexpectedTokenFault("Expected '}' after elif block")
            self.advance()
            cases.append((condition, block))

        if self.current_token.type == TokenType.ELSE:
            self.advance()
            if self.current_token.type != TokenType.LBRACE:
                raise StructureFault("Expected '{' after else")
            self.advance()
            else_case = self.statements()
            if self.current_token.type != TokenType.RBRACE:
                raise UnexpectedTokenFault("Expected '}' after else block")
            self.advance()

        node = IfNode(cases, else_case); node.line = line
        return node

    def while_expr(self):
        line = self.current_token.line
        self.advance() # while
        condition = self.expr()
        if self.current_token.type != TokenType.LBRACE:
            raise StructureFault("Expected '{' after while condition")
        self.advance()
        block = self.statements()
        if self.current_token.type != TokenType.RBRACE:
            raise UnexpectedTokenFault("Expected '}' after while block")
        self.advance()
        node = WhileNode(condition, block); node.line = line
        return node

    def for_expr(self):
        line = self.current_token.line
        self.advance() # for
        if self.current_token.type != TokenType.IDENTIFIER:
            raise UnexpectedTokenFault("Expected variable name after 'for'")
        var_name = self.current_token
        self.advance()
        if self.current_token.type != TokenType.ASSIGN:
            raise StructureFault("Expected '=' after for variable")
        self.advance()
        start_value = self.expr()
        if self.current_token.type != TokenType.TO:
            raise StructureFault("Expected 'to' after for start value")
        self.advance()
        end_value = self.expr()
        if self.current_token.type != TokenType.LBRACE:
            raise StructureFault("Expected '{' after for range")
        self.advance()
        block = self.statements()
        if self.current_token.type != TokenType.RBRACE:
            raise UnexpectedTokenFault("Expected '}' after for block")
        self.advance()
        node = ForNode(var_name, start_value, end_value, block); node.line = line
        return node

    def expr(self):
        return self.logical_or()

    def logical_or(self):
        return self.bin_op(self.logical_and, (TokenType.OR,))

    def logical_and(self):
        return self.bin_op(self.logical_not, (TokenType.AND,))

    def logical_not(self):
        if self.current_token.type == TokenType.NOT:
            op_token = self.current_token
            self.advance()
            return UnaryOpNode(op_token, self.logical_not())
        return self.comp_expr()

    def comp_expr(self):
        return self.bin_op(self.arith_expr, (TokenType.EE, TokenType.NE, TokenType.LT, TokenType.GT, TokenType.LTE, TokenType.GTE))

    def arith_expr(self):
        return self.bin_op(self.term, (TokenType.PLUS, TokenType.MINUS))

    def term(self):
        return self.bin_op(self.power, (TokenType.MUL, TokenType.DIV, TokenType.MOD))

    def power(self):
        base = self.factor()
        if self.current_token.type == TokenType.POW:
            op = self.current_token
            self.advance()
            exp = self.power()  # right-recursive → right-associative
            node = BinOpNode(base, op, exp)
            node.line = op.line
            return node
        return base

    def factor(self):
        token = self.current_token
        node = None

        if token.type == TokenType.MINUS:
            self.advance()
            node = UnaryOpNode(token, self.factor())
            node.line = token.line
            return node

        if token.type in (TokenType.INT, TokenType.FLOAT):
            self.advance()
            node = NumberNode(token)
            node.line = token.line
        elif token.type == TokenType.STRING:
            self.advance()
            node = StringNode(token)
            node.line = token.line
        elif token.type in (TokenType.TRUE, TokenType.FALSE):
            self.advance()
            node = BooleanNode(token)
            node.line = token.line
        elif token.type == TokenType.LBRACKET:
            node = self.list_literal()
        elif token.type == TokenType.LBRACE:
            node = self.dict_literal()
        elif token.type == TokenType.IDENTIFIER:
            node = self.identifier_expr()
        elif token.type == TokenType.LPAREN:
            self.advance()
            node = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                raise UnexpectedTokenFault("Expected ')'")
            self.advance()
        elif token.type == TokenType.EOF:
            raise UnexpectedEOFault("Unexpected end of expression")
        else:
            raise ExpressionFault(f"Invalid expression at token: {token}")

        while self.current_token.type == TokenType.LBRACKET:
            bracket_line = self.current_token.line
            self.advance()
            index = self.expr()
            if self.current_token.type != TokenType.RBRACKET:
                raise UnexpectedTokenFault("Expected ']'")
            self.advance()
            index_node = IndexAccessNode(node, index)
            index_node.line = bracket_line
            node = index_node

        return node

    def identifier_expr(self):
        token = self.current_token
        self.advance()
        if self.current_token.type == TokenType.LPAREN:
            self.advance()
            args = []
            if self.current_token.type != TokenType.RPAREN:
                args.append(self.expr())
                while self.current_token.type == TokenType.COMMA:
                    self.advance()
                    if self.current_token.type == TokenType.RPAREN:
                        break
                    args.append(self.expr())

            if self.current_token.type != TokenType.RPAREN:
                raise UnexpectedTokenFault("Expected ',' or ')'")
            self.advance()
            node = CallNode(token, args); node.line = token.line
            return node
        else:
            node = VarAccessNode(token); node.line = token.line
            return node

    def list_literal(self):
        line = self.current_token.line
        self.advance() # [
        elements = []
        if self.current_token.type != TokenType.RBRACKET:
            elements.append(self.expr())
            while self.current_token.type == TokenType.COMMA:
                self.advance()
                if self.current_token.type == TokenType.RBRACKET:
                    break
                elements.append(self.expr())
        
        if self.current_token.type != TokenType.RBRACKET:
            raise UnexpectedTokenFault("Expected ']' at the end of list")
        self.advance()
        node = ListNode(elements); node.line = line
        return node

    def dict_literal(self):
        line = self.current_token.line
        self.advance() # {
        pairs = []
        if self.current_token.type != TokenType.RBRACE:
            key = self.expr()
            if self.current_token.type != TokenType.COLON:
                raise StructureFault("Expected ':' after dictionary key")
            self.advance()
            value = self.expr()
            pairs.append((key, value))
            
            while self.current_token.type == TokenType.COMMA:
                self.advance()
                if self.current_token.type == TokenType.RBRACE:
                    break
                key = self.expr()
                if self.current_token.type != TokenType.COLON:
                    raise StructureFault("Expected ':' after dictionary key")
                self.advance()
                value = self.expr()
                pairs.append((key, value))
        
        if self.current_token.type != TokenType.RBRACE:
            raise UnexpectedTokenFault("Expected '}' at the end of dictionary")
        self.advance()
        node = DictNode(pairs); node.line = line
        return node

    def bin_op(self, func, ops):
        left = func()
        while self.current_token.type in ops:
            op_token = self.current_token
            self.advance()
            try:
                right = func()
            except ExpressionFault:
                raise OperatorFault(f"Operator '{op_token}' expects a valid expression on the right")
            bin_node = BinOpNode(left, op_token, right)
            bin_node.line = op_token.line
            left = bin_node
        return left
