from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, ForeignKey, Numeric, Enum, Text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import enum
import urllib.parse

Base = declarative_base()

class RoleEnum(enum.Enum):
    WarehouseStaff = 'WarehouseStaff'
    Manager = 'Manager'
    Supplier = 'Supplier'

class User(Base):
    __tablename__ = 'users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String(50), nullable=False, unique=True)
    PasswordHash = Column(String(128), nullable=False)
    Role = Column(Enum(RoleEnum), nullable=False)
    ContactInfo = Column(String(100))

    # Relationships
    inventory_movements = relationship('InventoryMovement', back_populates='user')
    purchase_orders = relationship('PurchaseOrder', back_populates='manager')
    reorder_thresholds = relationship('ReorderThreshold', back_populates='manager')

class Supplier(Base):
    __tablename__ = 'suppliers'

    SupplierID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    ContactInfo = Column(String(100))
    Address = Column(String(200))

    # Relationships
    products = relationship('Product', back_populates='supplier')
    purchase_orders = relationship('PurchaseOrder', back_populates='supplier')

class Category(Base):
    __tablename__ = 'categories'

    CategoryID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Description = Column(Text)

    # Relationships
    products = relationship('Product', back_populates='category')

class Location(Base):
    __tablename__ = 'locations'

    LocationID = Column(Integer, primary_key=True, autoincrement=True)
    Aisle = Column(String(50))
    Shelf = Column(String(50))
    Bin = Column(String(50))

    # Relationships
    products = relationship('Product', back_populates='location')
    inventory_movements_from = relationship('InventoryMovement', back_populates='from_location', foreign_keys='InventoryMovement.FromLocationID')
    inventory_movements_to = relationship('InventoryMovement', back_populates='to_location', foreign_keys='InventoryMovement.ToLocationID')

class Product(Base):
    __tablename__ = 'products'

    ProductID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Description = Column(Text)
    QuantityInStock = Column(Integer, default=0)
    ReorderLevel = Column(Integer, default=0)

    # Foreign Keys
    CategoryID = Column(Integer, ForeignKey('categories.CategoryID'), nullable=False)
    SupplierID = Column(Integer, ForeignKey('suppliers.SupplierID'), nullable=False)
    LocationID = Column(Integer, ForeignKey('locations.LocationID'), nullable=False)

    # Relationships
    category = relationship('Category', back_populates='products')
    supplier = relationship('Supplier', back_populates='products')
    location = relationship('Location', back_populates='products')
    order_items = relationship('OrderItem', back_populates='product')
    inventory_movements = relationship('InventoryMovement', back_populates='product')
    reorder_threshold = relationship('ReorderThreshold', back_populates='product', uselist=False)

class PurchaseOrderStatusEnum(enum.Enum):
    Pending = 'Pending'
    Approved = 'Approved'
    Received = 'Received'

class PurchaseOrder(Base):
    __tablename__ = 'purchase_orders'

    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    OrderDate = Column(Date, nullable=False)
    Status = Column(Enum(PurchaseOrderStatusEnum), nullable=False, default=PurchaseOrderStatusEnum.Pending)
    TotalAmount = Column(Numeric(12, 2))

    # Foreign Keys
    SupplierID = Column(Integer, ForeignKey('suppliers.SupplierID'), nullable=False)
    ManagerID = Column(Integer, ForeignKey('users.UserID'), nullable=False)

    # Relationships
    supplier = relationship('Supplier', back_populates='purchase_orders')
    manager = relationship('User', back_populates='purchase_orders')
    order_items = relationship('OrderItem', back_populates='purchase_order')

class OrderItem(Base):
    __tablename__ = 'order_items'

    OrderItemID = Column(Integer, primary_key=True, autoincrement=True)
    Quantity = Column(Integer, nullable=False)
    UnitPrice = Column(Numeric(12, 2), nullable=False)

    # Foreign Keys
    OrderID = Column(Integer, ForeignKey('purchase_orders.OrderID'), nullable=False)
    ProductID = Column(Integer, ForeignKey('products.ProductID'), nullable=False)

    # Relationships
    purchase_order = relationship('PurchaseOrder', back_populates='order_items')
    product = relationship('Product', back_populates='order_items')

class MovementTypeEnum(enum.Enum):
    CheckIn = 'Check-In'
    CheckOut = 'Check-Out'
    Transfer = 'Transfer'

class InventoryMovement(Base):
    __tablename__ = 'inventory_movements'

    MovementID = Column(Integer, primary_key=True, autoincrement=True)
    Quantity = Column(Integer, nullable=False)
    MovementDate = Column(DateTime, nullable=False)
    MovementType = Column(Enum(MovementTypeEnum), nullable=False)

    # Foreign Keys
    ProductID = Column(Integer, ForeignKey('products.ProductID'), nullable=False)
    FromLocationID = Column(Integer, ForeignKey('locations.LocationID'), nullable=True)
    ToLocationID = Column(Integer, ForeignKey('locations.LocationID'), nullable=True)
    UserID = Column(Integer, ForeignKey('users.UserID'), nullable=False)

    # Relationships
    product = relationship('Product', back_populates='inventory_movements')
    from_location = relationship('Location', foreign_keys=[FromLocationID], back_populates='inventory_movements_from')
    to_location = relationship('Location', foreign_keys=[ToLocationID], back_populates='inventory_movements_to')
    user = relationship('User', back_populates='inventory_movements')

class ReorderThreshold(Base):
    __tablename__ = 'reorder_thresholds'

    # Composite Primary Key
    ProductID = Column(Integer, ForeignKey('products.ProductID'), primary_key=True)
    ManagerID = Column(Integer, ForeignKey('users.UserID'), primary_key=True)
    ThresholdQuantity = Column(Integer, nullable=False)

    # Relationships
    product = relationship('Product', back_populates='reorder_threshold')
    manager = relationship('User', back_populates='reorder_thresholds')

# URL-encode the password
password = urllib.parse.quote_plus('Gdsc@12012004')

engine = create_engine(f'mysql+pymysql://root:{'Gdsc@12012004'}@localhost:3306/inventory_management', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    connection = engine.connect()
    print("Connection to MySQL database successful!")
    connection.close()
except Exception as e:
    print(f"Error connecting to MySQL database: {e}")
