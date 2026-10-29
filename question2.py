class employee:
    def __init__(self, employeeid, name, branch, rating, company_transport):
        self.__employeeid = employeeid
        self.__name = name
        self.__branch = branch
        self.__rating = rating
        self.__company_transport = company_transport

    def get_employeeid(self):
        return self.__employeeid

    def set_employeeid(self, employeeid):
        self.__employeeid = employeeid

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_branch(self):
        return self.__branch

    def set_branch(self, branch):
        self.__branch = branch

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_company_transport(self):
        return self.__company_transport

    def set_company_transport(self, company_transport):
        self.__company_transport = company_transport


class Myclass:

    @staticmethod
    def findCountOfEmployeesUsingCompTransport(Employee, branch):
        count = 0

        for i in Employee:
            if i.get_company_transport() == True and i.get_branch() == branch:
                count += 1

        return count

    @staticmethod
    def findEmployeeWithSecondHighestRating(Employee):
        eligible = []

        for i in Employee:
            if i.get_company_transport() == False:
                eligible.append(i)

        if len(eligible) < 2:
            return None

        eligible.sort(key=lambda x: x.get_rating(), reverse=True)

        return eligible[1]


if __name__ == "__main__":
    Employee = []

    for i in range(4):
        employeeid = int(input())
        name = input()
        branch = input()
        rating = float(input())
        company_transport = input().lower() == "true"

        emp = employee(employeeid, name, branch, rating, company_transport)
        Employee.append(emp)

    branch = input()

    count = Myclass.findCountOfEmployeesUsingCompTransport(Employee, branch)

    if count > 0:
        print(count)
    else:
        print("No such Employees")

    result = Myclass.findEmployeeWithSecondHighestRating(Employee)

    if result is not None:
        print(result.get_employeeid())
        print(result.get_name())
    else:
        print("All Employees using company transport")