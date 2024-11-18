from langchain_core.tools import tool
from core.chatbot.app.retriever import retriever
from core.managment.categories.app.usecases import get_categories_usecase
from shared.db.database import get_db
from typing import Optional, List
from core.managment.products.app.usecases.get_products_usecase import execute as get_products_usecase_execute
from core.managment.products.presenters.dtos.get_products_dto import GetProductsDto
from core.operations.cart.app.usecases import add_item_to_cart_usecase, clean_cart_usecase, get_cart_items_usecase, remove_item_to_cart_usecase, update_item_cart_usecase
from core.operations.cart.presenters.dtos.add_item_to_cart_dto import AddItemToCartDto
from core.operations.cart.presenters.dtos.update_item_cart_dto import UpdateItemCartDto

@tool
def lookup_ask(query: str) -> str:
    """Recibe una consulta acerca de las preguntas frecuentes y devuelve la respuesta más cercana"""
    
    print("Buscando respuesta a la pregunta:", query)
    result = retriever.query(query)
 
    return result

@tool
def get_categories():
    """Devuelve las categorías que hay en la tienda"""
    session = next(get_db())
    result = get_categories_usecase.execute(session)
    
    return [f"{category.name}" for category in result]

@tool
def get_products(
    category_name: Optional[str] = None,
    name: Optional[str] = None,
    range_price: Optional[List[int]] = None,
    color: Optional[str] = None,
    size: Optional[str] = None,
):
    """Busca las ropas que hay en la tienda según los filtros dados
    
    Argumentos:
    category_name (Optional[str]) -- Nombre de la categoría
    name (Optional[str]) -- Nombre del producto
    range_price (Optional[list[int]]) -- Rango de precios, de menor a mayor precio [min, max]
    color (Optional[str]) -- Color del producto
    size (Optional[str]) -- Tamaño del producto, ej: "S", "M", "L"
    
    Retorna:
    list[dict] -- Lista de productos
    """
    session = next(get_db())
    
    filters = GetProductsDto()
    
    if range_price:
        filters.range_price = range_price
    
    if category_name:
        filters.category_name = category_name
    
    if color:
        filters.color = color
    
    if size:
        filters.size = size
    
    if name:
        filters.name = name
    
    result = get_products_usecase_execute(session, filters)

    formated = [
        {
            "item_id": product.id,
            "name": product.name,
            "price": f"S/{product.price} soles",
            "color": product.color,
            "multimedia": product.multimedia,
            "sizes": product.sizes,
        }
        for product in result]
    
    return formated

@tool
def add_to_cart(user_id: int, product_id: int, quantity: int, sizes: dict):
    """ Para agregar un producto al carrito, se necesita el id del usuario, el id del producto, la cantidad y los tamaño de la prenda o prendas, en caso sea un pack
    
    Argumentos:
    user_id (int) -- Id del usuario
    product_id (int) -- Id del producto
    quantity (int) -- Cantidad de productos
    sizes (dict) -- Tamaños de las prenda(s), Ejemplo  En caso sea un pack, puede ser asi. {"polo": "M", "pantalon": "S"}, o puede darse el caso donde solo sea una prenda, {"short": "S"}
    
    Retorna:
    status (bool) -- True si se agrego correctamente, False si no
    
    """
    session = next(get_db())
    
    print({
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "sizes": sizes
    })
    
    result = add_item_to_cart_usecase.execute(session, user_id, AddItemToCartDto(
        product_id=product_id,
        quantity=quantity,
        sizes=sizes
    ))
    
    print(result, "result")
    
    return True

@tool
def remove_from_cart(user_id: int, item_id: int):
    """ Para remover un producto del carrito, se necesita el id del usuario y el id del item en el carrito
    
    Argumentos:
    user_id (int) -- Id del usuario
    item_id (int) -- Id del item en el carrito, no es el id del producto, es el id del item en el carrito. Obtenerlo con get_cart()
    
    Retorna:
    status (bool) -- True si se removio correctamente, False si no
    """
    
    session = next(get_db())
    
    remove_item_to_cart_usecase.execute(session, user_id, item_id)
    
    return True

@tool
def update_item_cart(user_id: int, item_id: int, quantity: Optional[int] = None, sizes: Optional[dict] = None):
    """ Para actualizar un item del carrito, se necesita el id del usuario, el id del item en el carrito, la cantidad (Opcional) y los tamaños de las prenda(s) (Opcional)
    Argumentos:
    user_id (int) -- Id del usuario
    item_id (int) -- Id del item en el carrito
    quantity Optional(int) -- Cantidad de productos (Opcional)
    sizes Optional(dict) -- Tamaños de las prenda(s) (Opcional)
    """
    
    session = next(get_db())
    
    update_item_cart_usecase.execute(session, user_id, UpdateItemCartDto(
        item_id=item_id,
        quantity=quantity,
        sizes=sizes
    ))
    
    return True

@tool
def get_cart(user_id: int):
    """ Para obtener los items del carrito, se necesita el id del usuario
    
    Argumentos:
    user_id (int) -- Id del usuario
    
    Retorna:
     list[dict] -- Lista de items del carrito
     
     
    
    """
    
    session = next(get_db())
    
    result = get_cart_items_usecase.execute(session, user_id)
    
    formated = [
        {
            "id": item.id,
            "product_name": item.products.name,
            "product_price": f"S/{item.products.price} soles",
            "quantity": item.quantity,
            "multimedia": item.products.multimedia,
            "sizes": item.sizes
        }
        for item in result
    ]
    
    print(formated, "formated")
    
    return formated

@tool
def clear_cart(user_id: int):
    """Para limpiar el carrito, se necesita el id del usuario
    
    Argumentos:
    user_id (int) -- Id del usuario
    
    """
    
    session = next(get_db())
    
    clean_cart_usecase.execute(session, user_id)
    
    return True

@tool
def get_cart_total(user_id: int):
    """Para obtener el total del carrito, se necesita el id del usuario
    Argumentos:
    user_id (int) -- Id del usuario
    
    Retorna:
    float -- Total del carrito
    """
    
    session = next(get_db())
    
    result = get_cart_items_usecase.execute(session, user_id)
    
    total = sum([item.products.price * item.quantity for item in result])
    
    return total






####