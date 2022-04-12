from minimalcd import application as app
from minimalcd import Principle
from minimalcd import db


@app.route("/")
def index():
    # Verify writes to database are working
    principle = Principle()
    principle.principle = "All good demos include state."
    db.session.add(principle)
    db.session.commit()

    # Verify database access, by displaying first principle from principle table
    firstPrinciple = Principle.query.first().principle
    return firstPrinciple
