from typing import List, Dict, Optional
from aws_lambda_powertools.utilities.parser import BaseModel

def to_lower_camel_case(snake_input: str) -> str:
    """
    utility to convert snake to lower camel case
    """
    first, *others = snake_input.split('_')
    return ''.join([first,*map(str.capitalize, others)])

class RequestsBaseModel(BaseModel):
    """
    Args:
        BaseModel
    """
    alias_generator = to_lower_camel_case
    allow_population_by_field_name = True

class GetTempRequest(BaseModel):
    """
    Args:
    Returns:
    """
    sensor_id: str
    
