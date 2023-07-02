from pydantic import BaseModel
from abc import ABC, abstractmethod



class BaseEval(ABC, BaseModel):
    eval_class: str
    eval_subclass: str
    

    @abstractmethod
    def evaluate(self, *args, **kwargs):
        pass

    
