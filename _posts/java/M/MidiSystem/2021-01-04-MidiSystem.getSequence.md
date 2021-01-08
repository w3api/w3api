---
title: MidiSystem.getSequence()
permalink: Java/MidiSystem/getSequence
date: 2021-01-04
key: JavaJava.M.MidiSystem
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiSystem.metodos valor="getSequence" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Sequence getSequence(File file) throws InvalidMidiDataException, IOException
public static Sequence getSequence(InputStream stream) throws InvalidMidiDataException, IOException
public static Sequence getSequence(URL url) throws InvalidMidiDataException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/), [InvalidMidiDataException](/Java/InvalidMidiDataException/)

## Clase Padre
[MidiSystem](/Java/MidiSystem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MidiSystem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
