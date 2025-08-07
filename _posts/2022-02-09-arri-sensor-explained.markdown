---
title: Learning the basics of ARRI sensors
date: 2022-02-09 00:00:00 Z
image: "/assets/images/posts/arri-sensor-explained-hero.jpg"
layout: post
meta_description: From photo sites to ARRIRAW recording, here's how the tech creates
  the ARRI look.
subtitle: From photo sites to ARRIRAW recording, here's how the tech creates the ARRI
  look.
---

![An Introduction to ARRIRAW](/assets/images/posts/arri-sensor-explained-hero.jpg)

**To understand how ARRIRAW works and what makes it different from other raw formats, it helps to go straight to the source.**

**MZed Pro 1-Year Filmmaking Courses Subscription**

In ARRI Academy's official [Certified Online Training for Camera Systems course](https://www.mzed.com/courses/certified-online-training-for-camera-systems?tap_a=17272-420962&tap_s=2527515-4eb418), which is only available online at [MZed](https://www.mzed.com/?tap_a=17272-420962&tap_s=2527515-4eb418), ARRI's senior trainer Florian Rettich distills the complicated subject of raw recording in a way we can all understand.

Even if you're not shooting with ARRI cameras, this lesson is an enlightening dive into camera sensors and photosites, bit depth, data compression, and color. There's a lot to learn and the knowledge will help you grasp the technology inside cameras today.

## ARRIRAW – Photosites, sensors, and analog to digital converters

To better explain ARRIRAW instructor Florian first gives a basic introduction to photosites and how they react to changes in light. You may already know this to some degree, but it's still a good refresher. The way Florian explains the digital imaging process is easy to understand for those of us who aren't already seasoned pixel peepers.

So, all digital cameras have sensors that convert light into an electric charge, which then gets digitized and processed into data. But the way they go about that process differs.

[![](/assets/images/posts/arri-academy-florian-instructor.jpg)](/assets/images/posts/arri-academy-florian-instructor.jpg)

Image source: ARRI

First let's only think about light itself, before we add color to the mix. If you think of photosites on a sensor as buckets of light, then each bucket is white when it is completely full of light, and black when it receives no light. You could also use the analogy of a glass of water if that helps you picture what's happening.

At some point the bucket is full, and the photosite is 100% saturated, or white, disregarding any additional light energy spilling over the bucket. And the same is true when there's no light and the photosite becomes 0% saturated, or black.

[![arriraw-photosites-optical-electric-digital-conversion](/assets/images/posts/arriraw-photosites-conversion.jpg)](/assets/images/posts/arriraw-photosites-conversion.jpg)

Image source: ARRI

Now if you have a 100% full bucket, and you stop the iris down by one stop, the bucket becomes only 50% full. If you stop down the iris an additional stop, the bucket is now 25% full. 

The output of the photosite is a little analog charge that needs to be amplified before it gets digitized via an analog to digital (A/D) converter. And at each stop down, the sensor is sending half the amount of analog energy to the digital converter.

## How ARRI gets to 14 stops of dynamic range

So if the camera is looking at a white cloud on a bright sunny day, stopping the lens down a stop from a clipping white cloud would result in a still very white cloud, but with the photosite bucket now at half full. 

Florian goes on to show a linear graph where at each stop down of light, the bucket's signal gets dropped in half, and the output or code value is reduced linearly. With a 10-bit signal, there are only 1024 code values, so splitting it in half from 1024 to 512 to 256 and so on would result in only 9 stops of light until you reach 2 code values. 

By adding two more bits and using a 12-bit A/D converter, you can now quadruple the code values, from 1024 to 4096, but that still only provides 11 stops of light. (To do the math, just start with the number 2 and multiply it by 2 – you can only do that 11 times before reaching 4096.)

[![arri-raw-12-bit-data-values](/assets/images/posts/arri-raw-12-bit-data-values.jpg)](/assets/images/posts/arri-raw-12-bit-data-values.jpg)

Image source: ARRI

