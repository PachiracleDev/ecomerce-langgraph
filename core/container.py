from fastapi import FastAPI
from core.managment.categories.presenters.controllers.categories_controller import router as categories_router
from core.managment.products.presenters.controllers.product_controller import router as products_router
from core.managment.products.presenters.controllers.uploader_multimedia_controller import router as uploader_multimedia_router
from core.auth.presenters.controllers.auth_controller import router as auth_router
from core.auth.presenters.controllers.user_controller import router as user_router
from core.operations.cart.presenters.controllers.cart_controller import router as cart_router
from core.chatbot.presenters.controllers.web import router as chatbot_web_router

def container_routes(app: FastAPI):
    
    controllers = [categories_router, products_router, auth_router, user_router, uploader_multimedia_router, cart_router, chatbot_web_router]
    
    for c in controllers:
        app.include_router(c)
    