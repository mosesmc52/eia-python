from typing import Dict

STORAGE_SERIES_BY_REGION: Dict[str, str] = {
    # examples only — replace with your actual EIA series codes
    "lower48": "NW2_EPG0_SWO_R48_BCF",
    "east": "NW2_EPG0_SWO_R31_BCF",
    "midwest": "NW2_EPG0_SWO_R32_BCF",
    "south_central": "NW2_EPG0_SWO_R33_BCF",
    "mountain": "NW2_EPG0_SWO_R34_BCF",
    "pacific": "NW2_EPG0_SWO_R35_BCF",
}

PRODUCTION_SERIES_BY_STATE = {
    "al": "NA1160_SAL_2",
    "ak": "NA1160_SAK_2",
    "az": "NA1160_SAZ_2",
    "ar": "NA1160_SAR_2",
    "ca": "NA1160_SCA_2",
    "co": "NA1160_SCO_2",
    "fl": "NA1160_SFL_2",
    "il": "NA1160_SIL_2",
    "in": "NA1160_SIN_2",
    "ks": "NA1160_SKS_2",
    "ky": "NA1160_SKY_2",
    "la": "NA1160_SLA_2",
    "md": "NA1160_SMD_2",
    "mi": "NA1160_SMI_2",
    "mo": "NA1160_SMO_2",
    "ms": "NA1160_SMS_2",
    "mt": "NA1160_SMT_2",
    "ne": "NA1160_SNE_2",
    "nv": "NA1160_SNV_2",
    "nm": "NA1160_SNM_2",
    "ny": "NA1160_SNY_2",
    "nd": "NA1160_SND_2",
    "oh": "NA1160_SOH_2",
    "ok": "NA1160_SOK_2",
    "or": "NA1160_SOR_2",
    "pa": "NA1160_SPA_2",
    "sd": "NA1160_SSD_2",
    "tn": "NA1160_STN_2",
    "tx": "NA1160_STX_2",
    "ut": "NA1160_SUT_2",
    "va": "NA1160_SVA_2",
    "wv": "NA1160_SWV_2",
    "united_states_total": "N9070US2",
}

CONSUMPTION_SERIES_BY_STATE = {
    "al": "N9140AL2",
    "ak": "N9140AK2",
    "az": "N9140AZ2",
    "ar": "N9140AR2",
    "ca": "N9140CA2",
    "co": "N9140CO2",
    "ct": "N9140CT2",
    "de": "N9140DE2",
    "fl": "N9140FL2",
    "ga": "N9140GA2",
    "hi": "N9140HI2",
    "id": "N9140ID2",
    "il": "N9140IL2",
    "in": "N9140IN2",
    "ia": "N9140IA2",
    "ks": "N9140KS2",
    "ky": "N9140KY2",
    "la": "N9140LA2",
    "me": "N9140ME2",
    "md": "N9140MD2",
    "ma": "N9140MA2",
    "mi": "N9140MI2",
    "mn": "N9140MN2",
    "ms": "N9140MS2",
    "mo": "N9140MO2",
    "mt": "N9140MT2",
    "ne": "N9140NE2",
    "nv": "N9140NV2",
    "nh": "N9140NH2",
    "nj": "N9140NJ2",
    "nm": "N9140NM2",
    "ny": "N9140NY2",
    "nc": "N9140NC2",
    "nd": "N9140ND2",
    "oh": "N9140OH2",
    "ok": "N9140OK2",
    "or": "N9140OR2",
    "pa": "N9140PA2",
    "ri": "N9140RI2",
    "sc": "N9140SC2",
    "sd": "N9140SD2",
    "tn": "N9140TN2",
    "tx": "N9140TX2",
    "ut": "N9140UT2",
    "vt": "N9140VT2",
    "va": "N9140VA2",
    "wa": "N9140WA2",
    "wv": "N9140WV2",
    "wi": "N9140WI2",
    "wy": "N9140WY2",
    "united_states_total": "N9140US2",
}

