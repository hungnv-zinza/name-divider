from namedivider import GBDTNameDivider

def handler(event, context):
    gbdt_divider = GBDTNameDivider()
    divide_name = gbdt_divider.divide_name(event["name"]).to_dict()
    return [divide_name["family"], divide_name["given"]]

    