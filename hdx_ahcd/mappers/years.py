# -*- coding: utf-8 -*-
"""
Year specific NAMCSMetaMappings for all the namcs year, all years are defined
by `YEAR_AVAILABLE` config parameter.
"""
# Python modules
import inspect

# Other modules
from hdx_ahcd.namcs.enums import NAMCSFieldEnum
from hdx_ahcd.helpers.functions import (
    get_slice_object
)
from hdx_ahcd.utils.utils import NAMCSMetaMappings

# 3rd party modules
# -N/A

# Global vars
# -N/A


class Year(object):
    """
    Base class for all classes of NAMCSMetaMappings per year.

    Child class will have field mappings for respective year in the form of
    attributes. Field mappings are nothing but objects of
    class `NAMCSMetaMappings` holding values for field name, location, length.

    This class implements methods to get attributes for specific class. In
    this case class of NAMCS mappings and to get slice object based on
    field location and field length for same Mappings.

    Child class will directly inherit this class, then classmethods of this
    class can be used to fetch attributes.
    """
    @classmethod
    def get_attributes(cls):
        """
        Method to get all attributes defined in class, excluding inbuilt
        arguments.

        Returns:
            :class:`list`: All explicitly defined attributes of class
        """
        # Inspect for class methods and attributes.
        attributes = dict(inspect.getmembers(cls,
                                             lambda attribute: not (
                                                 inspect.isroutine(attribute))))
        return [
            attributes.get(attr) for attr in attributes if not (
                    attr.endswith('_') or attr.startswith('_')
            )
        ]

    @classmethod
    def get_field_slice_mapping(cls):
        """
        Method to get mappings for field of year and corresponding
        slice operator

        Returns:
            :class:`dict`: Key value pair of field name and corresponding
                slice operator indicating location of field in raw record.
        """
        mappings_dict = {}
        for mapping in cls.get_attributes():
            if type(mapping) in (list, tuple):
                """
                Unpacking the tuple to create individual key in `mappings_dict`
                Example:
                    physician_diagnoses = (
                      __physician_diagnoses_1,
                      __physician_diagnoses_2,
                      __physician_diagnoses_3,
                    )
                """

                # Removing fields those already present in `mappings_dict`
                for clubbed_mapping in mapping:
                    if clubbed_mapping.field_name in mappings_dict:
                        del mappings_dict[clubbed_mapping.field_name]

                mappings_dict[mapping[0].field_name] = [
                    get_slice_object(
                        clubbed_mapping.field_location,
                        clubbed_mapping.field_length
                    )
                    for clubbed_mapping in mapping
                ]
            else:
                # Avoiding over writing the value of existing key
                if mapping.field_name not in mappings_dict:
                    mappings_dict[mapping.field_name] = \
                        get_slice_object(
                            mapping.field_location,
                            mapping.field_length
                        )
        return mappings_dict


class Year1973(Year):
    """
    Year 1973 data with specified fields.
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    month_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 5,
        field_name = NAMCSFieldEnum.MONTH_OF_BIRTH.value
    )
    year_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 7,
        field_name = NAMCSFieldEnum.YEAR_OF_BIRTH.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 9,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 4,
        field_location = 39,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 4,
        field_location = 43,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 4,
        field_location = 47,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 10,
        field_location = 71,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1975(Year1973):
    """
    Year 1975 data with specified fields...

    Note:
        Year 1975 and 1973 have same `NAMCSMetaMappings`.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 10,
        field_location = 78,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1976(Year1975):
    """
    Year 1976 data with specified fields...

    Note:
        Year 1976 and 1975 have same `NAMCSMetaMappings`.
    """
    pass


