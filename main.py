from schema import schema

def get_result(query):
    result = schema.execute(query)
    return result