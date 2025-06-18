from pydantic import BaseModel, Field

class AbandonedCartEvent(BaseModel):
    shop_id: str = Field(..., description="Shop id")
    customer_phone: str = Field(..., description="Phone number")
    cart_id: str
    items: list[dict] = Field(..., description="List of items with name and price")
    total_price: float