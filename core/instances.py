

def init_db():
    from core.managment.categories.domain import category_model
    from core.managment.products.domain import product_model
    from core.auth.domain import user_schema
    from core.auth.domain import user_billing_schema
    from core.operations.cart.domain import cart_schema
    from core.operations.cart.domain import cart_item_schema
    
    from shared.db.database import engine
    category_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)
    user_schema.Base.metadata.create_all(bind=engine)
    user_billing_schema.Base.metadata.create_all(bind=engine)
    cart_schema.Base.metadata.create_all(bind=engine)
    cart_item_schema.Base.metadata.create_all(bind=engine)