from c3d.src.compiler.expr.finals.enum_datatypes import DataTypes


def fnStrToDatatype(str_datatype: str) -> DataTypes:
    str_datatype = str_datatype.lower()
    if str_datatype == "int":
        return DataTypes.ENTERO
    elif str_datatype == "decimal":
        return DataTypes.DECIMAL
    elif str_datatype == "nvarchar":
        return DataTypes.CADENA
    elif str_datatype == "null":
        return DataTypes.NULL
    elif str_datatype == "bit":
        return DataTypes.BOOLEAN
