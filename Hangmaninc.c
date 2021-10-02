/****************************************************
Write a simple version of hangman, in which the user
enters the word he'll "guess", and then the user gets
to start guessing letters. After each guess, the word
is printed out with *s instead of unguessed letters.
 ****************************************************/
#include <stdio.h>
#include <string.h>

int main() {
  // Get word to guess
  char answer[128];
  printf("Enter word to guess: ");
  fflush(stdout);
  scanf(" %s", answer);

  // Set the mask array - mask[i] is true if the
  // character s[i] has been guessed.  The mask
  // must be allocated, and initialized to all false
  int N = strlen(answer);
  int mask[N];
  for (int i=0; i < N; ++i) {
    mask[i] = 0;
  }

  // Loop over each round of guessing
  int gameover = 0;
  while (! gameover) {
    // Print word with *s for unguessed letters
    printf("The word is : ");
    for(int j=0; j < N; ++j) {
      if (mask[j]) {
        printf("%c", answer[j]);
      }
      else {
        printf("*");
      }
    }
    printf("\n");

    // Get player's next guess
    char guess;
    printf("Letter? ");
    fflush(stdout);
    scanf(" %c", &guess);

    // Mark true all mask positions corresponding to guess
    for(int k=0; k < N; ++k) {
      if (answer[k] == guess) {
	mask[k] = 1;
      }
    }

    // Determine whether the player has won!
    gameover = 1;
    for(int m = 0; m < N; ++m) {
      if (!mask[m]) {
        gameover = 0;
        break;
      }
    }
  }

  // Print victory message!
  printf("Victory! The word is \"%s\".\n", answer);

  return 0;
}
