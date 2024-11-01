---
title: Fundamentals of OOP in PHP
publishDate: 2023-19-04 00:00:00
description:  This article provides an introduction to Object-Oriented Programming (OOP) in PHP, covering the basics of classes, objects, properties, and methods. It also discusses inheritance, encapsulation, and polymorphism, and provides examples of how to use these concepts in PHP code.
image: https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Drupal_logo_-_gray.png/640px-Drupal_logo_-_gray.png
tags:
  - Books
  - Article
  - Development
  - Learn
---




-----

# PREFACE

## The world of programming is constantly evolving, and with each new version, programming languages strive to offer more tools and resources to facilitate software development. PHP 8 is no exception. This version brings a series of improvements that promise to transform the way we write and maintain our PHP projects.

Object-oriented programming (OOP) has established itself as one of the most effective approaches to software development, allowing developers to create more organized, reusable, and maintainable systems. In this book, we delve deep into the OOP concepts applied to PHP 8, exploring everything from the fundamentals to advanced practices that will help you build robust and scalable applications.

Throughout the chapters, we will cover essential topics such as classes, objects, inheritance, polymorphism, encapsulation,
interfaces, abstract classes, namespaces, autoloading, exception handling, object composition, and, of course, the S.O.L.I.D. principles. Each chapter has been carefully crafted to provide a clear and practical understanding of the concepts, with code examples that illustrate how to apply these concepts in real situations.

This book is intended for developers of all levels, from beginners taking their first steps in PHP to experienced professionals looking to update their knowledge with the new features of PHP 8. Our goal is to provide a comprehensive and accessible resource that can be used as a reference in your daily programming work.

We hope that this book not only enhances your understanding of object-oriented programming with PHP 8 but also inspires you to explore new possibilities and create ever better software solutions.


-----

## Thank you for choosing this book as your learning source, and we wish you a productive and inspiring reading experience.

Happy reading!


-----

# TABLE OF CONTENTS

## 1. Introduction to PHP 8 2. Fundamentals of Object-Oriented Programming (OOP) 3. Inheritance and Polymorphism 4. Encapsulation 5. Interfaces and Abstract Classes 6. Namespace and Autoloading
7. Exception Handling
8. Object Composition 9. Traits
10. Dependency Management with Composer 11. Coding Best Practices 12. Unit Testing and TDD 13. Design Patterns in PHP 14. S.O.L.I.D. Principles 15. Conclusion


-----

# CHAPTER 1:
INTRODUCTION TO PHP 8

## PHP 8 brings a host of new features, improvements, and performance enhancements that make it a significant upgrade over its predecessors. In this chapter, we will explore these new features and understand how they can be leveraged to write better, more efficient code.

# Key Features of PHP 8

## ● JIT Compiler: The Just-In-Time compiler improves
performance by compiling code at runtime.

● Union Types: Allow a variable to hold multiple types,
enhancing type safety.

● Attributes: Provide a native way to add metadata to classes
and functions.

● Named Arguments: Enable passing arguments to a function
based on the parameter name.

● Match Expression: A more powerful and flexible alternative
to the switch statement.

Let's dive into each of these features with examples.

 <?php // JIT Compiler example function sum($a, $b) {
 return $a + $b;
 }


-----

## echo sum(2, 3); // Output: 5 ?>

php Copiar código <?php // Union Types example function foo(int|float $value): int|float {
return $value;
}

echo foo(2); // Output: 2 echo foo(3.5); // Output: 3.5 ?>


-----

# CHAPTER 2:
FUNDAMENTALS OF
OBJECT-ORIENTED
PROGRAMMING (OOP)

## Object-oriented programming is a paradigm that uses objects and classes to organize code into reusable and scalable components. In this chapter, we will cover the basics of OOP, including classes, objects, properties, and methods.

# Classes and Objects

