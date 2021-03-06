---
title: MidiFileWriter.write()
permalink: /Java/MidiFileWriter/write/
date: 2021-01-11
key: Java.M.MidiFileWriter
category: Java
tags: ['java se', 'javax.sound.midi.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiFileWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int write(Sequence in, int fileType, File out) throws IOException
public abstract int write(Sequence in, int fileType, OutputStream out) throws IOException
~~~

## Parámetros
* **Sequence in**,  {% include w3api/param_description.html metodo=_dato parametro="Sequence in" %}
* **int fileType**,  {% include w3api/param_description.html metodo=_dato parametro="int fileType" %}
* **File out**,  {% include w3api/param_description.html metodo=_dato parametro="File out" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[MidiFileWriter](/Java/MidiFileWriter/)

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
