import logging
import os
from logging.handlers import RotatingFileHandler

schoolparser_log_name = os.path.normpath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../", "logs", "autoengage.log"
    )
)

logger = logging.getLogger(__name__)

# set logging level
logger.setLevel(logging.DEBUG)

# add file handler
file_handler = RotatingFileHandler(
    schoolparser_log_name, maxBytes=2000000, backupCount=10
)
formatter = logging.Formatter(
    "%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.propagate = True

# list of school urls
SCHOOL_URLS = [
    "https://burtonhighschool.net/",
    "https://www.smuhsd.org/capuchinohigh",
    "https://www.sfusd.edu/school/balboa-high-school",
    "https://www.sfusd.edu/school/downtown-high-school",
    "https://www.ousd.org/castlemont",
    "https://echs.schoolloop.com/",
]

SCHOOL_SOCIAL_URLS = {
    "Burton hs": [
        "https://burtonhighschool.net/departments/socialsciences.html",
        "https://burtonhighschool.net/departments/counseling.html",
    ],
    "Capuchino hs": [
        "https://www.smuhsd.org/domain/661",
        "https://www.smuhsd.org/domain/225",
    ],
    "Balboa hs": [
        "https://www.sfusd.edu/school/balboa-high-school/students/counseling-department"
    ],
    "Castlemont hs": ["https://www.ousd.org/domain/4032"],
    "Downtown hs": ["https://www.sfusd.edu/school/downtown-high-school"],
    "El Camino hs": [
        "https://sites.google.com/ssfusd.org/elcaminocounseling/contact?authuser=0",
    ],
    "Galileo hs": [
        "https://sites.google.com/sfusd.edu/galileocounselingdepartment/contact-us?authuser=0",
    ],
    "Ida B Wells hs": [
        "https://www.sfusd.edu/school/ida-b-wells-high-school/about-our-school/staff-directory",
    ],
    "Independence hs": ["https://www.sfusd.edu/school/independence-high-school"],
    "Jefferson hs": ["https://www.juhsd.net/Page/553"],
    "John O'Connell hs": [
        "https://www.sfusd.edu/school/john-oconnell-high-school/student-services/counseling-services"
    ],
    "June Jordan hs": [],
    "Abraham Lincoln hs": ["https://www.sfusd.edu/school/abraham-lincoln-high-school"],
    "Lowell hs": [
        "https://www.sfusd.edu/school/lowell-high-school/school-information/contact-information"
    ],
    "Mills hs": [
        "https://www.smuhsd.org/domain/840",
        "https://www.smuhsd.org/domain/206",
    ],
    "Mission hs": [
        "https://www.sfusd.edu/school/mission-high-school/our-teams/counselors",
        "https://www.sfusd.edu/school/mission-high-school/our-teams/teachers/social-studies-department",
    ],
    "Oakland hs": [
        "https://www.ousd.org/domain/1723",
        "https://www.ousd.org/Page/5634",
    ],
    "Oceana hs": ["https://www.juhsd.net/domain/50",],
    "Raoul Wallenberg Traditional hs": [
        "https://www.sfusd.edu/school/raoul-wallenberg-traditional-high-school/school-info/departments/social-studies",
        "https://www.sfusd.edu/school/raoul-wallenberg-traditional-high-school/students/counseling",
    ],
    "Ruth Asawa San Francisco School of the Arts hs": [
        "https://www.sfusd.edu/school/ruth-asawa-san-francisco-school-arts/academics/academic-counseling",
    ],
    "San Mateo hs": [
        "https://www.smuhsd.org/domain/722",
        "https://www.smuhsd.org/domain/221",
    ],
    "Sequoia hs": ["https://www.sequoiahs.org/DEPARTMENT/Social-Studies/index.html"],
    "South San Francisco hs": ["https://ssfhs.schoolloop.com/job_listings",],
    "St. Ignatius hs": [
        "https://www.siprep.org/si-academics/academic-departments/counseling/counseling/meet-your-counselors",
    ],
    "Terra Nova hs": ["https://www.juhsd.net/Page/703",],
    "Thurgood Marshall hs": [
        "https://www.sfusd.edu/school/thurgood-marshall-academic-high-school/student/counseling-department/meet-counselors"
    ],
    "Washington hs": ["https://sites.google.com/sfusd.edu/counseling/counselors/"],
    "Westmoor hs": [
        "https://www.juhsd.net/Page/940",
        "https://www.juhsd.net/domain/209",
    ],
}
