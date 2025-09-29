import requests


def reply_message(reply_token, messages, access_token):
    reply_message_api = 'https://api.line.me/v2/bot/message/reply'
    headers = {'Authorization': f'Bearer {access_token}'}

    requests.post(
        reply_message_api,
        json={
            'replyToken': reply_token,
            'messages': messages
        },
        headers=headers
    )


def create_bubble(kind, icon, title, data, header_color, button_color):
    bubble = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "backgroundColor": header_color,
            "contents": [
                {
                    "type": "text",
                    "text": icon,
                    "size": "3xl",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": title,
                    "size": "lg",
                    "align": "center",
                    "weight": "bold",
                    "color": "#3A2529"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "color": button_color,
                    "margin": "md",
                    "action": {
                        "type": "postback",
                        "label": item,
                        "data": f"{kind}_selected={item}"
                    }
                }
                for item in data
            ]
        }
    }

    return bubble


def create_skill_eval_record_button():
    quick_reply = {
        'items': [
            {
                'type': 'action',
                'action': {
                    'type': 'postback',
                    'label': '查看目前的技能等級',
                    'data': 'assessment_record'
                }
            }
        ]
    }

    return quick_reply


def create_skill_confirm_template(text, labels, skill_name):
    template = [
        {
            'type': 'template',
            'altText': '技能選擇確認',
            'template': {
                'type': 'confirm',
                'text': text,
                'actions': [
                    {
                        'type': 'postback',
                        'label': labels[0],
                        'data': f'skill_confirmed=yes&skill={skill_name}'
                    },
                    {
                        'type': 'postback',
                        'label': labels[1],
                        'data': f'skill_confirmed=no&skill={skill_name}'
                    }
                ]
            }
        }
    ]

    return template


def create_evaluation_box(description, level, skill_name):
    box = {
        "type": "box",
        "layout": "horizontal",
        "backgroundColor": "#e8f4fd",
        "cornerRadius": "8px",
        "margin": "md",
        "paddingAll": "sm",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "paddingAll": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": description,
                        "size": "md",
                        "color": "#333333",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": level,
                        "size": "sm",
                        "color": "#666666",
                        "margin": "xs"
                    }
                ],
                "action": {
                    "type": "postback",
                    "data": f"level_selected={level}&skill={skill_name}"
                }
            }
        ]
    }

    return box


def create_pdf_template(title, text, thumbnail_image_url, uri, is_course=False, target_job=None):
    template = [
        {
            'type': 'template',
            'altText': title,
            'template': {
                'type': 'buttons',
                'thumbnailImageUrl': thumbnail_image_url,
                'title': title,
                'text': text,
                'actions': [
                    {
                        'type': 'uri',
                        'label': '立即下載',
                        'uri': uri
                    }
                ]
            }
        }
    ]

    if is_course:
        template[0]['template']['actions'].append(
            {
                'type': 'postback',
                'label': '查看課程連結',
                'data': f'course_link&target_job={target_job}'
            }
        )

    return template
