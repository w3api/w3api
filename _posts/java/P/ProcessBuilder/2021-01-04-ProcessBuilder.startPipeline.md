---
title: ProcessBuilder.startPipeline()
permalink: Java/ProcessBuilder/startPipeline
date: 2021-01-04
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
* **List&lt;ProcessBuilder&gt; builders**,  {% include w3api/param_description.html metodo=_data parametro="List<ProcessBuilder> builders" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[ProcessBuilder](/Java/ProcessBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProcessBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
