from models.user.schemas import ArticleBase
from db.models import DBArticle
from sqlalchemy.orm.session import Session


def create_article(db: Session, request: ArticleBase):
    new_article = DBArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, id: int):
    articles = db.query(DBArticle).filter(DBArticle.id == id).first()
    return articles
