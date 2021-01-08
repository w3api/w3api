---
title: HotSpotDiagnosticMXBean.dumpHeap()
permalink: Java/HotSpotDiagnosticMXBean/dumpHeap
date: 2021-01-04
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
* **boolean live**,  {% include w3api/param_description.html metodo=_data parametro="boolean live" %}
* **String outputFile**,  {% include w3api/param_description.html metodo=_data parametro="String outputFile" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[HotSpotDiagnosticMXBean](/Java/HotSpotDiagnosticMXBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HotSpotDiagnosticMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
