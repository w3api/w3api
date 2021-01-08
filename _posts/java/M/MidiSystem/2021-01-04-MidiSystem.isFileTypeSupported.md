---
title: MidiSystem.isFileTypeSupported()
permalink: Java/MidiSystem/isFileTypeSupported
date: 2021-01-04
key: JavaJava.M.MidiSystem
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiSystem.metodos valor="isFileTypeSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isFileTypeSupported(int fileType)
public static boolean isFileTypeSupported(int fileType, Sequence sequence)
~~~

## Parámetros
* **int fileType**,  {% include w3api/param_description.html metodo=_data parametro="int fileType" %}
* **Sequence sequence**,  {% include w3api/param_description.html metodo=_data parametro="Sequence sequence" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