## A class is a blueprint for creating objects. An object is an instance of a class. Classes can contain properties (variables) and methods (functions).

 <?php class Car {
 public string $color; public string $model;

 public function __construct(string $color, string $model) {
 $this->color = $color; $this->model = $model;
 }

 public function getDescription(): string {
 return "This car is a $this->color $this->model.";


-----

## }
 }

 $car = new Car("red", "Toyota"); echo $car->getDescription(); // Output: This car is a red Toyota. ?>


-----

# CHAPTER 3: INHERITANCE
AND POLYMORPHISM

## Inheritance allows a class to inherit properties and methods from another class. Polymorphism enables objects to be treated as instances of their parent class.

# Inheritance

## <?php class Vehicle {
public string $make; public string $model;

public function __construct(string $make, string $model) {
$this->make = $make; $this->model = $model;
}

public function getDetails(): string {
return "$this->make $this->model";
}
}

class Car extends Vehicle {
public int $doors;

public function __construct(string $make, string $model, int
$doors) {
parent::__construct($make, $model); $this->doors = $doors;


-----

## }

public function getDetails(): string {
return parent::getDetails() . " with $this->doors doors";
}
}

$car = new Car("Toyota", "Corolla", 4); echo $car->getDetails(); // Output: Toyota Corolla with 4 doors ?>

# Polymorphism

## <?php interface Shape {
public function area(): float;
}

class Circle implements Shape {
private float $radius;

public function __construct(float $radius) {
$this->radius = $radius;
}

public function area(): float {
return pi() * $this->radius * $this->radius;
}
}

class Rectangle implements Shape {
private float $width; private float $height;

public function __construct(float $width, float $height) {
$this->width = $width; $this->height = $height;


-----

## }

public function area(): float {
return $this->width * $this->height;
}
}

function printArea(Shape $shape) {
echo "Area: " . $shape->area() . "\n";
}

$circle = new Circle(3); $rectangle = new Rectangle(4, 5);

printArea($circle); // Output: Area: 28.27 printArea($rectangle); // Output: Area: 20 ?>


-----

# CHAPTER 4:
ENCAPSULATION

## Encapsulation is the concept of restricting access to the internal state of an object and only allowing modification through public methods.

 <?php class Person {
 private string $name; private int $age;

 public function __construct(string $name, int $age) {
 $this->name = $name; $this->age = $age;
 }

 public function getName(): string {
 return $this->name;
 }

 public function setName(string $name): void {
 if (!empty($name)) {
 $this->name = $name;
 }
 }

 public function getAge(): int {
 return $this->age;
 }

 public function setAge(int $age): void {


-----

## if ($age > 0) {
 $this->age = $age;
 }


## }
 }

 $person = new Person("John", 30); echo $person->getName(); // Output: John $person->setAge(35); echo $person->getAge(); // Output: 35 ?>


-----

# CHAPTER 5: INTERFACES
AND ABSTRACT CLASSES

## Interfaces define a contract that classes must adhere to. Abstract classes provide a base for other classes to extend from, but cannot be instantiated themselves.

# Interfaces

## <?php interface Logger {
public function log(string $message): void;
}

class FileLogger implements Logger {
public function log(string $message): void {
file_put_contents("log.txt", $message . PHP_EOL,
FILE_APPEND);
}
}

class DatabaseLogger implements Logger {
public function log(string $message): void {
// Code to log message in a database
}
}

function logMessage(Logger $logger, string $message) {
$logger->log($message);
}


-----

## $logger = new FileLogger(); logMessage($logger, "This is a log message."); // Logs message to file ?>

# Abstract Classes

## <?php abstract class Animal {
protected string $name;

public function __construct(string $name) {
$this->name = $name;
}

abstract public function makeSound(): string;

public function getName(): string {
return $this->name;
}
}

class Dog extends Animal {
public function makeSound(): string {
return "Bark";
}
}

class Cat extends Animal {
public function makeSound(): string {
return "Meow";
}
}

$dog = new Dog("Rex"); $cat = new Cat("Whiskers");


-----

## echo $dog->getName() . " says " . $dog->makeSound(); // Output: Rex says Bark echo $cat->getName() . " says " . $cat->makeSound(); // Output: Whiskers says Meow ?>


-----

# CHAPTER 6: NAMESPACE
AND AUTOLOADING

