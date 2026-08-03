-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
local wk = require("which-key")

-- Open remote repo
wk.add({ "<leader>gr", "<cmd>Repo<CR>", desc = "Open Remote" })

-- Open file in explorer
vim.keymap.set("n", "<leader>oe", function()
    local path = vim.fn.expand("%:p:h")
    local cmd = vim.fn.has("win32") == 1 and 'start "" "' .. path .. '"' or
    vim.fn.has("mac") == 1 and 'open "' .. path .. '"' or
    'xdg-open "' .. path .. '"'
    vim.fn.system(cmd)
end, { desc = "Open current file in explorer" })
