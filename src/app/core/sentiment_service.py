from typing import Any, final

import regex
import requests
from urllib3.util import parse_url

from app.core.model import Script, Sentiment


@final
class SentimentAnalyzer:
    def __init__(
        self,
        inference_endpoint_for_mixed: str,
        inference_endpoint_for_arabic: str | None = None,
        inference_endpoint_for_latin: str | None = None,
    ):
        self.session = requests.Session()
        for endpoint in [
            inference_endpoint_for_mixed,
            inference_endpoint_for_arabic,
            inference_endpoint_for_latin,
        ]:
            if endpoint is None:
                continue
            endpoint = parse_url(endpoint)
            health_endpoint = f"{endpoint.scheme}://{endpoint.authority}/health"
            try:
                response = self.session.get(health_endpoint)
                if response.status_code != 200:
                    raise RuntimeError(
                        f"No healthy upstream for sentiment classificaiton at {health_endpoint}"
                    )
            except Exception:
                raise RuntimeError(
                    f"No reachable upstream for sentiment classificaiton at {health_endpoint}"
                )

        self.inference_endpoint_for_mixed = inference_endpoint_for_mixed
        self.inference_endpoint_for_arabic = inference_endpoint_for_arabic
        self.inference_endpoint_for_latin = inference_endpoint_for_latin

    def analyze(self, text: str) -> Sentiment:
        inference_url = self.get_inference_endpoint_for_text(text)
        payload = self.get_payload(text, inference_url)
        try:
            response = self.session.post(inference_url, json=payload)
            if response.status_code != 200:
                raise RuntimeError(
                    "Sentiment classification upstream responded to an inference request with a non-200 status code."
                )
        except Exception:
            raise RuntimeError(
                f"No reachable upstream for sentiment classificaiton at {inference_url}"
            )

        return Sentiment(response.json()["data"][0]["label"])

    def get_payload(self, text: str, inference_url: str) -> dict[str, Any]:
        endpoint_path = parse_url(inference_url).path
        if endpoint_path == "/classify":
            # Pooling model such as BERT
            return dict(input=text, activation=True)
        elif endpoint_path == "/chat/completions":
            # Generative model such as Gemma
            raise NotImplementedError()
        else:
            raise NotImplementedError(
                f"No support for inference endpoint path {endpoint_path}"
            )

    def get_inference_endpoint_for_text(self, text: str) -> str:
        script = self.get_script_for_text(text)
        match (
            script,
            self.inference_endpoint_for_mixed,
            self.inference_endpoint_for_arabic,
            self.inference_endpoint_for_latin,
        ):
            case (
                (_, mixed_model, None, None)
                | (Script.MIXED, mixed_model, _, _)
                | (Script.ARABIC, mixed_model, None, _)
                | (Script.LATIN, mixed_model, _, None)
            ):
                return mixed_model
            case Script.ARABIC, _, arabic_model, _:
                return arabic_model
            case Script.LATIN, _, _, latin_model:
                return latin_model

    def get_script_for_text(self, text: str) -> Script:
        contains_arabic = regex.match(r"(?V1)\p{Script=Arabic}", text) is not None
        contains_latin = regex.match(r"(?V1)\p{Script=Latin}", text) is not None

        match contains_arabic, contains_latin:
            case True, True:
                return Script.MIXED
            case True, False:
                return Script.ARABIC
            case False, True:
                return Script.LATIN
            case False, False:
                return Script.MIXED
