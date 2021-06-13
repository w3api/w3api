---
title: FontMetrics.charsWidth()
permalink: /Java/FontMetrics/charsWidth/
date: 2021-01-11
key: Java.F.FontMetrics
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FontMetrics.metodos valor="charsWidth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int charsWidth(char[] data, int off, int len)
~~~

## Parámetros
* **char[] data**,  {% include w3api/param_description.html metodo=_dato parametro="char[] data" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
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
