---
title: MidiSystem.write()
permalink: Java/MidiSystem/write
date: 2021-01-04
key: JavaJava.M.MidiSystem
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiSystem.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int write(Sequence in, int type, File out) throws IOException
public static int write(Sequence in, int fileType, OutputStream out) throws IOException
~~~

## Parámetros
* **int type**,  {% include w3api/param_description.html metodo=_data parametro="int type" %}
* **File out**,  {% include w3api/param_description.html metodo=_data parametro="File out" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}
* **int fileType**,  {% include w3api/param_description.html metodo=_data parametro="int fileType" %}
* **Sequence in**,  {% include w3api/param_description.html metodo=_data parametro="Sequence in" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

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
