import { defineConfig } from "vitepress";

export default defineConfig({
  title: "HMG Release Workflows",
  description: "Reusable GitHub Actions workflows, templates, and scripts for Minecraft releases",
  themeConfig: {
    sidebar: [
      {
        text: "Documentation",
        items: [
          { text: "Overview", link: "/" },
          { text: "Setup", link: "/setup" },
          { text: "Naming", link: "/naming" },
          { text: "Secrets", link: "/secrets" },
          { text: "Platform Publishing", link: "/platform-publishing" },
          { text: "Contributing and Maintenance", link: "/contributing" },
          { text: "Migration", link: "/migration" },
          { text: "Troubleshooting", link: "/troubleshooting" },
        ],
      },
    ],

    search: {
      provider: "local",
    },

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/HMLabs-Gaming/release-workflows",
      },
    ],
  },
});
