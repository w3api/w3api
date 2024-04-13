---
title: FontMetrics.bytesWidth()
permalink: /Java/FontMetrics/bytesWidth/
date: 2021-01-11
key: Java.F.FontMetrics
category: Java
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
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
