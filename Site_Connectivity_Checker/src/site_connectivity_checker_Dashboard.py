import streamlit as st
from site_connectivity_checker import check_site_connectivity , format_url
from concurrent.futures import ThreadPoolExecutor, as_completed


st.title("🌐 Website Connectivity Checker")
site_input = st.text_area("Enter URLs (one per line):")
 
if st.button("Check Websites"):
    raw_urls = [url.strip() for url in site_input.splitlines() if url.strip()]
    
    if not raw_urls:
        st.warning("Please enter at least one URL.")
    else:
        st.info("Checking connectivity...")

        websites = [format_url(url) for url in raw_urls]

        results = {}

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_site_connectivity, url): url for url in websites}
        for future in as_completed(future_to_url):
            url, result = future.result()
            results[url] = result

        for url in websites:
            st.write(results.get(url, f"❌ No result for {url}"))
