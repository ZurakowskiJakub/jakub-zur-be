from app_config import db


class Proficiency(db.Model):
    """
    Proficiency object.

    Used to display proficiency in languages and technologies.
    """
    __tablename__ = 'proficiencies'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)  # "Programming",
    icon = db.Column(db.String(255))  # "faReact",
    iconColour = db.Column(db.String(255))  # "#61dbfb",
    label = db.Column(db.String(255), nullable=False)  # "React",
    # "I've worked quite extensivelly with React both in spare time (example, this website) and at work.",
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 4

    def as_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "icon": self.icon,
            "iconColour": self.iconColour,
            "label": self.label,
            "description": self.description,
            "rating": self.rating,
        }

    def __repr__(self):
        return f"id: {id} | cat: {self.category} | label: {self.label} | rating: {'*' * self.rating}"