So how do ARRI cameras maintain [14 stops of dynamic range](https://www.cined.com/arri-alexa-classic-mini-lf-lab-test-rolling-shutter-dynamic-range-and-latitude/)? In a nutshell, they need to start with a 16-bit A/D converter, but when the ALEV sensor was first designed that was difficult to acquire.

As a solution, what the engineers did with the original ARRI ALEV sensor was use two A/D converters, which were then mapped to a 16-bit linear signal. So now we have over 65,000 code values. 

This is the foundation of the Dual Gain Architecture (DGA). One of the A/D converters is looking at the highlights of the bucket, and the other at the shadows, with some overlap in the middle. 

[![arri-arriraw-alev-sensor-14-bit-dual-gain](/assets/images/posts/arri-alev-sensor-dual-gain.jpg)](/assets/images/posts/arri-alev-sensor-dual-gain.jpg)

Image source: ARRI

## How ARRIRAW stays uncompressed

Now that there's a robust digital signal available, how do you take 65,000 code values per frame and fit all of that data onto a media card or drive? How do you reduce the amount of data without compromising the image quality?

There are a few different ways to compress the data into a raw format, and most manufacturers have varying degrees of compression and style to minimize the effect on the image. For example, there's DCT (Discrete Cosine Transform) which works with square blocks of pixels, and there's Wavelet which is processor-heavy but takes a different approach to compress the raw image. 

ARRIRAW, on the other hand, is able to record an uncompressed image, while reducing the amount of data, by using a logarithmic allocation of data rather than linear. Florian explains that ARRI looked at their history with film, which is not linear, to figure out how to translate that photometric approach into a digital output.

[![arriraw-uncompressed-16-bit](/assets/images/posts/arriraw-uncompressed-16-bit.jpg)](/assets/images/posts/arriraw-uncompressed-16-bit.jpg)

Image source: ARRI

So with 65,000 code values available in a 16-bit signal, a linear process would allocate one stop of light to half of all the code values – essentially over 32,500 code values for the difference between two shades of white on a white cloud. ARRIRAW, on the other hand, gives each stop of light an equal amount of code values.

So the highlights aren't treated differently than the shadows. Each stop receives the same amount of code values, which makes the raw file more efficient at reducing data. And it's what enables ARRIRAW to save a raw image to media cards and drives, which all have limited data rates, without using compression.

## Adding color with the Bayer mosaic pattern

At this stage of the raw recording process with ARRIRAW, you're still only dealing with the monochromatic image, with photosites collecting light and converting each photosite into one pixel of data. In fact, ARRI does have a rental camera that only records Black & White: the ALEXA XT B&W. [Here is an example](https://arri.academy/Audi-X-Factor-Shoot-MZed) from a commercial that used this camera without an infrared filter for a cool effect.

<iframe loading="lazy" title="Audi X Factor Shoot" src="https://player.vimeo.com/video/66114200?dnt=1&amp;app_id=122963" width="500" height="281" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" data-rocket-lazyload="fitvidscompatible" data-lazy-src="https://player.vimeo.com/video/66114200?dnt=1&amp;app_id=122963" data-ll-status="loaded"></iframe>

With only one sensor, how can you create three colors? While some cameras utilize three sensors – one each for blue, green, and red – in this case, we only have one sensor, but we're using a Bayer filter on top of each photosite. (It's worth learning more about [Bryce Bayer](https://en.wikipedia.org/wiki/Bryce_Bayer) who designed the pattern while working at Kodak.)

What's interesting to note is that the filter assigns two greens per one red and blue, so on a 4k sensor with 4096 photosites, there are approximately 2,048 greens and 1,024 red and 1,024 blue. That's partly because green is a lot more sensitive than red and blue, so with twice as many green photosites on a sensor, there is more luminance which makes the sensor more light-sensitive.  

[![bayer-pattern-mosaic-sensor-filter](/assets/images/posts/bayer-pattern-mosaic-filter.jpg)](/assets/images/posts/bayer-pattern-mosaic-filter.jpg)

Image source: Wikipedia

The camera knows which photosite has which color filter assigned to it, and in real-time up to 200 times per second, the camera uses a de-mosaic or de-bayering press to produce a color image that you see on your viewfinder. 

But if you have only 4096 photosites, each with only 1 of the 4 Bayer color filters on top, wouldn't that result in a 1024 pixel color image? Well no, each camera manufacturer has their own algorithm that improves the de-bayering process. 

At this point you could take that debayered video signal and process and save it to your media, using whatever your camera has available in codec, data rate, color information, and so on. With a raw file, however, you're recording the monochromatic video, and all the color, exposure, and contrast info are simply metadata. You apply the Debayering process in post, rather than in-camera.

[![arriraw-debayer-color-rgb-image](/assets/images/posts/arriraw-debayer-color-rgb.jpg)](/assets/images/posts/arriraw-debayer-color-rgb.jpg)

Image source: ARRI

Of course, the main benefit to this is that you can make changes to white balance, ISO, and contrast in post without any impact on the image quality. Another benefit to shooting raw in general is being able to archive media and apply a different or more modern DeBayering algorithm down the road.

But we won't get into the debate between using raw and contemporary high-quality recording formats. I hope this was a good introduction or refresher to raw recording, specifically ARRIRAW. 

## Get certified with ARRI Academy

There's a wealth of knowledge with ARRI Academy training, and they're an amazing resource whether you are currently using ARRI products or you would like to learn how to use them with future creative work. At MZed, you can take the following ARRI Academy courses online:

-   [Certified Online Training for Camera Systems](https://www.mzed.com/courses/certified-online-training-for-camera-systems?tap_a=17272-420962&tap_s=2527515-4eb418)
-   [Certified Online Training for Large-Format Camera Systems](https://www.mzed.com/courses/certified-online-training-for-large-format-camera-system?tap_a=17272-420962&tap_s=2527515-4eb418)
-   [ARRI Lighting Systems Control](https://www.mzed.com/courses/arri-lighting-systems-control?tap_a=17272-420962&tap_s=2527515-4eb418)
-   [Large Format Cinematography with James Laxton ASC](https://www.mzed.com/courses/large-format-cinematography-with-james-laxton-asc?tap_a=17272-420962&tap_s=2527515-4eb418)
-   [ARRI Christmas Master Class with Julio Macat ASC](https://www.mzed.com/courses/arri-christmas-master-class-with-julio-macat-asc?tap_a=17272-420962&tap_s=2527515-4eb418)

[![ARRI-Master-class-MZed](/assets/images/posts/arri-master-class-mzed.jpg)](/assets/images/posts/arri-master-class-mzed.jpg)

> "Technology is evolving faster than ever. Such an in depth course is a strong foundation or a big boost to anyone's career in the field of cinematography affecting both technical & creative choices. Not everyone can go for such guided training practically on location especially in covid times, so an online course like this, feels like a blessing. Thanks for making this course ARRI. And thanks MZed."
> 
> Rishabh G.

As an [MZed Pro](https://www.mzed.com/?tap_a=17272-420962&tap_s=2527515-4eb418) member, you get access to ARRI Academy courses as well as everything else on the platform, plus we're constantly adding more courses. For just $30/month (billed annually at $349), here's everything you'll get:

-   42 courses, over 500 high quality lessons spanning over 275 hours of learning.
-   Highly produced courses from educators who have decades of experience and awards, including a Pulitzer Prize and an Academy Award.
-   Exclusive access to ARRI Academy online courses.
-   Unlimited access to stream all the content during the 12 months.
-   Offline download and viewing with the MZed iOS app.
-   The majority of MZed courses provide an industry-recognized certificate upon completion.
-   Purchasing the courses outright would cost over $9,800.
-   Course topics include cinematography, directing, lighting, cameras and lenses, producing, indie filmmaking, writing, editing, color grading, audio, and even how to launch a YouTube channel.
-   7-day money back guarantee if you decide it's not for you.

[![MZed courses](/assets/images/posts/mzed-all-courses-arri-sensor.jpg)](https://www.mzed.com/checkout/?sku=MZEDPRO12&tap_a=17272-420962&tap_s=2490653-f2e424)

**[Join MZed Pro now to get started](https://www.mzed.com/checkout/?sku=MZEDPRO12&tap_a=17272-420962&tap_s=2527515-4eb418)**!

Full disclosure: MZed is [owned by CineD](https://www.cined.com/cined-acquires-mzed/)

**Do you have any questions about ARRIRAW? Let us know in the comments below and the CineD community will do its best to help!**