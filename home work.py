#on doit d'abord specifie les taches demandes dans cet exercice :
#1. Chaque client peut avoir plusieurs comptes
#2. Chaque compte est automatiquement ajouté au client
#3. Ajout d’un historique des transactions
#4. Validation des montants
#5. Gestion des transferts
#donc: -Tâche 1 : Historique des transactions (self.transactions, append(), display_transactions())
      #-Tâche 2 : Validation des montants positifs et solde suffisant
      #-Tâche 3 : Plusieurs comptes par client (self.accounts, add_account(), display_accounts())


# LA CLASSE CLIENT
class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.cin = cin
        self.firstName = firstName
        self.lastName = lastName
        self.tel = tel
        # Tâche 3: liste des comptes pour permettre à un client d'avoir plusieurs comptes
        self.accounts = []  # liste des comptes du client

    # Ajouter un compte à ce client
    def add_account(self, account):
        self.accounts.append(account)  # Tâche 3: ajout automatique du compte

    # Afficher tous les comptes du client
    def display_accounts(self):
        print(f"\nComptes de {self.firstName} {self.lastName}:")
        if not self.accounts:
            print("Aucun compte.")
        else:
            for acc in self.accounts:
                print(f"- Compte {acc.code} : {acc.balance} DA")  # Tâche 3: afficher tous les comptes

    # Afficher les infos du client
    def display(self):
        print(f"CIN: {self.cin}, Name: {self.firstName} {self.lastName}, Tel: {self.tel}")


#LA CLASSE ACCOUNT
class Account:
    total_accounts = 0  # variable statique pour le code unique

    def __init__(self, owner):  # owner c'est le client qui a maintenant un compte
        Account.total_accounts += 1
        self.code = Account.total_accounts   # un code unique pour chaque compte
        self.balance = 0                     # le solde du compte est initialisé à 0
        self.owner = owner

        # Tâche 1: historique des transactions
        self.transactions = []

        # Tâche 3: ajouter automatiquement ce compte à la liste des comptes du client
        owner.add_account(self)

    # Crediter le compte
    def credit(self, amount, other_account=None):  # ajouter de l'argent
        # Tâche 2: validation des montants positifs
        if amount <= 0:
            print("Erreur : le montant doit être positif.")
            return

        if other_account is None:  # ajouter de l'argent au solde
            self.balance += amount
            # Tâche 1: enregistrer dans l'historique
            self.transactions.append(f"Credit: +{amount}")
        else:  # retirer de l'argent du compte2 et le mettre dans le compte 1 (exp)
            self.balance += amount
            other_account.debit(amount)
            #Tâche 1: enregistrer le transfert dans l'historique
            self.transactions.append(f"Received transfer: +{amount} from Account {other_account.code}")

    # Débiter le compte
    def debit(self, amount, other_account=None):  # pour retirer de l'argent
        # Tâche 2: validation des montants positifs
        if amount <= 0:
            print("Erreur : le montant doit être positif.")
            return

        if self.balance >= amount:  # il faut avoir le solde > le montant que je vais retirer
            self.balance -= amount
            #Tâche 1: enregistrer le retrait dans l'historique
            self.transactions.append(f"Debit: -{amount}")

            if other_account:  # retirer de l'argent du compte 1 et le mettre dans le compte 2 (exp)
                other_account.credit(amount)
                #Tâche 1: enregistrer le transfert dans l'historique
                self.transactions.append(f"Transfer to Account {other_account.code}: -{amount}")
        else:
            print("Solde insuffisant.")  # si le solde n'est pas suffisant pour retirer le montant

    # Afficher les infos du compte
    def display(self):
        print(f"\nCompte {self.code}")
        print(f"Propriétaire: {self.owner.firstName} {self.owner.lastName}")  # afficher le client qui a un compte
        print(f"Solde: {self.balance} DA")

    #Tâche 1: afficher l'historique des transactions
    def display_transactions(self):
        print(f"\nHistorique du Compte {self.code}:")
        if not self.transactions:
            print("Aucune transaction.")
        else:
            for t in self.transactions:
                print("- " + t)

    # Afficher le nombre total de comptes
    @staticmethod
    def display_total_accounts():
        print("Total des comptes créés:", Account.total_accounts)  # afficher le nombre total de comptes créés


#APPLICATION SUR LE PROGRAMME:

# Création des clients
client1 = Client("1234", "Serine", "Teghri", "0550 00 00 00")
client2 = Client("5678", "Aya", "Bensalem", "0661 22 33 44")

# Création de plusieurs comptes par client
acc1 = Account(client1)   # Compte 1 de Serine
acc2 = Account(client1)   # Compte 2 de Serine
acc3 = Account(client2)   # Compte 1 de Aya

print("\t")
# Affichage des comptes appartenant a chaque client
client1.display_accounts()
client2.display_accounts()

print("\t")
# Operations sur acc1
acc1.credit(5000)        # Depot
acc1.debit(1500)         # Retrait

print("\t")
# Transfert de acc1 -> acc2
acc1.debit(1000, acc2)

print("\t")
# Transfert de acc3 -> acc1
acc3.credit(2000, acc1)

print("\t")
# Affichage des comptes
acc1.display()
acc2.display()
acc3.display()

print("\t")
# Historique des transactions
acc1.display_transactions()
acc2.display_transactions()
acc3.display_transactions()


print("\t")
# Nombre total de comptes crees
Account.display_total_accounts()