 # Stiallan Parser

# TOKENS
operator_tokens = ["PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO"]

def inner_bracket(pos, tokens, ast):
    holder = []
    holder.append("start")
    pos += 1
    while tokens[pos].typ != "RBRACKET":
        if tokens[pos].text.isnumeric():
            tokens[pos].text = int(tokens[pos].text)
            holder.append(tokens[pos].text)
            pos += 1
        elif tokens[pos].typ == "LBRACKET":
            result = inner_bracket(pos, tokens, ast)
            pos = result[0]
            holder.append(result[1])
        else:
            holder.append(tokens[pos].text)
            pos += 1


    holder.append("end")
    pos += 1

    return pos, holder

# Functions
def bracket(pos, tokens):
    ast = []
    pos += 1
    ast.append("start")

    while pos < len(tokens):
        if tokens[pos].text.isnumeric():
            tokens[pos].text = int(tokens[pos].text)
            ast.append(tokens[pos].text)
            pos += 1
        elif tokens[pos].typ == "RBRACKET":
            tokens[pos].text = "end"
            ast.append(tokens[pos].text)
            pos += 1
        elif tokens[pos].typ == "LBRACKET":
            result = inner_bracket(pos, tokens, ast)
            pos = result[0]
            ast.append(result[1])
        elif tokens[pos].typ == "DEC":
            ast.append(tokens[pos].typ)
            pos += 1
        elif tokens[pos].typ == "AS":
            ast.append(tokens[pos].typ)
            pos += 1
        else:
            ast.append(tokens[pos].text)
            pos += 1
            

    return ast