IMPORT_SERIES_BY_COUNTRY = {
    # pipeline imports
    "canada_pipeline": "N9102CN2",
    "mexico_pipeline": "N9102MX2",
    "united_states_pipeline_total": "N9102US2",
    # LNG imports by country
    "algeria": "N9103AG2",
    "australia": "N9103AU2",
    "brunei": "N9103BX2",
    "egypt": "N9103EG2",
    "equatorial_guinea": "NGM_EPG0_NUS-NEK_IML_MMCF",
    "france": "NGM_EPG0_IML_NUS-NFR_MMCF",
    "indonesia": "N9103ID2",
    "jamaica": "NGM_EPG0_IML_NUS-NJM_MMCF",
    "malaysia": "N9103MY2",
    "nigeria": "N9103NG2",
    "norway": "NGM_EPG0_NUS-NNO_IML_MMCF",
    "oman": "N9103MU2",
    "peru": "NGM_EPG0_NUS-NPE_IML_MMCF",
    "qatar": "N9103QR2",
    "trinidad_and_tobago": "N9103TD2",
    "united_arab_emirates": "N9103UA2",
    "united_kingdom": "NGM_EPG0_IML_NUS-NUK_MMCF",
    "yemen": "NGM_EPG0_IML_NUS-NYE_MMCF",
    # LNG aggregate
    "united_states_lng_total": "N9103US2",
    # compressed natural gas
    "canada_compressed": "NGM_EPG0_INC_NUS-NCA_MMCF",
    "united_states_compressed_total": "NGM_EPG0_INC_NUS-Z00_MMCF",
}

EXPORT_SERIES_BY_COUNTRY = {
    # pipeline exports
    "canada_pipeline": "N9132CN2",
    "mexico_pipeline": "N9132MX2",
    "united_states_pipeline_total": "N9132US2",
    # LNG exports by vessel
    "argentina": "NGM_EPG0_EVE_NUS-NAT_MMCF",
    "australia": "NGM_EPG0_EVE_NUS-NAU_MMCF",
    "bahrain": "NGM_EPG0_EVE_NUS-NBA_MMCF",
    "bangladesh": "NGM_EPG0_EVE_NUS-NBG_MMCF",
    "barbados": "NGM_EPG0_EVE_NUS-NBB_MMCF",
    "belgium": "NGM_EPG0_EVE_NUS-NBE_MMCF",
    "brazil": "NGM_EPG0_EVE_NUS-NBR_MMCF",
    "chile": "NGM_EPG0_EVE_NUS-NCI_MMCF",
    "china": "NGM_EPG0_EVE_NUS-NCH_MMCF",
    "colombia": "NGM_EPG0_EVE_NUS-NCO_MMCF",
    "croatia": "NGM_EPG0_EVE_NUS-NHR_MMCF",
    "dominican_republic": "NGM_EPG0_EVE_NUS-NDR_MMCF",
    "egypt": "NGM_EPG0_EVE_NUS-NEG_MMCF",
    "el_salvador": "NGM_EPG0_EVE_NUS-NES_MMCF",
    "finland": "NGM_EPG0_EVE_NUS-NFL_MMCF",
    "france": "NGM_EPG0_EVE_NUS-NFR_MMCF",
    "germany": "NGM_EPG0_EVE_NUS-NGM_MMCF",
    "greece": "NGM_EPG0_EVE_NUS-NGR_MMCF",
    "haiti": "NGM_EPG0_EVE_NUS-NHA_MMCF",
    "india": "NGM_EPG0_EVE_NUS-NIN_MMCF",
    "indonesia": "NGM_EPG0_EVE_NUS-NID_MMCF",
    "israel": "NGM_EPG0_EVE_NUS-NIS_MMCF",
    "italy": "NGM_EPG0_EVE_NUS-NIT_MMCF",
    "jamaica": "NGM_EPG0_EVE_NUS-NJM_MMCF",
    "japan": "NGM_EPG0_EVE_NUS-NJA_MMCF",
    "jordan": "NGM_EPG0_EVE_NUS-NJO_MMCF",
    "kuwait": "NGM_EPG0_EVE_NUS-NKU_MMCF",
    "lithuania": "NGM_EPG0_EVE_NUS-NLH_MMCF",
    "malta": "NGM_EPG0_EVE_NUS-NM6_MMCF",
    "mauritania": "NGM_EPG0_EVE_NUS-NMR_MMCF",
    "mexico": "NGM_EPG0_EVE_NUS-NMX_MMCF",
    "netherlands": "NGM_EPG0_EVE_NUS-NNL_MMCF",
    "nicaragua": "NGM_EPG0_EVE_NUS-NNU_MMCF",
    "pakistan": "NGM_EPG0_EVE_NUS-NPK_MMCF",
    "panama": "NGM_EPG0_EVE_NUS-NPM_MMCF",
    "philippines": "NGM_EPG0_EVE_NUS-NRP_MMCF",
    "poland": "NGM_EPG0_EVE_NUS-NPL_MMCF",
    "portugal": "NGM_EPG0_EVE_NUS-NPO_MMCF",
    "russia": "NGM_EPG0_EVE_NUS-NRS_MMCF",
    "senegal": "NGM_EPG0_EVE_NUS-NSG_MMCF",
    "singapore": "NGM_EPG0_EVE_NUS-NSN_MMCF",
    "south_korea": "NGM_EPG0_EVE_NUS-NKS_MMCF",
    "spain": "NGM_EPG0_EVE_NUS-NSP_MMCF",
    "taiwan": "NGM_EPG0_EVE_NUS-NTW_MMCF",
    "thailand": "NGM_EPG0_EVE_NUS-NTH_MMCF",
    "turkiye": "NGM_EPG0_EVE_NUS-NTU_MMCF",
    "united_arab_emirates": "NGM_EPG0_EVE_NUS-NTC_MMCF",
    "united_kingdom": "NGM_EPG0_EVE_NUS-NUK_MMCF",
    # LNG aggregate
    "united_states_lng_total": "N9133US2",
    # truck exports
    "canada_truck": "NGM_EPG0_ETR_NUS-NCA_MMCF",
    "mexico_truck": "NGM_EPG0_ETR_NUS-NMX_MMCF",
    "united_states_truck_total": "NGM_EPG0_ETR_NUS-Z00_MMCF",
    # compressed natural gas exports
    "canada_compressed": "NGM_EPG0_ENC_NUS-NCA_MMCF",
    "united_states_compressed_total": "NGM_EPG0_ENC_NUS-Z00_MMCF",
}

