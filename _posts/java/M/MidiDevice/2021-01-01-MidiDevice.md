---
title: MidiDevice
permalink: Java/MidiDevice
date: 2021-01-11
key: JavaJava.M.MidiDevice
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MidiDevice.description }}

## Sintaxis
~~~java
public interface MidiDevice extends AutoCloseable
~~~

## Métodos
* [close()](/Java/MidiDevice/close)
* [getDeviceInfo()](/Java/MidiDevice/getDeviceInfo)
* [getMaxReceivers()](/Java/MidiDevice/getMaxReceivers)
* [getMaxTransmitters()](/Java/MidiDevice/getMaxTransmitters)
* [getMicrosecondPosition()](/Java/MidiDevice/getMicrosecondPosition)
* [getReceiver()](/Java/MidiDevice/getReceiver)
* [getReceivers()](/Java/MidiDevice/getReceivers)
* [getTransmitter()](/Java/MidiDevice/getTransmitter)
* [getTransmitters()](/Java/MidiDevice/getTransmitters)
* [isOpen()](/Java/MidiDevice/isOpen)
* [open()](/Java/MidiDevice/open)

## Ejemplo
~~~java
{{ site.data.Java.M.MidiDevice.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MidiDevice.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
