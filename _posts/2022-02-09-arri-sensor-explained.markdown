---

date: '2022-02-09'
image: /assets/images/posts/arri-sensor-explained-hero.jpg
layout: post
meta_description: From photo sites to ARRIRAW recording, here's how the tech creates
  the ARRI look.
subtitle: From photo sites to ARRIRAW recording, here's how the tech creates the ARRI
  look.
title: Learning the basics of ARRI sensors
---

To understand how ARRIRAW works and what makes it different from other raw formats, it helps to go straight to the source.

In ARRI Academy's official [Certified Online Training for Camera Systems course](https://www.mzed.com/courses/certified-online-training-for-camera-systems), which is only available online at [MZed](https://www.mzed.com), ARRI's senior trainer Florian Rettich distills the complicated subject of raw recording in a way we can all understand.

![ARRI Academy instructor Florian Rettich explaining ARRIRAW](/assets/images/posts/arri-sensor-explained-florian-instructor.jpg)
*Florian Rettich, ARRI's senior trainer, explaining sensor technology. Image source: ARRI*

Even if you're not shooting with ARRI cameras, this lesson is an enlightening dive into camera sensors and photosites, bit depth, data compression, and color. There's a lot to learn and the knowledge will help you grasp the technology inside cameras today.

## ARRIRAW – Photosites, sensors, and analog to digital converters

To better explain ARRIRAW instructor Florian first gives a basic introduction to photosites and how they react to changes in light. You may already know this to some degree, but it's still a good refresher. The way Florian explains the digital imaging process is easy to understand for those of us who aren't already seasoned pixel peepers.

So, all digital cameras have sensors that convert light into an electric charge, which then gets digitized and processed into data. But the way they go about that process differs.

First let's only think about light itself, before we add color to the mix. If you think of photosites on a sensor as buckets of light, then each bucket is white when it is completely full of light, and black when it receives no light. You could also use the analogy of a glass of water if that helps you picture what's happening.

At some point the bucket is full, and the photosite is 100% saturated, or white, disregarding any additional light energy spilling over the bucket. And the same is true when there's no light and the photosite becomes 0% saturated, or black.

![ARRIRAW photosites converting optical to electric to digital signals](/assets/images/posts/arri-sensor-explained-photosite-conversion.jpg)
*The process of converting optical light to digital data through photosites. Image source: ARRI*

Now if you have a 100% full bucket, and you stop the iris down by one stop, the bucket becomes only 50% full. If you stop down the iris an additional stop, the bucket is now 25% full.

The output of the photosite is a little analog charge that needs to be amplified before it gets digitized via an analog to digital (A/D) converter. And at each stop down, the sensor is sending half the amount of analog energy to the digital converter.

## How ARRI gets to 14 stops of dynamic range

So if the camera is looking at a white cloud on a bright sunny day, stopping the lens down a stop from a clipping white cloud would result in a still very white cloud, but with the photosite bucket now at half full.

Florian goes on to show a linear graph where at each stop down of light, the bucket's signal gets dropped in half, and the output or code value is reduced linearly. With a 10-bit signal, there are only 1024 code values, so splitting it in half from 1024 to 512 to 256 and so on would result in only 9 stops of light until you reach 2 code values.

By adding two more bits and using a 12-bit A/D converter, you can now quadruple the code values, from 1024 to 4096, but that still only provides 11 stops of light. (To do the math, just start with the number 2 and multiply it by 2 – you can only do that 11 times before reaching 4096.)

![ARRI 12-bit data values and dynamic range explanation](/assets/images/posts/arri-sensor-explained-12-bit-data.jpg)
*Understanding how 12-bit data values relate to dynamic range. Image source: ARRI*

