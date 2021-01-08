---
title: MidiFileWriter.getMidiFileTypes()
permalink: Java/MidiFileWriter/getMidiFileTypes
date: 2021-01-04
key: JavaJava.M.MidiFileWriter
category: java
tags: ['java se', 'javax.sound.midi.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiFileWriter.metodos valor="getMidiFileTypes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int[] getMidiFileTypes()
public abstract int[] getMidiFileTypes(Sequence sequence)
~~~

## Parámetros
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
