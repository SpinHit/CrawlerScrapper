/*************************************************************/
/******************PROJET CORPUS MASTER BIG DATA**************/
/*************************************************************/
/*************************************************************/

#include "corpus.h"

int main(int argc, char *argv[])
{
  int choix;
  printf("\n      *|       Cr�ation corpus HTML        |*\n                ________________________\n");

  while (1)
  {
    switch (choix = menu())
    {
    case 1:
    {
      printf("\n*****************************************\n R�alisation du corpus \n*****************************************\n\n");
      char fichier_dictionnaire[150] = "./dictionnaires/lexique_corpus_sans_doublons.txt";
      char rep_fin[150] = "./fichiers/corpus/";

      // if(confirmer()==1)
      {

        faire_corpus(fichier_dictionnaire, rep_fin);
      }
      break;
    }
    case 0:
    {
      return 0; 
    }

    default:
    {
      puts("choix incorrect");
    }
    }
  }

  return 0;
}

/*************************************************************/
/*MENU*/
/*************************************************************/
int menu(void)
{
  int reponse;
  printf("\n\n\n*****************************************\n CHOIX FONCTIONALITES\n*****************************************\n\n");
  puts(" 1 Realisation corpus  -> OK");
  puts(" 0 Quitter le programme");
  printf("\n Choix : ");
  scanf("%d", &reponse);
  printf("\n");

  return reponse;
}
