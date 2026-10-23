class Course:
    def __init__(self,courseId,courseName,courseAdmin,quiz,handson):
        self.__courseId=courseId
        self.__courseName=courseName
        self.__courseAdmin=courseAdmin
        self.__quiz=quiz
        self.__handson=handson

    def get_courseId(self):
        return self.__courseId

    def get_courseName(self):
        return self.__courseName

    def get_courseAdmin(self):
        return self.__courseAdmin

    def get__quiz(self):
        return self.__quiz

    def get__handson(self):
        return self.__handson

    def set__courseId(self,courseId):
        self.__courseId=courseId

    def set_courseName(self,courseName):
        self.__courseName=courseName
    
    def set_courseAdmin(self,courseAdmin):
        self.__courseAdmin=courseAdmin
    
    def set__quiz(self,quiz):
        self.__quiz=quiz
    
    def set__handson(self,handson):
        self.__handson=handson
class courseProgram:
    @staticmethod
    def findAvgOfQuizByAdmin(course,admin):
        total=0
        count=0
        for i in course:
            if admin==i.get__courseAdmin():
                total+=i.get__quiz()
                count+=1
        if count==0:
            return 0
        avrage=total//count
        return avrage

    @staticmethod
    def sortCourseByHandsOn(course,value):
        ans=[]
        for i in course:
            if value>i.get__handson():
                ans.append(i)
        if len(ans)==0:
            return None
        ans.sort(key=lambda x:x.get__handson())

        return ans

    if __name__=="__main__":
    n=int(input())
    course=[]
    for i in range(n):
        courseId=int(input())
        courseName=input()
        courseAdmin=input()
        quiz=int(input())
        handson=int(input())

        c=Course(courseId,courseName,courseAdmin,quiz,handson)
        course.append(c)

    admin=input()
    value=int(input())

    avg=courseProgram.findAvgOfQuizByAdmin(course,admin)

    if avg==0:
        print("no course")
    else:
        print(avg)
        