class Year1977(Year):
    """
    Year 1977 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    month_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 5,
        field_name = NAMCSFieldEnum.MONTH_OF_BIRTH.value
    )
    year_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 7,
        field_name = NAMCSFieldEnum.YEAR_OF_BIRTH.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 9,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 4,
        field_location = 28,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 4,
        field_location = 32,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 4,
        field_location = 36,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 10,
        field_location = 75,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1978(Year1977):
    """
    Year 1978 data with specified fields..

    Note:
        Year 1978 and Year 1977 have same `NAMCSMetaMappings`.
    """
    pass


class Year1979(Year):
    """
    Year 1979 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    month_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 5,
        field_name = NAMCSFieldEnum.MONTH_OF_BIRTH.value
    )
    year_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 7,
        field_name = NAMCSFieldEnum.YEAR_OF_BIRTH.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 9,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 29,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )

    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 35,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 41,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )

    visit_weight = NAMCSMetaMappings(
        field_length = 10,
        field_location = 84,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1980(Year):
    """
    Year 1980 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    month_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 5,
        field_name = NAMCSFieldEnum.MONTH_OF_BIRTH.value
    )
    year_of_birth = NAMCSMetaMappings(
        field_length = 2,
        field_location = 7,
        field_name = NAMCSFieldEnum.YEAR_OF_BIRTH.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 9,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 40,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 46,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 52,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 10,
        field_location = 122,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1981(Year1980):
    """
    Year 1981 data with specified fields..

    Note:
        Year 1981 and Year 1980 have same `NAMCSMetaMappings`.
    """
    pass


class Year1985(Year):
    """
    Year 1985 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 5,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 2,
        field_location = 7,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 9,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 57,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 63,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 69,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 5,
        field_location = 135,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1989(Year):
    """
    Year 1989 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 5,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 2,
        field_location = 7,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 9,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 37,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 43,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 49,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 135,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1990(Year1989):
    """
    Year 1990 data with specified fields..

    Note:
        Year 1990 and Year 1989 have same `NAMCSMetaMappings`.
    """
    pass


class Year1991(Year):
    """
    Year 1991 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 5,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 2,
        field_location = 7,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 9,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 153,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 39,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 45,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 51,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year1992(Year1991):
    """
    Year 1992 data with specified fields..

    Note:
        Year 1992 and Year 1991 have same `NAMCSMetaMappings`.
    """
    pass


class Year1993(Year1991):
    """
    Year 1993 data with specified fields..

    Note:
        Year 1993 and Year 1991 have same `NAMCSMetaMappings`.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 160,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )


class Year1994(Year1993):
    """
    Year 1994 data with specified fields..

    Note:
        Year 1994 and Year 1994 have same `NAMCSMetaMappings`.
    """
    pass


class Year1995(Year1991):
    """
    Year 1995 data with specified fields..
    """
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 7,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 10,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 196,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 5,
        field_location = 52,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 5,
        field_location = 57,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 5,
        field_location = 62,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year1996(Year1995):
    """
    Year 1996 data with specified fields..

    Note:
        Year 1996 and Year 1995 have same `NAMCSMetaMappings`.
    """
    pass


class Year1997(Year):
    """
    Year 1997 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 4,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 8,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 297,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 567,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 573,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 579,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year1998(Year1997):
    """
    Year 1998 data with specified fields..

    Note:
        Year 1998 and Year 1997 have same `NAMCSMetaMappings`.
    """
    pass


class Year1999(Year):
    """
    Year 1999 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 4,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 8,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 307,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 577,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 583,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 589,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2000(Year1999):
    """
    Year 2000 data with specified fields..

    Note:
        Year 2000 and Year 1999 have same `NAMCSMetaMappings`.
    """
    pass


class Year2001(Year):
    """
    Year 2001 data with specified fields..
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 4,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 8,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 273,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 547,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 553,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 559,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2002(Year2001):
    """
    Year 2002 data with specified fields..

    Note:
        Year 2002 and Year 2001 have same `NAMCSMetaMappings`.
    """
    pass


class Year2003(Year2001):
    """
    Year 2003 data with specified fields..
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 288,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 723,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value

    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 729,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 735,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2004(Year2003):
    """
    Year 2004 data with specified fields.
    """
    pass


class Year2005(Year):
    """
    Year 2005 data with specified fields.
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 4,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 8,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 271,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 703,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 709,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 715,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2006(Year2005):
    """
    Year 2006 data with specified fields.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 276,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 826,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 832,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 838,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2007(Year):
    """
    Year 2007 data with specified fields.
    """
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    year_of_visit = NAMCSMetaMappings(
        field_length = 4,
        field_location = 3,
        field_name = NAMCSFieldEnum.YEAR_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 8,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 303,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 909,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 915,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 921,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2008(Year2007):
    """
    Year 2008 data with specified fields.
    """
    pass


class Year2009(Year2007):
    """
    Year 2009 data with specified fields.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 294,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 892,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 898,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 904,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2010(Year2007):
    """
    Year 2010 data with specified fields.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 294,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 919,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 925,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 931,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2011(Year):
    """
    Year 2011 data with specified fields.

    Note:
        Field `Year_of_visit` has been removed from records.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 6,
        field_location = 286,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 4,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 7,
        field_name = NAMCSFieldEnum.GENDER.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 919,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 925,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 931,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2012(Year):
    """
    Year 2012 data with specified fields.

    Note:
        Extra field  in record `AGE RECODE`,
        `AGE IN DAYS FOR PATIENTS LESS THAN ONE YEAR OF AGE`, for year 2012
        and onwards
        [PATWT] PATIENT VISIT WEIGHT (NOT FOR STATE ESTIMATES)
        This variable has been produced as an un rounded integer in 2012,
        which will make estimates slightly more precise. It is ONLY for use in
        producing national, regional, division, and MSA-level estimates, NOT
        state estimates.
        168.792 – 82313.10758
        [PATWTST] PATIENT VISIT WEIGHT FOR STATE ESTIMATES
        This variable has been produced as an un rounded integer in 2012,
        which will make estimates slightly more precise. It is ONLY for use in
        producing state estimates, NOT national, regional, division, or MSA-
        level estimates.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 11,
        field_location = 1383,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 4,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 96,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 102,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 108,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2013(Year):
    """
    Year 2013 data with specified fields.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 11,
        field_location = 1363,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 4,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 96,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 102,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 108,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3
    )


