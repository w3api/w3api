---
title: MidiMessage
permalink: Java/MidiMessage
date: 2021-01-04
key: JavaJava.M.MidiMessage
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MidiMessage.description }}

## Sintaxis
~~~java
public abstract class MidiMessage extends Object implements Cloneable
~~~

## Constructores
* [MidiMessage()](/Java/MidiMessage/MidiMessage/)

## Campos
* [data](/Java/MidiMessage/data)
* [length](/Java/MidiMessage/length)

## Métodos
* [clone()](/Java/MidiMessage/clone)
* [getLength()](/Java/MidiMessage/getLength)
* [getMessage()](/Java/MidiMessage/getMessage)
* [getStatus()](/Java/MidiMessage/getStatus)
* [setMessage()](/Java/MidiMessage/setMessage)

## Ejemplo
~~~java
{{ site.data.Java.M.MidiMessage.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MidiMessage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
