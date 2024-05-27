import { Noto_Sans_Thai } from 'next/font/google';

export const siteConfig = {
  title: 'Next.js + Tailwind CSS + Excalidraw + mdx',
  description: 'Quikwise is a team workspace where knowledge and collaboration meet.',
  url: 'https://quikwise.dev',
};

export const defaultFont = Noto_Sans_Thai({
  weight: ['100', '200', '300', '400', '500', '600', '700', '800', '900'],
  subsets: ['thai'],
  display: 'swap',
  variable: '--default-font',
});
