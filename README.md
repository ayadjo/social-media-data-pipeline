# End-to-End Data Engineering Pipeline

A comprehensive Data Engineering project designed to ingest, process, store, and visualize data from public APIs using a modern big data stack. 

This project serves as a practical implementation of core data engineering concepts: data ingestion, batch processing, real-time streaming, data warehousing, and dashboarding.

---

## 📌 Phase I: Data Sources & API Access

* **Selected Data Source:** YouTube Data API v3 (Public Data)
* **Setup & Authentication:** 
  * Configured a dedicated project (`DE-YouTube-Project`) on Google API Console.
  * Generated and secured a public **API Key** restricted to YouTube Data API v3.
* **Connectivity Verification:**
  * Tested REST API access via `cURL` (HTTP GET requests) ensuring valid JSON responses.
  * Implemented a programmatic connection test using the official Python client (`google-api-python-client`), verifying successful endpoint responses for video search queries.
* **Streaming Capability Note:** YouTube Data API v3 does not natively support real-time WebSocket streaming; batch/polling ingestion strategies will be applied via Apache NiFi.

### Core Entities & Attributes
* **Video** (`videos` / `search`): 
  `id`, `snippet.title`, `snippet.description`, `snippet.publishedAt`, `snippet.channelId`, `statistics.viewCount`, `statistics.likeCount`, `statistics.commentCount`, `contentDetails.duration`
* **Channel** (`channels`): 
  `id`, `snippet.title`, `snippet.description`, `statistics.subscriberCount`, `statistics.videoCount`
* **CommentThread** (`commentThreads`): 
  `id`, `snippet.videoId`, `snippet.topLevelComment.snippet.textDisplay`, `snippet.topLevelComment.snippet.authorDisplayName`