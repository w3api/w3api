---
title: Synthesizer
permalink: /Java/Synthesizer/
date: 2021-01-11
key: Java.S.Synthesizer
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.Synthesizer.description }}

## Sintaxis
~~~java
public interface Synthesizer extends MidiDevice
~~~

## Métodos
* [getAvailableInstruments()](/Java/Synthesizer/getAvailableInstruments)
* [getChannels()](/Java/Synthesizer/getChannels)
* [getDefaultSoundbank()](/Java/Synthesizer/getDefaultSoundbank)
* [getLatency()](/Java/Synthesizer/getLatency)
* [getLoadedInstruments()](/Java/Synthesizer/getLoadedInstruments)
* [getMaxPolyphony()](/Java/Synthesizer/getMaxPolyphony)
* [getVoiceStatus()](/Java/Synthesizer/getVoiceStatus)
* [isSoundbankSupported()](/Java/Synthesizer/isSoundbankSupported)
* [loadAllInstruments()](/Java/Synthesizer/loadAllInstruments)
* [loadInstrument()](/Java/Synthesizer/loadInstrument)
* [loadInstruments()](/Java/Synthesizer/loadInstruments)
* [remapInstrument()](/Java/Synthesizer/remapInstrument)
* [unloadAllInstruments()](/Java/Synthesizer/unloadAllInstruments)
* [unloadInstrument()](/Java/Synthesizer/unloadInstrument)
* [unloadInstruments()](/Java/Synthesizer/unloadInstruments)

## Ejemplo
~~~java
{{ site.data.Java.S.Synthesizer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Synthesizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
