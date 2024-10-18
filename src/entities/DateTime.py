from datetime import datetime, timezone

class DateTime:
    def __init__(self, dateTime: str):
        if dateTime == None: raise ValueError("DateTime invalido.")
        
        try:
            self._value = datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S.%f%z')
        except:
            raise ValueError("formato de data invalido, utilize %Y-%m-%dT%H:%M:%S.%f%z.")
    
    @property
    def value(self) -> datetime:
        return self._value
    