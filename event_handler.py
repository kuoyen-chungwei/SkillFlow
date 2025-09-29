from menu_service import MenuService
from repository.skill_assessment import SkillAssessmentRepository


class EventHandler:
    def __init__(self, event, access_token, base_url, connection):
        self.event = event
        self.access_token = access_token
        self.base_url = base_url
        self.connection = connection

        self.reply_token = self.event['replyToken']
        self.user_id = self.event['source']['userId']
        self.menu_service = MenuService(self.reply_token, self.access_token, self.base_url)
        self.skill_repo = SkillAssessmentRepository(self.connection)

    def handle(self):
        if self.event['type'] == 'postback':
            self._handle_postback(self.event)

    def _handle_postback(self, event):
        postback_data = event['postback']['data']

        if postback_data.startswith('function_selected='):
            function_selected = postback_data.split('=')[1]

            if function_selected == '職能分析':
                self.menu_service.reply_skill_menu()
            elif function_selected == '技能差距':
                self.menu_service.reply_occupation_menu()
            elif function_selected == '推薦課程':
                self.menu_service.reply_course_menu()
            elif function_selected == '學習通知' or function_selected == '諮詢助教':
                self.menu_service.reply_developing_message()

        elif postback_data == 'assessment_record':
            user_skills = self.skill_repo.get_user_all_skills(self.user_id)
            self.menu_service.reply_assessment_record(user_skills)

        elif postback_data.startswith('skill_selected='):
            skill_name = postback_data.split('=')[1]
            existing_record = self.skill_repo.get_user_skill(self.user_id, skill_name)

            if existing_record:
                self.menu_service.reply_skill_confirm_with_memory(
                    skill_name,
                    existing_record
                )
            else:
                self.menu_service.reply_skill_confirm(skill_name)

        elif postback_data.startswith('skill_confirmed='):
            params = self._parse_postback_data(postback_data)

            if params['skill_confirmed'] == 'yes':
                self.menu_service.reply_evaluation(params['skill'])
            else:
                self.menu_service.handle_skill_eval_declined()

        elif postback_data.startswith('level_selected='):
            params = self._parse_postback_data(postback_data)
            self.menu_service.reply_level_confirm(
                params['level_selected'],
                params['skill']
            )

        elif postback_data.startswith('level_confirmed='):
            params = self._parse_postback_data(postback_data)

            if params['level_confirmed'] == 'yes':
                success = self.skill_repo.save_assessment(
                    self.user_id,
                    params['skill'],
                    params['level']
                )
                self.menu_service.handle_level_confirmed(
                    params['skill'],
                    params['level'],
                    success
                )
            else:
                self.menu_service.handle_level_declined(params['skill'])

        elif postback_data.startswith('occupation_selected='):
            occupation_name = postback_data.split('=')[1]
            user_skills = self.skill_repo.get_user_all_skills(self.user_id)

            self.menu_service.reply_skill_report(occupation_name, user_skills)

        elif postback_data.startswith('course_selected='):
            occupation_name = postback_data.split('=')[1]
            user_skills = self.skill_repo.get_user_all_skills(self.user_id)

            self.menu_service.reply_course_report(occupation_name, user_skills)

        elif postback_data.startswith('course_link'):
            occupation_name = postback_data.split('&')[1].split('=')[1]
            user_skills = self.skill_repo.get_user_all_skills(self.user_id)

            self.menu_service.reply_course_link(occupation_name, user_skills)

    @staticmethod
    def _parse_postback_data(postback_data):
        params = {}
        parts = postback_data.split('&')

        for part in parts:
            key, value = part.split('=')
            params[key] = value

        return params
