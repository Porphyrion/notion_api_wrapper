from notion_client import Client
from notion_api.objects_helper import Database, DatabaseModel, PageModel, DatabaseEntry

# notion_client = Client(auth="secret_eLliR2BucBAUz2CuPm3KUid9oUJyWltBG9vLQLlrEIT")


class NotionClient:
    DATABASE_FILTER = {"property":"object", "value":"database"}
    

    def __init__(self, auth):
        self.notion_client = Client(auth=auth)

    def get_databases(self): 
        result = []
        for db in self.notion_client.search(filter=NotionClient.DATABASE_FILTER).get("results"):
            db_obj = DatabaseModel(**db)
            result.append(Database(db_obj))
        return result
    
    def get_databases_entries(self, id):
        result = []
        for x in self.notion_client.databases.query(database_id=id).get("results"):
            page_obg = PageModel(**x)
            result.append(DatabaseEntry(page_obg))
        return result
            
    
            
    # def write_new_entrie(self, id):
        
    # 
    # def get_databases_property(self, id):
    #      for db in self.notion_client.search(filter=NotionClient.DATABASE_FILTER).get("results"):
    #         print(db["properties"])

