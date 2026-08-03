# Enable Powerlevel10k instant prompt.
# Keep this near the top of ~/.zshrc.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# completion
autoload -Uz compinit
compinit

# history
HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000

export PATH="$HOME/bin:$HOME/.local/bin:$PATH"

# things
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

# Powerlevel10k
[[ -f ~/.p10k.zsh ]] && source ~/.p10k.zsh
