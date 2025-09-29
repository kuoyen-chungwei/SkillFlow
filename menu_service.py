import uuid

from line_helper import (
    reply_message, create_bubble, create_skill_eval_record_button,
    create_skill_confirm_template, create_evaluation_box, create_pdf_template
)
from data.skill_data import (
    languages, frameworks, data_analysis,
    system_management, information_security, version_control
)
from data.job_data import (
    software_development, system,
    analysis, management, job_skill
)
from data.learning_data import learning_paths, learning_resources, course_links
from report.pdf_report import EnhancedSkillRadarPDFReport, CareerSpecificReportGenerator


class MenuService:
    def __init__(self, reply_token, access_token, base_url):
        self.reply_token = reply_token
        self.access_token = access_token
        self.base_url = base_url

    def reply_skill_menu(self):
        messages = [
            {
                'type': 'text',
                'text': '歡迎使用「職能分析」！請選擇您欲檢測的技能：'
            },
            {
                "type": "flex",
                "altText": "技能選單",
                "contents": {
                    "type": "carousel",
                    "contents": [
                        create_bubble(
                            kind='skill',
                            icon='⌨️',
                            title='程式語言與網頁開發技術',
                            data=languages,
                            header_color='#d9ebfc',
                            button_color='#5aa4c8'
                        ),
                        create_bubble(
                            kind='skill',
                            icon='⌨️',
                            title='框架',
                            data=frameworks,
                            header_color='#d9ebfc',
                            button_color='#3d8db3'
                        ),
                        create_bubble(
                            kind='skill',
                            icon='📂',
                            title='資料庫與資料分析',
                            data=data_analysis,
                            header_color='#D6C3BF',
                            button_color='#832a47'
                        ),
                        create_bubble(
                            kind='skill',
                            icon='🎨',
                            title='作業系統與系統管理',
                            data=system_management,
                            header_color='#D6C3BF',
                            button_color='#832a47'
                        ),
                        create_bubble(
                            kind='skill',
                            icon='🛠️️',
                            title='網路與資安',
                            data=information_security,
                            header_color='#d9ebfc',
                            button_color='#4c9cc3'
                        ),
                        create_bubble(
                            kind='skill',
                            icon='🌐',
                            title='版本控制',
                            data=version_control,
                            header_color='#d9ebfc',
                            button_color='#4c9cc3'
                        )
                    ]
                },
                'quickReply': create_skill_eval_record_button()
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def reply_assessment_record(self, skills):
        if not skills:
            messages = [
                {
                    'type': 'text',
                    'text': '您還沒有檢測過任何技能哦！'
                }
            ]

        else:
            skill_list = []
            for i, skill in enumerate(skills, 1):
                skill_name = skill[0]
                level = skill[1]

                skill_list.append(f'{i}. {skill_name}: {level}')

            skill_text = '\n'.join(skill_list)
            total_count = len(skills)

            messages = [
                {
                    "type": "flex",
                    "altText": "我的技能檔案",
                    "contents": {
                        "type": "bubble",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "backgroundColor": "#5aa4c8",
                            "paddingAll": "lg",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "📋 我的技能檔案",
                                    "size": "lg",
                                    "align": "center",
                                    "weight": "bold",
                                    "color": "#edf9ff"
                                },
                                {
                                    "type": "text",
                                    "text": f"總共評估過 {total_count} 項技能",
                                    "size": "sm",
                                    "color": "#0c445f",
                                    "align": "center",
                                    "margin": "sm"
                                }
                            ]
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "paddingAll": "lg",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": skill_text,
                                    "size": "sm",
                                    "color": "#333333",
                                    "wrap": True
                                }
                            ]
                        }
                    }
                }
            ]

        reply_message(self.reply_token, messages, self.access_token)

    def reply_skill_confirm(self, skill_name):
        messages = create_skill_confirm_template(
            text=f'您確定要檢測 {skill_name} 嗎？',
            labels=['是', '否'],
            skill_name=skill_name
        )

        reply_message(self.reply_token, messages, self.access_token)

    def reply_skill_confirm_with_memory(self, skill_name, existing_record):
        level = existing_record[1]
        messages = create_skill_confirm_template(
            text=f'您先前曾檢測過 {skill_name}，當時的等級為 {level}。要重新評估嗎？',
            labels=['重新評估', '算了'],
            skill_name=skill_name
        )

        reply_message(self.reply_token, messages, self.access_token)

    def reply_evaluation(self, skill_name):
        messages = [
            {
                "type": "flex",
                "altText": "實作能力評估",
                "contents": {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "backgroundColor": "#5aa4c8",
                        "paddingAll": "lg",
                        "contents": [
                            {
                                "type": "text",
                                "text": f"{skill_name} 實作能力評估",
                                "weight": "bold",
                                "size": "lg",
                                "color": "#edf9ff",
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": "請點擊符合您經歷的選項",
                                "size": "sm",
                                "color": "#0c445f",
                                "align": "center",
                                "margin": "sm"
                            }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "paddingAll": "lg",
                        "contents": [
                            create_evaluation_box(
                                description='沒有學過或只會基本用法',
                                level='Beginner',
                                skill_name=skill_name
                            ),
                            create_evaluation_box(
                                description='可完成小專案',
                                level='Intermediate',
                                skill_name=skill_name
                            ),
                            create_evaluation_box(
                                description='可獨立完成中型專案',
                                level='Advanced',
                                skill_name=skill_name
                            ),
                            create_evaluation_box(
                                description='可維護大型專案或參與開源專案',
                                level='Expert',
                                skill_name=skill_name
                            )
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "paddingAll": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "點擊任一選項",
                                "size": "xs",
                                "color": "#125474",
                                "align": "center"
                            }
                        ]
                    }
                }
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def handle_skill_eval_declined(self):
        text = '好的，若想檢測特定技能，歡迎隨時點擊「職能分析」哦$！'
        messages = [
            {
                'type': 'text',
                'text': text,
                'emojis': [
                    {
                        'index': text.find('$'),
                        'productId': '5ac1bfd5040ab15980c9b435',
                        'emojiId': '009'
                    }
                ]
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def reply_level_confirm(self, level, skill_name):
        messages = [
            {
                'type': 'template',
                'altText': '等級選擇確認',
                'template': {
                    'type': 'confirm',
                    'text': f'確認您的 {skill_name} 技能等級為 {level}？',
                    'actions': [
                        {
                            'type': 'postback',
                            'label': '確認',
                            'data': f'level_confirmed=yes&skill={skill_name}&level={level}'
                        },
                        {
                            'type': 'postback',
                            'label': '重新選擇',
                            'data': f'level_confirmed=no&skill={skill_name}'
                        }
                    ]
                }
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def handle_level_confirmed(self, skill_name, level, success):
        if success:
            text = f'✅ 系統已成功記錄您的 {skill_name} 技能等級（{level}）！'
        else:
            text = f'❌ 抱歉，系統在記錄您的 {skill_name} 技能等級（{level}）時發生錯誤，請稍後再試！'

        messages = [
            {
                'type': 'text',
                'text': text,
                'quickReply': create_skill_eval_record_button()
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def handle_level_declined(self, skill_name):
        self.reply_evaluation(skill_name)

    def reply_occupation_menu(self):
        messages = [
            {
                'type': 'text',
                'text': '歡迎使用「技能差距查詢」！請選擇您的目標職業：'
            },
            {
                "type": "flex",
                "altText": "職業選單",
                "contents": {
                    "type": "carousel",
                    "contents": [
                        create_bubble(
                            kind='occupation',
                            icon='💼',
                            title='軟體開發與技術',
                            data=software_development,
                            header_color='#d9ebfc',
                            button_color='#5aa4c8'
                        ),
                        create_bubble(
                            kind='occupation',
                            icon='💼',
                            title='系統與網路管理',
                            data=system,
                            header_color='#d9ebfc',
                            button_color='#3d8db3'
                        ),
                        create_bubble(
                            kind='occupation',
                            icon='💼',
                            title='資料處理與分析',
                            data=analysis,
                            header_color='#d9ebfc',
                            button_color='#3d8db3'
                        ),
                        create_bubble(
                            kind='occupation',
                            icon='💼',
                            title='管理',
                            data=management,
                            header_color='#d9ebfc',
                            button_color='#3d8db3'
                        )
                    ]
                },
                'quickReply': create_skill_eval_record_button()
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def reply_skill_report(self, occupation_name, user_skills):
        user_skills = dict(user_skills)

        report_generator = EnhancedSkillRadarPDFReport(job_skill)
        career_system = report_generator.career_recommender

        user_skills = {key: career_system.skill_levels[value] for key, value in user_skills.items()}

        target_job = occupation_name
        current_job_skills = job_skill[target_job]
        current_values = [user_skills.get(skill, 0) for skill in current_job_skills]

        target_values = [100] * len(current_job_skills)
        file_id = uuid.uuid4()
        filename = report_generator.generate_comprehensive_pdf_report(
            categories=current_job_skills,
            current_values=current_values,
            target_values=target_values,
            user_skills=user_skills,
            filename=f'static/{file_id}.pdf',
            title=f'{target_job}技能分析報告'
        )

        print(filename)

        messages = create_pdf_template(
            title=f'{target_job}技能分析報告',
            text='已根據您目前的技能等級與目標職業生成技能分析報表。',
            thumbnail_image_url='https://cdn-www.cw.com.tw/article/202308/article-64df22195aedf.jpg',
            uri=f'{self.base_url}/{filename}'
        )

        reply_message(self.reply_token, messages, self.access_token)

    def reply_course_menu(self):
        messages = [
            {
                'type': 'text',
                'text': '歡迎使用「課程推薦」！請選擇您的目標職業：'
            },
            {
                "type": "flex",
                "altText": "課程選單",
                "contents": {
                    "type": "carousel",
                    "contents": [
                        create_bubble(
                            kind='course',
                            icon='⌨️',
                            title='軟體開發與技術',
                            data=software_development,
                            header_color='#d9ebfc',
                            button_color='#5aa4c8'
                        ),
                        create_bubble(
                            kind='course',
                            icon='🧬',
                            title='系統與網路管理',
                            data=system,
                            header_color='#d9ebfc',
                            button_color='#3d8db3'
                        ),
                        create_bubble(
                            kind='course',
                            icon='🧬',
                            title='資料處理與分析',
                            data=analysis,
                            header_color='#d9ebfc',
                            button_color='#3d8db3'
                        ),
                        create_bubble(
                            kind='course',
                            icon='🧬',
                            title='管理',
                            data=management,
                            header_color='#d9ebfc',
                            button_color='#3d8db3'
                        )
                    ]
                },
                'quickReply': create_skill_eval_record_button()
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def reply_course_report(self, occupation_name, user_skills):
        user_skills = dict(user_skills)

        report_generator = CareerSpecificReportGenerator(job_skill, learning_paths, learning_resources)
        career_system = report_generator.career_recommender

        user_skills = {key: career_system.skill_levels[value] for key, value in user_skills.items()}

        target_job = occupation_name
        file_id = uuid.uuid4()
        filename = report_generator.generate_comprehensive_pdf_report(
            target_job,
            user_skills,
            f'static/{file_id}.pdf'
        )

        messages = create_pdf_template(
            title=f'{target_job}技能發展指南',
            text='已根據您目前的技能等級與目標職業生成了技能發展指南。',
            thumbnail_image_url='https://cdn-www.cw.com.tw/article/202308/article-64df22195aedf.jpg',
            uri=f'{self.base_url}/{filename}',
            is_course=True,
            target_job=target_job
        )

        reply_message(self.reply_token, messages, self.access_token)

    def reply_course_link(self, occupation_name, user_skills):
        user_skills = dict(user_skills)
        requirement = job_skill[occupation_name]

        links = []
        for skill in requirement:
            if skill in course_links:
                level = user_skills.get(skill, 'Beginner')
                links.extend(course_links[skill][level])

        text = '\n\n'.join(links)
        messages = [
            {
                'type': 'text',
                'text': text
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)

    def reply_developing_message(self):
        messages = [
            {
                'type': 'text',
                'text': '這項功能尚在開發中'
            }
        ]

        reply_message(self.reply_token, messages, self.access_token)
