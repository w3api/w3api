---
title: MidiFileReader.getMidiFileFormat()
permalink: Java/MidiFileReader/getMidiFileFormat
date: 2021-01-04
key: JavaJava.M.MidiFileReader
category: java
tags: ['java se', 'javax.sound.midi.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiFileReader.metodos valor="getMidiFileFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract MidiFileFormat getMidiFileFormat(File file) throws InvalidMidiDataException, IOException
public abstract MidiFileFormat getMidiFileFormat(InputStream stream) throws InvalidMidiDataException, IOException
public abstract MidiFileFormat getMidiFileFormat(URL url) throws InvalidMidiDataException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/), [InvalidMidiDataException](/Java/InvalidMidiDataException/)

## Clase Padre
[MidiFileReader](/Java/MidiFileReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MidiFileReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