## Namespaces help organize code by grouping related classes together, preventing name collisions. Autoloading simplifies the inclusion of class files.

# Namespaces

## <?php namespace App\Models;

class User {
public string $name;

public function __construct(string $name) {
$this->name = $name;
}

public function getName(): string {
return $this->name;
}
} ?>

 <?php require 'User.php';

 use App\Models\User;

 $user = new User("Alice");


-----

## echo $user->getName(); // Output: Alice ?>

# Autoloading

## <?php spl_autoload_register(function ($class) {
include $class . '.php';
});

use App\Models\User;

$user = new User("Alice"); echo $user->getName(); // Output: Alice ?>


-----

# CHAPTER 7: EXCEPTION
HANDLING

## Exceptions are used to handle errors and exceptional conditions in a program's flow. They allow for more controlled and readable error handling.

 <?php class CustomException extends Exception {}

 function divide($a, $b) {
 if ($b === 0) {
 throw new CustomException("Division by zero.");
 } return $a / $b;
 }

 try {
 echo divide(10, 0);
 } catch (CustomException $e) {
 echo "Error: " . $e->getMessage(); // Output: Error: Division by
 zero. } finally {
 echo "Execution complete.";
 } ?>


-----

# CHAPTER 8: OBJECT
COMPOSITION

## Object composition involves using objects within other objects to build complex functionalities.

 <?php class Engine {
 public function start() {
 return "Engine started";
 }
 }

 class Car {
 private Engine $engine;

 public function __construct() {
 $this->engine = new Engine();
 }

 public function startCar() {
 return $this->engine->start();
 }
 }

 $car = new Car(); echo $car->startCar(); // Output: Engine started ?>


-----

# CHAPTER 9: TRAITS

## Traits are a mechanism for code reuse in single inheritance languages like PHP. They allow you to include methods in multiple classes.

 <?php trait Logger {
 public function log(string $message) {
 echo "Log: " . $message;
 }
 }

 class User {
 use Logger;

 public function createUser(string $name) {
 // Code to create user $this->log("User $name created.");
 }
 }

 class Order {
 use Logger;

 public function createOrder(string $product) {
 // Code to create order $this->log("Order for $product created.");
 }
 }

 $user = new User(); $user->createUser("Alice"); // Output: Log: User Alice created.


-----

## $order = new Order(); $order->createOrder("Book"); // Output: Log: Order for Book created. ?>


-----

# CHAPTER 10:
DEPENDENCY
MANAGEMENT WITH
COMPOSER

## Composer is a dependency manager for PHP, allowing you to manage libraries and packages your project depends on.

# Install Composer globally php -r "copy('https://getcomposer.org/installer', 'composer setup.php');" php composer-setup.php php -r "unlink('composer-setup.php');" mv composer.phar /usr/local/bin/composer

# Using Composer

## # Initialize a new project composer init

# Require a package composer require monolog/monolog

# Autoloading with Composer

## php


-----

## Copiar código <?php require 'vendor/autoload.php';

use Monolog\Logger; use Monolog\Handler\StreamHandler;

$log = new Logger('name'); $log->pushHandler(new StreamHandler('path/to/your.log',
Logger::WARNING));

$log->warning('Foo'); $log->error('Bar'); ?>


-----

# CHAPTER 11: CODING
BEST PRACTICES

## Adhering to coding best practices ensures your code is readable, maintainable, and efficient.

# Coding Standards

## ● Follow PSR (PHP Standard Recommendations) guidelines.
● Use meaningful variable and function names.
● Write comments and documentation.

# Example

## <?php class User {
private string $name; private string $email;

public function __construct(string $name, string $email) {
$this->name = $name; $this->email = $email;
}

public function getName(): string {
return $this->name;
}