FUTURES_SERIES_BY_CONTRACT = {
    1: "RNGC1",
    2: "RNGC2",
    3: "RNGC3",
    4: "RNGC4",
}


# ===============================
# Natural Gas – Proved Reserves
# Wet, After Lease Separation
# Associated-Dissolved (BCF)
# ===============================

NG_PROVED_WET_ASSOC_BY_STATE = {
    "al": "RNGR41SAL_1",  # Alabama
    "ak": "RNGR41SAK_1",  # Alaska
    "ar": "RNGR41SAR_1",  # Arkansas
    "ca": "RNGR41SCA_1",  # California
    "co": "RNGR41SCO_1",  # Colorado
    "fl": "RNGR41SFL_1",  # Florida
    "ks": "RNGR41SKS_1",  # Kansas
    "ky": "RNGR41SKY_1",  # Kentucky
    "la": "RNGR41SLA_1",  # Louisiana
    "mi": "RNGR41SMI_1",  # Michigan
    "ms": "RNGR41SMS_1",  # Mississippi
    "mt": "RNGR41SMT_1",  # Montana
    "nd": "RNGR41SND_1",  # North Dakota
    "nm": "RNGR41SNM_1",  # New Mexico
    "ny": "RNGR41SNY_1",  # New York
    "oh": "RNGR41SOH_1",  # Ohio
    "ok": "RNGR41SOK_1",  # Oklahoma
    "pa": "RNGR41SPA_1",  # Pennsylvania
    "tx": "RNGR41STX_1",  # Texas
    "ut": "RNGR41SUT_1",  # Utah
    "va": "RNGR41SVA_1",  # Virginia
    "wv": "RNGR41SWV_1",  # West Virginia
    "wy": "RNGR41SWY_1",  # Wyoming
    # U.S. total
    "us": "RNGR41NUS_1",
    "all": "RNGR41NUS_1",
}

# ===============================
# Natural Gas – Proved Reserves
# Wet, After Lease Separation
# Nonassociated (BCF)
# ===============================

