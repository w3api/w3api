---
title: MidiSystem.getMidiDevice()
permalink: /Java/MidiSystem/getMidiDevice/
date: 2021-01-11
key: Java.M.MidiSystem
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiSystem.metodos valor="getMidiDevice" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MidiDevice getMidiDevice(MidiDevice.Info info) throws MidiUnavailableException
~~~

## Parámetros
* **MidiDevice.Info info**,  {% include w3api/param_description.html metodo=_dato parametro="MidiDevice.Info info" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [MidiUnavailableException](/Java/MidiUnavailableException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MidiSystem](/Java/MidiSystem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
