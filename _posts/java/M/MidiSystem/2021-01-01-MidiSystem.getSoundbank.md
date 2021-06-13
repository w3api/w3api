---
title: MidiSystem.getSoundbank()
permalink: Java/MidiSystem/getSoundbank
date: 2021-01-11
key: JavaJava.M.MidiSystem
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiSystem.metodos valor="getSoundbank" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Soundbank getSoundbank(File file) throws InvalidMidiDataException, IOException
public static Soundbank getSoundbank(InputStream stream) throws InvalidMidiDataException, IOException
public static Soundbank getSoundbank(URL url) throws InvalidMidiDataException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [InvalidMidiDataException](/Java/InvalidMidiDataException/), [IOException](/Java/IOException/)

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
