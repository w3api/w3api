---
title: ProcessBuilder.startPipeline()
permalink: Java/ProcessBuilder/startPipeline
date: 2021-01-11
key: JavaJava.P.ProcessBuilder
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessBuilder.metodos valor="startPipeline" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static List<Process> startPipeline(List<ProcessBuilder> builders) throws IOException
~~~

## Parámetros
* **List&lt;ProcessBuilder&gt; builders**,  {% include w3api/param_description.html metodo=_dato parametro="List<ProcessBuilder> builders" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ProcessBuilder](/Java/ProcessBuilder/)

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