class Year2014(Year):
    """
    Year 2014 data with specified fields.

    Note:
        New diagnosis fields `DIAGNOSIS 4 ` and `DIAGNOSIS  5` in record
        for year 2014 and onwards
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 11,
        field_location = 2722,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 4,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 146,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 152,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 158,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    __physician_diagnoses_4 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 164,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_4.value
    )
    __physician_diagnoses_5 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 170,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_5.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3,
        __physician_diagnoses_4,
        __physician_diagnoses_5
    )


class Year2015(Year):
    """
    Year 2015 data with specified fields.
    """
    visit_weight = NAMCSMetaMappings(
        field_length = 11,
        field_location = 2682,
        field_name = NAMCSFieldEnum.VISIT_WEIGHT.value
    )
    month_of_visit = NAMCSMetaMappings(
        field_length = 2,
        field_location = 1,
        field_name = NAMCSFieldEnum.MONTH_OF_VISIT.value
    )
    age = NAMCSMetaMappings(
        field_length = 3,
        field_location = 4,
        field_name = NAMCSFieldEnum.PATIENT_AGE.value
    )
    sex = NAMCSMetaMappings(
        field_length = 1,
        field_location = 11,
        field_name = NAMCSFieldEnum.GENDER.value
    )

    # Numeric format
    __physician_diagnoses_1 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 148,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_1.value
    )
    __physician_diagnoses_2 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 154,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_2.value
    )
    __physician_diagnoses_3 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 160,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_3.value
    )
    __physician_diagnoses_4 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 166,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_4.value
    )
    __physician_diagnoses_5 = NAMCSMetaMappings(
        field_length = 6,
        field_location = 172,
        field_name = NAMCSFieldEnum.PHYSICIANS_DIAGNOSES_5.value
    )
    physician_diagnoses = (
        __physician_diagnoses_1,
        __physician_diagnoses_2,
        __physician_diagnoses_3,
        __physician_diagnoses_4,
        __physician_diagnoses_5
    )
