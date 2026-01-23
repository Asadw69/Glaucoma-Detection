'use client';

import Image from 'next/image';

export default function StoryPage() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-[#0a192f] to-[#112240] py-12 px-4">
      <div className="max-w-4xl mx-auto space-y-12">

        {/* Our Story Title */}
        <div className="text-center">
          <h1 className="text-4xl font-bold text-white mb-2">Our Story</h1>
          <p className="text-blue-300 text-lg">Built from Experience. Designed for Impact.</p>
        </div>

        {/* About the Team Section */}
        <section className="bg-[#1a2942] p-8 rounded-xl">
          <h2 className="text-2xl font-semibold text-white mb-6">About the Team</h2>
          <div className="text-gray-300 text-lg space-y-4">
            <p>
              This project was developed by Asad Siddiqui, Mohd Sameer, and Mohd Akib (Batch 2022–2026, GEU) during the final year of our B.Tech program.
            </p>
            <p>
              While exploring real-world healthcare challenges, we identified early-stage glaucoma detection as a critical problem where timely intervention can significantly reduce the risk of vision loss. Motivated by this, we set out to design and implement an effective approach using technology to support early diagnosis.
            </p>
            <p>
              Over the course of our final year, we researched existing methods, experimented with different techniques, and iteratively improved our solution to achieve better accuracy and reliability. This project reflects our combined efforts, teamwork, and commitment to applying engineering knowledge to meaningful medical problems.
            </p>
          </div>
        </section>
      </div>
    </main>
  );
}
