import graphene
from graphene_file_upload.scalars import Upload
from graphene_django import DjangoObjectType, DjangoListField 
from .models import TeamMembers 

# BookType, qui adapte le Bookmodèle à un DjangoObjectType
class TeamMembersType(DjangoObjectType): 
    class Meta:
        model = TeamMembers
        fields = "__all__"

# La Queryclasse définit les requêtes GraphQL que l'API fournira aux clients
class Query(graphene.ObjectType):
    all_TeamMembers = graphene.List(TeamMembersType)
    TeamMembers = graphene.Field(TeamMembersType, teamMembers_id=graphene.Int())

    def resolve_all_TeamMembers(self, info, **kwargs):
        return TeamMembers.objects.all()

    def resolve_TeamMembers(self, info, teamMembers_id):
        return TeamMembers.objects.get(pk=teamMembers_id)

####################################################""
class TeamMembersInput(graphene.InputObjectType):
    id =graphene.ID()
    fullname = graphene.String()
    designation = graphene.String()
    photo = Upload(required=False)
    date_add = graphene.String()
    date_update = graphene.String()
    status = graphene.Boolean(default=True)

# procedure de creation
class CreateTeamMembers(graphene.Mutation):
    class Arguments:
        teamMembers_data = TeamMembersInput(required=True)

    teamMembers = graphene.Field(TeamMembersType)

    @staticmethod
    # In Python, the @staticmethod decorator is used to define static methods within a class. Static methods a
    # re methods that do not operate on the instance of the class and do not have access to the instance's data.
    def mutate(root, info, teamMembers_data=None):
        teamMembers_instance = TeamMembers( 
            fullname=teamMembers_data.fullname,
            designation=teamMembers_data.designation,
            photo = teamMembers_data.photo,
            date_add=teamMembers_data.date_add,
            date_upload=teamMembers_data.date_upload,
            status=teamMembers_data.status
        )
        teamMembers_instance.save()
        return CreateTeamMembers(teamMembers=teamMembers_instance)

# La CreateBookclasse sera utilisée pour créer et enregistrer de nouvelles 
# Bookentrées dans la base de données. Pour chaque classe de mutation, 
# nous devons avoir une Argumentsclasse interne et une mutate()méthode de classe.

# Nous avons défini une instance de la BookInputclasse que nous avons créée précédemment 
# comme nos arguments, et nous l'avons rendue obligatoire avec l' required=Trueoption. Après cela,
#  nous avons défini le modèle avec lequel nous travaillons en faisant ceci book = graphene.Field(BookType).


#procedure update
class UpdateTeamMembers(graphene.Mutation):
    class Arguments:
        teamMembers_data = TeamMembersInput(required=True)

    teamMembers = graphene.Field(TeamMembersType)

    @staticmethod
    def mutate(root, info, teamMembers_data=None):

        teamMembers_instance = TeamMembers.objects.get(pk=teamMembers_data.id)

        if teamMembers_instance:
            teamMembers_instance.fullname = teamMembers_data.title
            teamMembers_instance.author = teamMembers_data.designation
            teamMembers_instance.photo = teamMembers_data.photo
            teamMembers_instance.date_add = teamMembers_data.date_add
            teamMembers_instance.date_update = teamMembers_data.date_update
            teamMembers_instance.status = teamMembers_data.status
            teamMembers_instance.save()

            return UpdateTeamMembers(teamMembers=teamMembers_instance)
        return UpdateTeamMembers(book=None)

#procedure delete
class DeleteTeamMembers(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(TeamMembersType)

    @staticmethod
    def mutate(root, info, id):
        teamMembers_instance = TeamMembers.objects.get(pk=id)
        teamMembers_instance.delete()
        return None


# enregistrement auprès de Graphene
class Mutation(graphene.ObjectType):
    create_teamMembers = CreateTeamMembers.Field()
    update_teamMembers = UpdateTeamMembers.Field()
    delete_teamMembers = DeleteTeamMembers.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


# Django CSRF empêche les utilisateurs non authentifiés sur le site Web d'effectuer des attaques malveillantes.