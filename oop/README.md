# More about OOP.

### book_class.py

- *a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).*

##### Attributes:
- `title` (str): The title of the book.
- `author` (str): The author of the book.
- `year` (int): The publication year of the book.

##### Magic Methods:

- Constructor (`__init__`): Initializes a `Book` instance with `title`, `author`, and `year`.
- Destructor (`__del__`): Prints `"Deleting (title of the book)"` upon object deletion.
- String Representation (`__str__`): Returns a string in the format `"(title) by (author), published in (year)"`.
- Official Representation (`__repr__`): Returns a string that would recreate the Book instance: `f"Book('{self.title}', '{self.author}', {self.year})"`.

### library_system.py

- *a system that models a library with different types of books.*

##### Base Class - `Book`:

- Attributes: `title` (str) and `author` (str).
- Method: `__init__(self, title, author)` for initializing book attributes.

##### Derived Classes - `EBook` and `PrintBook`:

- Both classes inherit from `Book`.
- `EBook` additional attribute: `file_size (int)`.
- `PrintBook` additional attribute: `page_count (int)`.
- Each derived class should have its own `__init__` method that properly calls the base class `__init__` while also initializing its unique attribute.

##### Composition - Library:

- Attributes: `books` (a list to store instances of `Book`, `EBook`, and `PrintBook`).
- Methods:
    - `add_book(self, book)`: Adds a `Book`, `EBook`, or `PrintBook` instance to the library.
    - `list_books(self)`: Prints details of each book in the library.

### polymorphism_demo.py

- *a set of classes that demonstrate method overriding and polymorphic behavior.*

##### Base Class - `Shape`:

- Method: `area(self)`, which simply raises a `NotImplementedError`, indicating that derived classes need to override this method.

##### Derived Class - `Rectangle`:

- Inherits from `Shape`.
- Attributes: `length` and `width`.
- Overrides the `area()` method to calculate the rectangle’s area using the formula: *length × width*.

##### Derived Class - `Circle`:

- Inherits from `Shape`.
- Attributes: `radius`.
- Overrides the `area()` method to calculate the circle’s area using the formula: *π × radius²*.

### class_static_methods_demo.py 

- *a script with a class `Calculator` that includes both a class method and a static method to perform calculations.*

##### `Calculator` Class:

- Static Method - `add(a, b)`: Returns the sum of two numbers. Use the `@staticmethod` decorator.
- Class Method - `multiply(cls, a, b)`: Returns the product of two numbers. Use the `@classmethod` decorator and ensure it prints a class attribute named `calculation_type` before performing the multiplication.
- Class Attribute:
- Define a class attribute `calculation_type` with a value of `"Arithmetic Operations"` that the multiply class method will reference.