NG_PROVED_WET_NONASSOC_BY_STATE = {
    "al": "RNGR31SAL_1",  # Alabama
    "ak": "RNGR31SAK_1",  # Alaska
    "ar": "RNGR31SAR_1",  # Arkansas
    "ca": "RNGR31SCA_1",  # California
    "co": "RNGR31SCO_1",  # Colorado
    "fl": "RNGR31SFL_1",  # Florida
    "ks": "RNGR31SKS_1",  # Kansas
    "ky": "RNGR31SKY_1",  # Kentucky
    "la": "RNGR31SLA_1",  # Louisiana
    "mi": "RNGR31SMI_1",  # Michigan
    "ms": "RNGR31SMS_1",  # Mississippi
    "mt": "RNGR31SMT_1",  # Montana
    "nd": "RNGR31SND_1",  # North Dakota
    "nm": "RNGR31SNM_1",  # New Mexico
    "ny": "RNGR31SNY_1",  # New York
    "oh": "RNGR31SOH_1",  # Ohio
    "ok": "RNGR31SOK_1",  # Oklahoma
    "pa": "RNGR31SPA_1",  # Pennsylvania
    "tx": "RNGR31STX_1",  # Texas
    "ut": "RNGR31SUT_1",  # Utah
    "va": "RNGR31SVA_1",  # Virginia
    "wv": "RNGR31SWV_1",  # West Virginia
    "wy": "RNGR31SWY_1",  # Wyoming
    # U.S. total
    "us": "RNGR31NUS_1",
    "all": "RNGR31NUS_1",
}

# ===============================
# Natural Gas Plant Liquids
# Proved Reserves (MMBbl)
# ===============================

NGL_PROVED_BY_STATE = {
    "al": "RL2R01SAL_1",  # Alabama
    "ak": "RL2R01SAK_1",  # Alaska
    "ar": "RL2R01SAR_1",  # Arkansas
    "ca": "RL2R01SCA_1",  # California
    "co": "RL2R01SCO_1",  # Colorado
    "fl": "RL2R01SFL_1",  # Florida
    "ks": "RL2R01SKS_1",  # Kansas
    "ky": "RL2R01SKY_1",  # Kentucky
    "la": "RL2R01SLA_1",  # Louisiana
    "mi": "RL2R01SMI_1",  # Michigan
    "ms": "RL2R01SMS_1",  # Mississippi
    "mt": "RL2R01SMT_1",  # Montana
    "nd": "RL2R01SND_1",  # North Dakota
    "nm": "RL2R01SNM_1",  # New Mexico
    "ny": "RL2R01SNY_1",  # New York
    "oh": "RL2R01SOH_1",  # Ohio
    "ok": "RL2R01SOK_1",  # Oklahoma
    "pa": "RL2R01SPA_1",  # Pennsylvania
    "tx": "RL2R01STX_1",  # Texas
    "ut": "RL2R01SUT_1",  # Utah
    "va": "RL2R01SVA_1",  # Virginia
    "wv": "RL2R01SWV_1",  # West Virginia
    "wy": "RL2R01SWY_1",  # Wyoming
    # U.S. total
    "us": "RL2R01NUS_1",
    "all": "RL2R01NUS_1",
}


# ===============================
# Natural Gas – Expected Future Production
# Dry Natural Gas (BCF)
# ===============================

NG_EFP_DRY_BY_STATE = {
    "al": "RNGR11SAL_1",  # Alabama
    "ak": "RNGR11SAK_1",  # Alaska
    "ar": "RNGR11SAR_1",  # Arkansas
    "ca": "RNGR11SCA_1",  # California
    "co": "RNGR11SCO_1",  # Colorado
    "fl": "RNGR11SFL_1",  # Florida
    "ks": "RNGR11SKS_1",  # Kansas
    "ky": "RNGR11SKY_1",  # Kentucky
    "la": "RNGR11SLA_1",  # Louisiana
    "mi": "RNGR11SMI_1",  # Michigan
    "ms": "RNGR11SMS_1",  # Mississippi
    "mt": "RNGR11SMT_1",  # Montana
    "nd": "RNGR11SND_1",  # North Dakota
    "nm": "RNGR11SNM_1",  # New Mexico
    "ny": "RNGR11SNY_1",  # New York
    "oh": "RNGR11SOH_1",  # Ohio
    "ok": "RNGR11SOK_1",  # Oklahoma
    "pa": "RNGR11SPA_1",  # Pennsylvania
    "tx": "RNGR11STX_1",  # Texas
    "ut": "RNGR11SUT_1",  # Utah
    "va": "RNGR11SVA_1",  # Virginia
    "wv": "RNGR11SWV_1",  # West Virginia
    "wy": "RNGR11SWY_1",  # Wyoming
    # U.S. total
    "us": "RNGR11NUS_1",
    "all": "RNGR11NUS_1",
}
