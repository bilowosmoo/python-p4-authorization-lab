from app import app
from models import db, User, Article

with app.app_context():
    # Clear existing data
    User.query.delete()
    Article.query.delete()

    # Create user
    user = User(username="testuser")
    db.session.add(user)

    # Create member-only article
    member_article = Article(
        title="Exclusive Post",
        content="Only for members",
        is_member_only=True
    )
    db.session.add(member_article)

    # Commit changes
    db.session.commit()
