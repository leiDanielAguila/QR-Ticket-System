import uuid

def generate_id() -> uuid:
    """
    Generate unique identifier using uuid version 4 
    
    return: 
        UUID V4
    """
    return uuid.uuid4()