So how do ARRI cameras maintain [14 stops of dynamic range](https://www.cined.com/arri-alexa-classic-mini-lf-lab-test-rolling-shutter-dynamic-range-and-latitude/)? In a nutshell, they need to start with a 16-bit A/D converter, but when the ALEV sensor was first designed that was difficult to acquire.

As a solution, what the engineers did with the original ARRI ALEV sensor was use two A/D converters, which were then mapped to a 16-bit linear signal. So now we have over 65,000 code values.

This is the foundation of the Dual Gain Architecture (DGA). One of the A/D converters is looking at the highlights of the bucket, and the other at the shadows, with some overlap in the middle.

![ARRI ALEV sensor dual gain architecture achieving 14 stops](/assets/images/posts/arri-sensor-explained-dual-gain-architecture.jpg)
*ARRI's Dual Gain Architecture enables 14 stops of dynamic range. Image source: ARRI*

## How ARRIRAW stays uncompressed

Now that there's a robust digital signal available, how do you take 65,000 code values per frame and fit all of that data onto a media card or drive? How do you reduce the amount of data without compromising the image quality?

There are a few different ways to compress the data into a raw format, and most manufacturers have varying degrees of compression and style to minimize the effect on the image. For example, there's DCT (Discrete Cosine Transform) which works with square blocks of pixels, and there's Wavelet which is processor-heavy but takes a different approach to compress the raw image.

ARRIRAW, on the other hand, is able to record an uncompressed image, while reducing the amount of data, by using a logarithmic allocation of data rather than linear. Florian explains that ARRI looked at their history with film, which is not linear, to figure out how to translate that photometric approach into a digital workflow.

## The advantages of logarithmic encoding

The key insight is that human vision doesn't perceive light linearly. We're much more sensitive to changes in darker areas than in bright areas. Film naturally captured this through its chemical response to light, and ARRI mimicked this characteristic digitally.

By allocating more code values to the shadow areas where we can see the most difference, and fewer code values to the highlights where we're less sensitive to changes, ARRIRAW maximizes the perceptual quality of the image while keeping file sizes manageable.

This logarithmic approach means that:

- **Shadow detail is preserved:** More digital "resolution" is dedicated to the areas where our eyes are most sensitive
- **Highlight rolloff is natural:** The gradual transition to white mimics how film handles overexposure  
- **File sizes remain practical:** No unnecessary data is wasted on imperceptible highlight gradations
- **Post-production flexibility:** The full dynamic range is available for color grading

## Technical specifications of ARRIRAW

ARRIRAW files contain several key technical characteristics:

**Bit depth:** True 16-bit linear data from the dual gain architecture
**Color space:** Native sensor RGB before any color matrix is applied
**Compression:** Uncompressed raw sensor data
**Metadata:** Extensive camera settings and lens data embedded in each frame
**Compatibility:** Supported by major post-production applications

## Workflow considerations

Working with ARRIRAW requires understanding several workflow implications:

**Storage requirements:** Uncompressed files are significantly larger than compressed alternatives
**Processing power:** Raw debayering and color grading require substantial computing resources  
**Color pipeline:** Proper color management from capture through delivery is essential
**Archive strategy:** Long-term storage of large raw files needs careful planning

## Learn more about camera technology with MZed Pro

As an [MZed Pro member](https://www.mzed.com/), you get access to over 500 hours of filmmaking education, including ARRI Academy's official training courses on camera systems and technology.

For just $30/month (billed annually at $349), here's what you'll get:

- 55+ courses, over 850+ high-quality lessons, spanning over 500 hours of learning.
- Highly produced courses from educators who have decades of experience and awards, including a Pulitzer Prize and an Academy Award.
- Unlimited access to stream all content during the 12 months.
- Offline download and viewing with the MZed iOS app.
- Discounts to ARRI Academy online courses, exclusively on MZed.
- Most of our courses provide an industry-recognized certificate upon completion.
- Purchasing the courses outright would cost over $9,500.
- Course topics include cinematography, directing, lighting, cameras and lenses, producing, indie filmmaking, writing, editing, color grading, audio, time-lapse, pitch decks, and more.
- 7-day money-back guarantee if you decide it's not for you.

[**Join MZed Pro now and start watching today!**](https://www.mzed.com/)

Understanding the technology behind ARRIRAW provides insight not just into ARRI cameras, but into the fundamental principles of digital cinematography. The innovations in sensor design, analog-to-digital conversion, and logarithmic encoding that make ARRIRAW possible represent the cutting edge of imaging technology, translated into practical tools for visual storytelling.