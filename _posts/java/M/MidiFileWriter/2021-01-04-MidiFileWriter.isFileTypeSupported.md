---
title: MidiFileWriter.isFileTypeSupported()
permalink: Java/MidiFileWriter/isFileTypeSupported
date: 2021-01-04
key: JavaJava.M.MidiFileWriter
category: java
tags: ['java se', 'javax.sound.midi.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiFileWriter.metodos valor="isFileTypeSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isFileTypeSupported(int fileType)
public boolean isFileTypeSupported(int fileType, Sequence sequence)
~~~

## Parámetros
* **int fileType**,  {% include w3api/param_description.html metodo=_data parametro="int fileType" %}
* **Sequence sequence**,  {% include w3api/param_description.html metodo=_data parametro="Sequence sequence" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MidiFileWriter](/Java/MidiFileWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MidiFileWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
