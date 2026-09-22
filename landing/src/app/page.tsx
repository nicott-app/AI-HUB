import Navbar from '@/components/layout/Navbar';
import Footer from '@/components/layout/Footer';
import Hero from '@/components/sections/Hero';
import SocialProof from '@/components/sections/SocialProof';
import ProblemStatement from '@/components/sections/ProblemStatement';
import ValuePillars from '@/components/sections/ValuePillars';
import AiPipeline from '@/components/sections/AiPipeline';
import PrioritizationMatrix from '@/components/sections/PrioritizationMatrix';
import ProductHealth from '@/components/sections/ProductHealth';
import Architecture from '@/components/sections/Architecture';
import Differentiation from '@/components/sections/Differentiation';
import FinalCta from '@/components/sections/FinalCta';

export default function Home() {
  return (
    <>
      <Navbar />
      <main className="w-full pt-16 bg-surface-canvas flex-grow">
        <div className="flex flex-col w-full">
          <Hero />
          <SocialProof />
          <ProblemStatement />
          <ValuePillars />
          <AiPipeline />
          <PrioritizationMatrix />
          <ProductHealth />
          <Architecture />
          <Differentiation />
          <FinalCta />
        </div>
      </main>
      <Footer />
    </>
  );
}
