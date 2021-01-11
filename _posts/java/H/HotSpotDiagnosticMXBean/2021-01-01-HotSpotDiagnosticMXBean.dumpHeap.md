---
title: HotSpotDiagnosticMXBean.dumpHeap()
permalink: Java/HotSpotDiagnosticMXBean/dumpHeap
date: 2021-01-11
key: JavaJava.H.HotSpotDiagnosticMXBean
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HotSpotDiagnosticMXBean.metodos valor="dumpHeap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void dumpHeap(String outputFile, boolean live) throws IOException
~~~

## Parámetros
* **String outputFile**,  {% include w3api/param_description.html metodo=_dato parametro="String outputFile" %}
* **boolean live**,  {% include w3api/param_description.html metodo=_dato parametro="boolean live" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HotSpotDiagnosticMXBean](/Java/HotSpotDiagnosticMXBean/)

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