public function getEmail(): string {
return $this->email;


-----

## }


## } ?>


-----

# CHAPTER 12: UNIT
TESTING AND TDD

## Unit testing involves testing individual components of your application to ensure they work as expected. Test-driven
development (TDD) is a development approach where tests are written before the code.

# PHPUnit

## # Install PHPUnit composer require --dev phpunit/phpunit

# Example Test

## <?php use PHPUnit\Framework\TestCase;

class UserTest extends TestCase {
public function testUserCreation() {
$user = new User("Alice", "alice@example.com"); $this->assertEquals("Alice", $user->getName()); $this->assertEquals("alice@example.com", $user >getEmail());
}
} ?>


-----

# CHAPTER 13: DESIGN
PATTERNS IN PHP

## Design patterns are reusable solutions to common problems in software design.

# Singleton Pattern

## php Copiar código <?php class Singleton {
private static ?Singleton $instance = null;

private function __construct() {}

public static function getInstance(): Singleton {
if (self::$instance === null) {
self::$instance = new Singleton();
} return self::$instance;
}
}

$instance = Singleton::getInstance(); ?>

# Factory Pattern

## <?php


-----

## interface Shape {
public function draw();
}

class Circle implements Shape {
public function draw() {
echo "Drawing Circle";
}
}

class Square implements Shape {
public function draw() {
echo "Drawing Square";
}
}

class ShapeFactory {
public static function createShape(string $type): Shape {
return match ($type) {
'circle' => new Circle(), 'square' => new Square(), default => throw new InvalidArgumentException("Unknown
shape type"),
};
}
}

$circle = ShapeFactory::createShape('circle'); $circle->draw(); // Output: Drawing Circle

$square = ShapeFactory::createShape('square'); $square->draw(); // Output: Drawing Square ?>


-----

# CHAPTER 14: S.O.L.I.D.
PRINCIPLES

## The S.O.L.I.D. principles are five design principles intended to make software designs more understandable, flexible, and maintainable.

# Single Responsibility Principle (SRP)

## <?php class Order {
public function addItem(string $item) {
// Add item to order
}
}

class OrderRepository {
public function save(Order $order) {
// Save order to database
}
} ?>

# Open/Closed Principle (OCP)

## <?php interface Shape {


-----

## public function area(): float;
}

class Circle implements Shape {
private float $radius;

public function __construct(float $radius) {
$this->radius = $radius;
}

public function area(): float {
return pi() * $this->radius * $this->radius;
}
}

class Rectangle implements Shape {
private float $width; private float $height;

public function __construct(float $width, float $height) {
$this->width = $width; $this->height = $height;
}

public function area(): float {
return $this->width * $this->height;
}
}

function printArea(Shape $shape) {
echo "Area: " . $shape->area() . "\n";
} ?>


-----

# Liskov Substitution Principle (LSP)

## <?php class Bird {
public function fly() {
// Flying logic
}
}

class Duck extends Bird {
// Duck specific logic
}

class Ostrich extends Bird {
public function fly() {
throw new Exception("Ostrich can't fly");
}
} ?>

# Interface Segregation
Principle (ISP)

## <?php interface Printer {
public function printDocument(string $document);
}

interface Scanner {
public function scanDocument(string $document);
}


-----

## class MultiFunctionPrinter implements Printer, Scanner {
public function printDocument(string $document) {
// Print logic
}

public function scanDocument(string $document) {
// Scan logic
}
} ?>

# Dependency Inversion
Principle (DIP)

## <?php interface DatabaseConnection {
public function connect();
}

class MySQLConnection implements DatabaseConnection {
public function connect() {
// MySQL connection logic
}
}

class PasswordReminder {
private DatabaseConnection $dbConnection;

public function __construct(DatabaseConnection $dbConnection)
{
$this->dbConnection = $dbConnection;
}
} ?>


-----

-----

# CHAPTER 15:
CONCLUSION

## As we conclude this journey through PHP 8 and object-oriented programming, we hope you now have a deeper understanding of the principles and practices that will help you build better, more maintainable software. PHP 8 offers a powerful set of tools and features that, when combined with solid OOP practices, can significantly enhance your development process.

Remember to keep experimenting, learning, and applying these concepts to real-world projects. The field of software development is ever-changing, and staying updated with the latest advancements is crucial for success.

Thank you for reading, and we wish you all the best in your programming endeavors.


-----


