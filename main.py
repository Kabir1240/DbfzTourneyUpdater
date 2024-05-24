from startgg_functions import get_tournaments_by_owner
from update_google_doc import upload_doc
from owner_ids import *

MESSAGE_PATH = "doc_body.txt"
STARTGG_URL = "https://start.gg/"


# get the template for the google doc
with open(MESSAGE_PATH, 'r') as file:
    doc_body = file.read()


def update_com_link() -> None:
    """
    gets link for the upcoming city of mayhem event that week and updates the doc_body
    :return: None
    """
    global doc_body

    tournies = get_tournaments_by_owner(BUM_ID)

    com_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "City of Mayhem" in tourney["name"] and "Dragon Ball Fighterz" in tourney["name"]:
            com_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{com_link}", f"{STARTGG_URL}{com_link}")
    print(f"updating City Of Mayhem link {com_link}")


def update_wanted_link() -> None:
    """
    gets link for the upcoming wanted event that week and updates the doc_body
    :return: None
    """
    global doc_body

    tournies = get_tournaments_by_owner(DAMASCUS_ID)

    wanted_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "Wanted" in tourney["name"] and "DBFZ" in tourney["name"]:
            wanted_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{wanted_link}", f"{STARTGG_URL}{wanted_link}")
    print(f"Updating Wanted link: {wanted_link}")


def update_zwarrior_link() -> None:
    """
    gets link for the upcoming Online Warrior Z event that week and updates the doc_body
    :return: None
    """

    global doc_body

    tournies = get_tournaments_by_owner(TYRANT_ID)
    zwarrior_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "Online WarriorZ" in tourney["name"]:
            zwarrior_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{online_zwarrior_link}", f"{STARTGG_URL}{zwarrior_link}")
    print(f"updating Online WarriorZ link: {zwarrior_link}")


def update_fda_link() -> None:
    """
    gets link for the upcoming FighterZ Duel Academy that week and updates the doc_body
    :return: None
    """

    global doc_body

    tournies = get_tournaments_by_owner(NEO_JUDAI_ID)

    fda_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "FighterZ Duel Academy" in tourney["name"]:
            fda_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{fda_link}", f"{STARTGG_URL}{fda_link}")
    print(f"Updating FighterZ Duel Academy Link: {fda_link}")


def update_bfns_link() -> None:
    """
    gets link for the upcoming Battle for Ningen Supremacy event that week and updates the doc_body
    :return: None
    """
    global doc_body

    tournies = get_tournaments_by_owner(LINDSEY_ID)

    bfns_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "Battle for Ningen Supremacy" in tourney["name"]:
            bfns_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{bfns_link}", f"{STARTGG_URL}{bfns_link}")
    print(f"Updating Battle for Ningen Supremacy Link: {bfns_link}")


def update_iacon_link() -> None:
    """
    gets link for the upcoming Iacon that week and updates the doc_body
    :return: None
    """

    global doc_body

    tournies = get_tournaments_by_owner(DION_ID)

    iacon_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "{DBFZ PC}" in tourney["name"]:
            iacon_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{iacon_link}", f"{iacon_link}")
    print(f"Updating Iacon link: {iacon_link}")


def update_tns_link() -> None:
    """
    gets link for the upcoming Tampa Never Sleeps event that week and updates the doc_body
    :return: None
    """

    global doc_body

    tournies = get_tournaments_by_owner(TNS_ID, 50)
    tns_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "Dragon Ball Fighterz" in tourney["name"]:
            tns_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{tns_link}", f"{STARTGG_URL}{tns_link}")
    print(f"Updating Tampa Never Sleeps link: {tns_link}")


def update_dead_zone_link() -> None:
    """
    gets link for the upcoming dead zone circuit event that week and updates the doc_body
    :return: None
    """

    global doc_body

    tournies = get_tournaments_by_owner(LORD_BEERUS_ID)
    dead_zone_link = "No link ATM"
    for tourney in tournies["data"]["tournaments"]["nodes"]:
        if "DBFZ" in tourney["name"]:
            dead_zone_link = tourney["slug"]
            break

    doc_body = doc_body.replace("{dead_zone_link}", f"{STARTGG_URL}{dead_zone_link}")
    print(f"Updating Dead Zone Circuit link: {dead_zone_link}")


if __name__ == "__main__":
    update_wanted_link()
    update_com_link()
    update_zwarrior_link()
    update_fda_link()
    update_dead_zone_link()
    update_tns_link()
    update_iacon_link()
    update_bfns_link()

    upload_doc(doc_body)
