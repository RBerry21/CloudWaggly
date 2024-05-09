import azure.functions as func
from azure.functions.decorators.core import DataType
import logging
import uuid
import json

app = func.FunctionApp()
# Register New Dog and Owner
@app.function_name(name="adddog")
@app.route(route="adddog", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET", "POST"])
@app.generic_output_binding(arg_name="adddog", type="sql", CommandText="dbo.dogowners", ConnectionStringSetting="SqlConnectionString", data_type=DataType.STRING)
def adddog(req: func.HttpRequest, adddog: func.Out[func.SqlRow]) -> func.HttpResponse:
    req_data = json.loads(req.get_body().decode("utf-8"))
    customer_name = req_data.get("customer_name")
    dog_name = req_data.get("dog_name")
    customer_postcode = req_data.get("customer_postcode")
    customer_number = req_data.get("customer_number")
    customer_email = req_data.get("customer_email")
    
    if customer_name:
        adddog.set(func.SqlRow({"dog_id": str(uuid.uuid4()), "customer_name": customer_name, "dog_name": dog_name, "customer_postcode": customer_postcode, "customer_number": customer_number, "customer_email": customer_email}))
        return func.HttpResponse(f"Thank you for registering with Wagg.ly! Your details have been added, we will contact you soon!")
    else:
        return func.HttpResponse("There seems to have been an issue, please check your details and try again.", status_code=400)

# Register New Dog Walker

@app.function_name(name="addwalker")
@app.route(route="addwalker", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET", "POST"])
@app.generic_output_binding(arg_name="addwalker", type="sql", CommandText="dbo.dogwalkers", ConnectionStringSetting="SqlConnectionString", data_type=DataType.STRING)
def addwalker(req: func.HttpRequest, addwalker: func.Out[func.SqlRow]) -> func.HttpResponse:
    req_data = json.loads(req.get_body().decode("utf-8"))
    walker_name = req_data.get("walker_name")
    walker_postcode = req_data.get("walker_postcode")
    walker_number = req_data.get("walker_number")
    walker_email = req_data.get("walker_email")
    if walker_name:
        addwalker.set(func.SqlRow({"walker_id": str(uuid.uuid4()), "walker_name": walker_name,"walker_postcode": walker_postcode, "walker_number": walker_number, "walker_email": walker_email}))
        return func.HttpResponse(f"Thank you for registering with Wagg.ly! Your details have been added, we will contact you soon!")
    else:
        return func.HttpResponse("There seems to have been an issue, please check your details and try again.", status_code=400)
    




