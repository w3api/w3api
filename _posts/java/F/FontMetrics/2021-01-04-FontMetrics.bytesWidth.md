---
title: FontMetrics.bytesWidth()
permalink: Java/FontMetrics/bytesWidth
date: 2021-01-04
key: JavaJava.F.FontMetrics
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FontMetrics.metodos valor="bytesWidth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int bytesWidth(byte[] data, int off, int len)
~~~

## Parámetros
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[FontMetrics](/Java/FontMetrics/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FontMetrics.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
