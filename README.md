# AutoMart

## API Backend for Automart 
    - API is only readable

---

## End points

---

- `/glass/company/` - give all companys
- `/glass/cars/` - give all cars
- `/glass/models/` - give all models
- `/glass/glass-list/` - give all glass

- `/glass/cars/?company="id"` - filter cars by company id
- `/glass/models/?car="id"` - filter models by car id
- `/glass/glass-list/?car="id"&model="id"` - filter glass by car id and model id
- `/glass/glass-list/?search="car-name"` - filter glass by car name
