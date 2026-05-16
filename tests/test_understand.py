import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

FIXTURES = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_validate_scene_tags():
    from understand import VALID_SCENE_TAGS, validate_segments
    segments = [
        {"start": "00:00", "end": "00:10", "visual": "test", "scene": "intro"},
        {"start": "00:10", "end": "00:20", "visual": "test", "scene": "invalid-tag"},
    ]
    validated = validate_segments(segments)
    assert validated[0]['scene'] == 'intro'
    assert validated[1]['scene'] == 'other'


def test_parse_gemini_response():
    from understand import parse_gemini_response
    fixture_path = os.path.join(FIXTURES, 'gemini_response.json')
    with open(fixture_path, 'r') as f:
        raw = f.read()
    segments = parse_gemini_response(raw)
    assert len(segments) == 3
    assert segments[0]['scene'] == 'intro'
    assert segments[0]['start'] == '00:00'


def test_get_prompt():
    from understand import get_prompt
    prompt = get_prompt()
    assert 'visual' in prompt
    assert 'scene' in prompt
    assert 'JSON' in prompt


def test_valid_scene_tags_list():
    from understand import VALID_SCENE_TAGS
    assert 'intro' in VALID_SCENE_TAGS
    assert 'talking-head' in VALID_SCENE_TAGS
    assert 'other' in VALID_SCENE_TAGS
    assert len(VALID_SCENE_TAGS) == 20
