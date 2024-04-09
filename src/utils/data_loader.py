import numpy as np
import json
from typing import Dict


def import_instance(instance_path: str) -> Dict[str, np.ndarray | int]:
    try:
        with open(instance_path, "r") as file:
            instance = json.load(file)
            return instance
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except Exception as e:
        print(e)
        raise ValueError("Error")
