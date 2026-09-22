import type { Metadata } from "next";
import { Geist, Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Sprinto AI Hub - Product Management OS",
  description: "Convierte ideas en decisiones de producto. Plataforma asistida por IA para priorizar iniciativas y estructurar requerimientos.",
  openGraph: {
    title: "Sprinto AI Hub - Product Management OS",
    description: "Una plataforma asistida por IA para descubrir oportunidades reales, estructurar casos de uso con contexto y priorizar con rigor técnico.",
    type: "website",
  }
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
      </head>
      <body className={`${geistSans.variable} ${inter.variable} ${jetbrainsMono.variable} bg-surface-canvas text-text-primary font-body-md antialiased`}>
        {children}
      </body>
    </html>
  );
}
