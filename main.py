import os

# commands = input("Что вы хотите сделать?")

class Access():
    def pravi_file(self):
        print(f"вы пытаетесь управлять доступами пользователей для файлов\n")
        self.file_prava = input(f"введите названия файла с которым хотите работать\n")
        self.file_opcii = input(f"введите опции для файла с которым хотите работать\n")
        print(f"команды для разрешения\n"
              f" (-r)-для разрешения чтения\n"
              f" (-w)-для разрешения записи\n"
              f" (-x)-для разрешения выполнения\n")
        os.system(f"chmod  {self.file_opcii} {self.file_prava}")
        return Funcii().vibor_func()

    def pravi_katalog(self):
        print(f"вы пытаетесь управлять доступами пользователей для каталогов\n")
        self.katalog_prava = input(f"введите названия каталога с которым хотите работать\n")
        self.katalog_opcii = input(f"введите опции для каталога с которым хотите работать\n")
        os.system(f"chmod  {self.file_opcii} {self.file_prava}")

    def open_file(self):
        self.open_file = input("введите название папки который хотите открыть")
        os.system(f"nano {self.open_file}")
        return Funcii().vibor_func()

    def create_file(self):
        self.file_name = input("введите название файла в формате 'text.txt'\n")
        self.file_razreweniya = input('введите опции для разрешения пользователя')
        os.system(f"touch {self.file_name} ")
        return Funcii().vibor_func()

    def create_kotalog(self):
        self_kotalog = input(f"введите имя каталога\n")
        os.system(f"mkdir {self_kotalog}")
        return Funcii().vibor_func()

    def admin_user(self):
        self.user_admin = input("введите имя пользователя для доступа Админестратированые привелегии")
        os.system(f"usermod -G root {self.user_admin}")
        return Funcii().vibor_func()

    def add_group(self):
        self.group_name = input("введите название группы\nв который хотите добавить пользователя:\n")
        self.user_name = input("введите имя пользователя\n")
        os.system(f"usermod -aG {self.group_name} {self.user_name}")
        return Funcii().vibor_func()

    def create_gr(self):
        self.name_group = input("введите имя для группы\n")
        os.system(f"sudo groupadd {self.name_group}")
        print(f"{self.name_group} успешна создана!\n")
        return Funcii().vibor_func()

    def useradd(self):
        # os.system("sudo -S su")
        self.user = input("введите имя пользователя:\n")
        os.system(f"adduser {self.user}")
        self.pas = input('введите пароль пользователя:\n')
        os.system(f"echo -e PassWord'@1\nPassWord@1' |passwd {self.pas}")
        print(f"пользователь {self.user} успешно создан\n")
        return Funcii().vibor_func()

    def other_command(self):
        self.other = input("")
        os.system({self.other_command()})
        return Funcii().vibor_func()

class Funcii():
    def vibor_func(self):
        command = input(f"Выберите функцию для работы\n"
                        f"1. Создание каталога\n"
                        f"2. Создание файла\n"
                        f"3. создание группы\n"
                        f"4. добавление пользователей в группу\n"
                        f"5. Управления правами каталога\n"
                        f"6. Управления правами файла\n"
                        f"7. Управления рут правами пользователей\n"
                        f"8. Создать пользователей\n"
                        f"9. Открыть файл\n"
                        f"10. другие команды\n")

        if command == '1':
            return Access().create_kotalog()
        elif command == '2':
            return Access().create_file()
        elif command == '3':
            return Access().create_gr()
        elif command == "4":
            return Access().add_group()
        elif command == "5":
            return Access().pravi_katalog()
        elif command == "6":
            return Access().pravi_file()
        elif command == '7':
            return Access().admin_user()
        elif command == '8':
            return Access().useradd()
        elif command == '9':
            return Access().open_file()
        elif command == '10':
            return Access().other_command()
        else:
            return ("exit()")


if __name__ == '__main__':
    Funcii().vibor_func()
