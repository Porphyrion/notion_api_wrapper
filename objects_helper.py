from pydantic import BaseModel, ConfigDict, validator
from typing import List, Optional

class ObjectBase:
    model_config = ConfigDict(extra='ignore', arbitrary_types_allowed=True) 
    
class RichTextModel(BaseModel, ObjectBase):
    plain_text: str
    
class EmojiModel(BaseModel, ObjectBase):
    type: str
    emoji: str

class DatabaseModel(BaseModel, ObjectBase):
    id: str
    properties: List[str] 
    title: List[RichTextModel]
    properties: object
    
class PageModel(BaseModel, ObjectBase):
    id: str
    icon: Optional[EmojiModel]
    properties: object
    
    @validator('icon', pre=True, always=True)
    def validate_icon(cls, v):
        if isinstance(v, EmojiModel):
            return v
        if isinstance(v, dict):
            try:
                return EmojiModel(**v)
            except ValueError:
                pass
        return None


class Property:
    def __init__(self, property_obj):
        self.__type = property_obj["type"]
        self.__isSelect = self.__type == "select" or self.__type =="multi_select"
        self.__options = [] if not self.__isSelect else property_obj[self.__type]["options"]
    
    def get_type(self) -> str:
        return self.__type
    
    def get_options(self) -> []:
        return self.__options
    
    def is_select(self) -> bool:
        return self.__isSelect

class Database:
    def __init__(self, db_model):
        self.__database_model = db_model
        self.__properties = {}
        for key, value in db_model.properties.items():
            self.__properties[key] = Property(value)
    
    # should I throw exeption？ 
    def get_name(self) -> str:
        return self.__database_model.title[0].plain_text
    
    def get_id(self) -> str:
        return self.__database_model.id
    
    def get_properties_names(self) -> List[str]:
        return self.__properties.keys()
       
class DatabaseEntry:
    def __init__(self, page_model):
        self.__page_model = page_model
        
    def get_raw_property_value(self, property_name: str) -> str:
        return self.__page_model.properties[property_name]; 
    # def get_title(self) -> str:
    #     
    # def get_property_value(self, property_name) -> str:
    #         
    # def get_icon(self) -> str:
        

        
    

    
    

    
    
