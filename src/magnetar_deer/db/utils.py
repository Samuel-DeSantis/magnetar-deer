from sqlalchemy import Integer, String, Float, DateTime, Boolean

def map_type(ftype: str):
    ftype = ftype.lower()

    match ftype:
        case "string" | "str" | "text":
            return String(255)

        case "int" | "integer":
            return Integer

        case "float" | "double" | "decimal":
            return Float

        case "bool" | "boolean":
            return Boolean

        case "datetime" | "date":
            return DateTime

        case _:
            raise ValueError(f"Unknown field type: {ftype}")