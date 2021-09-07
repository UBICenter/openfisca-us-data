from openfisca_us_data.datasets.cps.base_cps.survey_input_variables import (
    get_CPS_variables,
)
from openfisca_core.model_api import Variable, YEAR, Reform


def get_input_variables():
    from openfisca_us.entities import (
        Person,
        TaxUnit,
        Household,
        Family,
        SPMUnit,
    )

    class e00200(Variable):
        value_type = float
        entity = Person
        label = u"Wage and salary"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_WSAL_VAL", period)

    class interest(Variable):
        value_type = float
        entity = Person
        label = u"Interest income"
        definition_period = YEAR

        def formula(person, period):
            return person("P_INT_VAL", period)

    class e00900(Variable):
        value_type = float
        entity = Person
        label = u"Self-employment income"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_SEMP_VAL", period)

    class e02100(Variable):
        value_type = float
        entity = Person
        label = u"label"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_FRSE_VAL", period)

    class divs(Variable):
        value_type = float
        entity = Person
        label = u"label"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_DIV_VAL", period)

    class rents(Variable):
        value_type = float
        entity = Person
        label = u"label"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_RNT_VAL", period)

    class e01500(Variable):
        value_type = float
        entity = Person
        label = u"label"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_RTM_VAL", period)

    class e00800(Variable):
        value_type = float
        entity = Person
        label = u"label"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_ALIMONY", period)

    class e02400(Variable):
        value_type = float
        entity = Person
        label = u"label"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_SS_IMPUTE", period)

    class e02300(Variable):
        value_type = float
        entity = Person
        label = u"label"
        definition_period = YEAR

        def formula(person, period, parameters):
            return person("P_UI_IMPUTE", period)

    input_variables = [
        e00200,
        interest,
        e00900,
        e02100,
        divs,
        rents,
        # e01500,
        # e00800,
        # e02400,
        # e02300,
    ]

    return input_variables


def from_BaseCPS(year: int = 2020):
    class reform(Reform):
        def apply(self):
            for var in get_CPS_variables():
                self.add_variable(var)
            for var in get_input_variables():
                self.update_variable(var)

    return reform
