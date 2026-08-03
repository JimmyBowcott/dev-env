return {
  {
    "vague2k/vague.nvim",
    lazy = false,
    priority = 1000,
    config = function()
      require("vague").setup({
        -- Add any optional settings here
      })
      vim.cmd.colorscheme("vague")
    end,
  },
}