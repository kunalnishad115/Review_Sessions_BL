# ● id → int
# ● name → string (required)
# ● description → string (optional)
# ● price → float (> 0)
# ● stock → int (>= 0)
# ● category → string (example: electronics, clothing)

from pydantic import BaseModel,Field

class Product(BaseModel):
    id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., gt=0, description="Product price")
    description: str = Field(None, description="Product description")
    stock: int = Field(..., ge=0, description="Product stock")
    category: str = Field(..., description="Product category")