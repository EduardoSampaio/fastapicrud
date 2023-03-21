from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from src.database import Base


class FundosImobiliarios(Base):
    __tablename__ = "fundos_imobiliarios"

    id = Column("fundo_id", Integer, index=True, primary_key=True)
    codigo_do_fundo = Column("CODIGO_DO_FUNDO", String(30), index=True, unique=True, nullable=False)
    setor = Column("SETOR", String(30))
    liquidez_diaria = Column("LIQUIDEZ_DIARIA", Numeric, nullable=True)
    dividendo = Column("DIVIDENDO", Numeric, nullable=True)
    dividend_yield = Column("DIVIDEND_YIELD", Numeric, nullable=True)
    dy_ano = Column("DY_ANO", Numeric, nullable=True)
    variacao_preco = Column("VARIAÇÃO_PREÇO", Numeric, nullable=True)
    rentab_periodo = Column("RENTAB_PERIODO", Numeric, nullable=True)
    rentab_acumulada = Column("RENTAB_ACUMULADA", Numeric, nullable=True)
    patrimonio_liq = Column("PATRIMÔNIO_LIQ", Numeric, nullable=True)
    vpa = Column("VPA", Numeric, nullable=True)
    p_vpa = Column("P_VPA", Numeric, nullable=True)
    dy_patrimonial = Column("DY_PATRIMONIAL", Numeric, nullable=True)
    variacao_patrimonial = Column("VARIAÇÃO_PATRIMONIAL", Numeric, nullable=True)
    rentab_patr_no_período = Column("RENTAB_PATR_NO_PERÍODO", Numeric, nullable=True)
    rentab_patr_acumulada = Column("RENTAB_PATR_ACUMULADA", Numeric, nullable=True)
    vacancia_fisica = Column("VACANCIA_FISICA", Numeric, nullable=True)
    vacancia_financeira = Column("VACÂNCIA_FINANCEIRA", Numeric, nullable=True)
    quantidade_ativos = Column("QUANTIDADE_ATIVOS", Integer, nullable=True)

    def __init__(self, codigo_do_fundo,
                 setor,
                 liquidez_diaria,
                 dividendo,
                 dividend_yield,
                 dy_ano,
                 variacao_preco,
                 rentab_periodo,
                 rentab_acumulada,
                 patrimonio_liq,
                 vpa,
                 p_vpa,
                 dy_patrimonial,
                 variacao_patrimonial,
                 rentab_patr_no_período,
                 rentab_patr_acumulada,
                 vacancia_financeira,
                 quantidade_ativos):
        self.codigo_do_fundo = codigo_do_fundo
        self.setor = setor
        self.liquidez_diaria = liquidez_diaria
        self.dividendo = dividendo
        self.dividend_yield = dividend_yield
        self.dy_ano = dy_ano
        self.variacao_preco = variacao_preco
        self.rentab_periodo = rentab_periodo
        self.rentab_acumulada = rentab_acumulada
        self.patrimonio_liq = patrimonio_liq
        self.vpa = vpa
        self.p_vpa = p_vpa
        self.dy_patrimonial = dy_patrimonial
        self.variacao_patrimonial = variacao_patrimonial
        self.rentab_patr_no_período = rentab_patr_no_período
        self.rentab_patr_acumulada = rentab_patr_acumulada
        self.vacancia_financeira = vacancia_financeira
        self.quantidade_ativos = quantidade_ativos
