# buddy_test

Specifications:

    There can be multiple questionnaires
    Questionnaires have like title and description
    Each questionnaires can have many questions
    Questions have question text
    Each question has a type like: single choice, multiple choice, yes/no, text, number, range slider, etc
    A user can answer questions in a questionnaire (the answer, timestamp and user id, etc. neccessary will be stored)

Additional specifications (plus points):

    Localisation (translation) support for the system (the questionnaires with the questions can be in multiple languages)
    The history of questionnaires and questions are stored (the questionnaires or questions have version/revision number). So for example if a change to question text is done, it will create a new question with a new revision number).
    There are dependencies between questions in a way that the question is not shown until a dependency is met (e.g. would need to)

Implementation of Django models and some user interface to manage the questions and questionnaires.

Technologies:

    Django framework
    PostgreSQL database
    Code in Github
    Code hosted somewhere (e.g. on Heroku free account) to demonstrate the application in function

Usages:

    - Use admin page (http://url.to.the.page/admin)for managing questionaires, questions, and users.
    - Can create questionaire along with multiple questions. But the question metadata such as answers for multiple choice question must be inserted in the MultipleChoiceQuestion admin page.
    - Use http://url.to.the.page/questionaire to answer questionaire (login required).
    - Changed questions will create a new version one (on branch question_provision). Use admin question's actions to select the version

Assumption:

    - Not handle setting multiple versions of the same question selected.
    - Not implement localisation
