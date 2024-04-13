---
title: MidiSystem.getMidiFileTypes()
permalink: /Java/MidiSystem/getMidiFileTypes/
date: 2021-01-11
key: Java.M.MidiSystem
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiSystem.metodos valor="getMidiFileTypes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int[] getMidiFileTypes()
public static int[] getMidiFileTypes(Sequence sequence)
~~~

## Parámetros
* **Sequence sequence**,  {% include w3api/param_description.html metodo=_dato parametro="Sequence sequence" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
