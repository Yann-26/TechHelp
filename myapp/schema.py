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
    TeamMembers = graphene.Field(TeamMembersType, TeamMembers_id=graphene.Int())

    def resolve_all_TeamMembers(self, info, **kwargs):
        return TeamMembers.objects.all()

    def resolve_TeamMembers(self, info, TeamMembers_id):
        return TeamMembers.objects.get(pk=TeamMembers_id)

class TeamMembersInput(graphene.InputObjectType):
    id =graphene.ID()
    fullname = graphene.String()
    designation = graphene.String()
    photo = Upload(required=False)
    date_add = graphene.String()
    date_update = graphene.String()
    status = graphene.Boolean(default=True)


class CreateTeamMembers(graphene.Mutation):
    class Arguments:
        teamMembers_data = TeamMembersInput(required=True)

    teamMembers = graphene.Field(TeamMembersType)

    @staticmethod
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