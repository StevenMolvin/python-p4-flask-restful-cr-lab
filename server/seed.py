from faker import Faker
from app import app
from models import db, Plant

with app.app_context():
    fake = Faker()

    db.create_all()  # Create all tables, including 'plants' if not already created

    Plant.query.delete()

    plants = []

    aloe = Plant(
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
    )
    plants.append(aloe)

    zz_plant = Plant(
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=25.98,
    )
    plants.append(zz_plant)

    for _ in range(48):  # Create 48 additional fake plants
        fake_plant = Plant(
            name=fake.name(),
            image=fake.image_url(),
            price=fake.random_number(digits=2) + fake.random_number(digits=2) / 100,
        )
        plants.append(fake_plant)

    db.session.add_all(plants)
    db.session.commit()