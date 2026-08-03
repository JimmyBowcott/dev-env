-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

-- ~~~~~~~~~~~~~~~ Visuals ~~~~~~~~~~~~~~~~~
vim.g.snacks_animate = false

-- ~~~~~~~~~~~~~~~ Utility ~~~~~~~~~~~~~~~~~
vim.api.nvim_set_keymap('n', '<leader>h', ':Dashboard<CR>', { noremap = true, silent = true })
vim.keymap.set("n", "<leader>yf", ":let @+ = expand('%:p')<CR>", { desc = "Yank Filepath" })


-- ~~~~~~~~~~~~~~~ Editing ~~~~~~~~~~~~~~~~~
vim.g.autoformat = false
vim.opt.clipboard = "unnamedplus"

vim.api.nvim_create_user_command("Fmt", function()
  vim.diagnostic.setloclist({ open = false })
  vim.lsp.buf.format({ async = true })
end, { desc = "Format file" })

vim.opt.expandtab = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.softtabstop = 4

vim.api.nvim_set_keymap('n', '<leader>fa', ':Fmt<CR>', { noremap = true, silent = true })

-- ~~~~~~~~~~~~~~~~ Git ~~~~~~~~~~~~~~~~~~~~

-- Open the remote repo with <leader>gr
vim.api.nvim_create_user_command("Repo", function()
  local handle = io.popen("git remote get-url origin")
  if handle then
    local url = handle:read("*a"):gsub("%s+$", "")
    handle:close()

    if url == "" then
      print("No remote URL found")
      return
    end

    url = url:gsub("^git@([^:]+):(.+)$", "https://%1/%2"):gsub("%.git$", "")

    local open_cmd = vim.fn.has("win32") == 1 and "start" or "xdg-open"
    os.execute(open_cmd .. " " .. url)
  end
end, { desc = "Open remote repository" })
