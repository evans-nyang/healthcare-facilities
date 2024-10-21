# Healthcare Facility Assistant

## Problem Description

Healthcare facilities are a critical component of any healthcare system. They provide the necessary infrastructure for the delivery of healthcare services. However, the availability of healthcare facilities is not uniform across different regions, some regions have a higher concentration compared to others. This disparity in the distribution can have a significant impact on the health outcomes of the population. In this project, we will explore the distribution of healthcare facilities in Kenya and identify regions that are underserved in terms of healthcare facilities.

The goal of this project is to create a tool that will help users find healthcare facilities information in different regions of Kenya. The tool will provide information on the number of healthcare facilities in a given region, the type of facilities available, their location and other related information. This will help users to identify regions that are underserved and in need of additional resources.

## Data Description

The data used in this project is sourced from the Kenya Master Health Facility List (KMHFL). The KMHFL is a comprehensive database of all health facilities in Kenya. It contains information on the location, type, and other related information of healthcare facilities in the country. The data is available in a CSV format and will be used to create the tool.

The dataset contains the following columns:

- **Facility Code:** A unique identifier code assigned to the facility.
- **Facility Name:** The name of the healthcare facility.
- **Keph Level:** The keph level of the facility (e.g. Level 4, Level 5).
- **Facility Type:** The type of healthcare facility (e.g. hospital, clinic, dispensary).
- **Facility Owner:** The owner of the facility (e.g. government, private).
- **County:** The county where the facility is located.
- **Sub-County:** The sub-county where the facility is located.
- **Constituency:** The constituency where the facility is located.
- **Ward:** The ward where the facility is located.
- **Operation Status:** The status of the facility (e.g. operational, closed).
- **Open_whole_day:** Whether the facility is open whole day.
- **Open_public_holidays:** Whether the facility is operational during public holidays.
- **Open_weekends:** Whether the facility operates during weekends.
- **Open_late_night:** Whether the facility is operational at night.
- **Approved:** Approval status of the healthcare facility.
- **Public visible:** Visibility status of the healthcare facility.
- **Closed:** Operational status of the facility i.e closed or not closed.

## Project Overview

The Healthcare Facility Assistant is a RAG application for assisting users with their healthcare facilities information needs. The application provides users with the following functionalities:

1. **Search for Healthcare Facilities:** Users can search for healthcare facilities by county, sub-county, constituency, ward, facility type, and facility owner. The application will display a list of healthcare facilities that match the search criteria.

2. **View Facility Details:** Users can view detailed information about a specific healthcare facility by selecting it from the search results. The application will display information such as the facility name, type, location, and other related information.

3. **Identify Underserved Regions:** The application will analyze the distribution of healthcare facilities in different regions and identify regions that are underserved. Users can view a map that highlights regions with a low concentration of healthcare facilities.

4. **Get Directions:** Users can get directions to a specific healthcare facility by selecting it from the search results. The application will display a map with the location of the facility and provide directions from the user's current location.

5. **Contact Facility:** Users can contact a specific healthcare facility by selecting it from the search results. The application will display contact information such as phone number, email address, and website (if available).

The Healthcare Facility Assistant is designed to be user-friendly and intuitive, providing users with easy access to healthcare facilities information. It aims to improve the accessibility of healthcare services and help users make informed decisions about their healthcare needs.

## Ingestion

## Evaluation

Check out the code for the evaluation [here](notebooks/ragTest.ipynb)

### Retrieval

The basic approach - using minsearch without any boosting - gave the following metrics:

```
{
  "recall": 0.0,
  "precision": 0.0,
  "f1": 0.0,
  "accuracy": 0.0
}
```

### RAG flow

## Monitoring
