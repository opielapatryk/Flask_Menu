# Flask_Menu
## Project is created based on Clean Architecture <br>
### Inward -> Simple data x Outward -> Interfaces

## External systems
Web Framework: Flask <br>
Repository: Memory <br>

## Gateways
Dictionary + DB Interface <br>
i.e. class MemRepo <br>

## Use Cases: "business logic"
### Receive repo + parameters, returns results
GET: List all dishes <br>
GET{id}: List dish <br>
POST: Add dish <br>
PUT: Edit dish <br>
DELETE: Remove dish <br>

## Entities
Module: Dish <br>

# TODO
-[x] Apply Clean Architecture
-[x] Layer Abstraction
 Dependency Injection
 UseCase Implementation
 Serialization / Deserialization
 Mock Repo Implementation
 Handle Exceptions
 Response Marshalling
 Review usecase.execute() with Req/Resp
 Review API Documentation
 Implement Full Story with Entity, ValueObject
 Request Validation with Marshmallow
 Deal with Date/DateTime
 Database with SQLAlchemy
 Logging
 OAuth2 with Authlib Implementation
 Authentication to Resource API
 Dev/Prod Configuration
 Apply Tests
 WSGI Settings