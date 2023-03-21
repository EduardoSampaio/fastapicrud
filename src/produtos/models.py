# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double
# from sqlalchemy.orm import relationship
# from src.database import Base
#
# # ManyToOne
#
#
# class Produto(Base):
#     __tablename__ = "produtos"
#
#     id = Column(Integer, index=True, primary_key=True)
#     nome = Column(String(30), nullable=False)
#     preco = Column(Double, nullable=False)
#     categoria_id = Column(ForeignKey("categorias.id"), index=True)
#     categoria = relationship("Categoria", back_populates="produtos", lazy="joined")
#
#     def __init__(self, nome, preco, categoria_id):
#         self.nome = nome
#         self.preco = preco
#         self.categoria_id = categoria_id
#
#
# class Categoria(Base):
#     __tablename__ = "categorias"
#
#     id = Column(Integer, index=True, primary_key=True)
#     nome = Column(String(30), nullable=False)
#     produtos = relationship("Produto", back_populates="categorias", lazy="select")
#
#
# # ManyTo Many
#
# class Student(Base):
#     __tablename__ = 'student'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     courses = relationship("Course", secondary="student_course", back_populates="students")
#
#
# class Course(Base):
#     __tablename__ = 'course'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     students = relationship("Student", secondary="student_course", back_populates="courses")
#
#
# class StudentCourse(Base):
#     __tablename__ = 'student_course'
#     student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
#     course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)