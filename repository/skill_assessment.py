class SkillAssessmentRepository:
    def __init__(self, connection):
        self.connection = connection

    def save_assessment(self, user_id, skill_name, level):
        cursor = self.connection.cursor()

        try:
            sql_cmd = '''
            INSERT INTO skill_assessment 
            VALUES (%s, %s, %s) 
            ON DUPLICATE KEY UPDATE 
            user_level = VALUES(user_level)
            '''
            cursor.execute(sql_cmd, (user_id, skill_name, level))
            self.connection.commit()

            return True
        except Exception as e:
            print(f'儲存評估結果失敗：{e}')
            self.connection.rollback()

            return False
        finally:
            cursor.close()

    def get_user_skill(self, user_id, skill_name):
        cursor = self.connection.cursor()

        try:
            sql_cmd = '''
            SELECT skill_name, user_level FROM skill_assessment 
            WHERE user_id = %s AND skill_name = %s
            '''
            cursor.execute(sql_cmd, (user_id, skill_name))

            return cursor.fetchone()
        except Exception as e:
            print(f'查詢技能評估失敗：{e}')

            return None
        finally:
            cursor.close()

    def get_user_all_skills(self, user_id):
        cursor = self.connection.cursor()

        try:
            sql_cmd = '''
            SELECT skill_name, user_level FROM skill_assessment 
            WHERE user_id = %s
            '''
            cursor.execute(sql_cmd, (user_id,))

            return cursor.fetchall()
        except Exception as e:
            print(f'查詢所有技能評估失敗：{e}')

            return []
        finally:
            cursor.close()
