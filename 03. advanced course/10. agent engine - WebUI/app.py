from google.cloud import storage
import cloudpickle
import vertexai
import streamlit as st

def vertexai_init():
    # 환경 변수 설정 (선택 사항)
    PROJECT_ID="gemini-demo-450807"
    LOCATION="us-central1"

    vertexai.init(project=PROJECT_ID, location=LOCATION)

def load_reasoning_engine_from_gcs(bucket_name: str, blob_name: str):
    """
    GCS에 저장된 pkl 파일을 로드하여 ReasoningEngine 객체를 반환합니다.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # pkl 파일 다운로드 및 로드
    with blob.open("rb") as f:
        loaded_engine = cloudpickle.load(f)
    return loaded_engine

def web_ui(agent):
    st.header(":sparkles: Calc_web", divider="rainbow")
    st.subheader("Input")

    input_str = st.text_input(
        "Enter contents: \n\n", key="input_str", value=""
    )

    process_btn = st.button("process...", key="process_btn")

    if process_btn and input_str:
        with st.spinner("processing..."):
            result = agent.query(input=input_str)
            st.write(result["output"])


if __name__ == "__main__":
    vertexai_init()
    BUCKET_NAME = "jin62-staging-gemini-demo-450807"  # 실제 버킷 이름으로 변경
    BLOB_NAME = "reasoning_engine/reasoning_engine.pkl"  # 실제 pkl 파일 경로로 변경

    # ReasoningEngine 로드
    loaded_engine = load_reasoning_engine_from_gcs(BUCKET_NAME, BLOB_NAME)
    web_ui(loaded_engine)
    