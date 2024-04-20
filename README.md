This script does the following:

1. Uses 50 threads for concurrent scraping.
2. Adds a pause of 1 second for each URL from the same domain.
3. Follows all internal URLs within the domain being scraped.
4. Scrapes from "facebook.com".
5. Scrapes only for external URLs.
6. Deletes duplicate URLs before importing them into the file.
7. Adds all URLs to the "urls.txt" file in the same directory as the script.
8. Writes URLs to the "urls.txt" file in batches of 1000 to prevent bottlenecks.
