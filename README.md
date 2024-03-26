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
- [x] Apply Clean Architecture <br> 
- [x] Layer Abstraction<br> 
- [x] Dependency Injection<br> 
- [x] UseCase Implementation<br> 
- [x] Serialization / Deserialization<br> 
- [x] Mock Repo Implementation<br> 
 Handle Exceptions<br> 
 Response Marshalling<br> 
 Review usecase.execute() with Req/Resp<br> 
 Review API Documentation<br> 
 Implement Full Story with Entity, ValueObject<br> 
 Request Validation with Marshmallow<br> 
 Deal with Date/DateTime<br> 
 Database with SQLAlchemy<br> 
 Logging<br> 
 OAuth2 with Authlib Implementation<br> 
 Authentication to Resource API<br> 
 Dev/Prod Configuration<br> 
- [x] Apply Tests<br> 
 WSGI Settings<br> 