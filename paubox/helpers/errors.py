"""
Handle Error responses from the Paubox API.
"""
def handle_error(error):
    """
    Print Response error from Paubox API and return error.
    """
    print(error.response.text)
    return error
