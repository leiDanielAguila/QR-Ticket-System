import uuid

def generate_id() -> str:
    """
    Generate unique identifier using uuid version 4 
    
    return: 
        UUID V4
    """

    user_id = uuid.uuid4()

    return str(user_id)

