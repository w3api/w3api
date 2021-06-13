---
title: BufferedOutputStream.BufferedOutputStream()
permalink: /Java/BufferedOutputStream/BufferedOutputStream/
date: 2021-01-11
key: Java.B.BufferedOutputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedOutputStream.constructores valor="BufferedOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedOutputStream(OutputStream out)
public BufferedOutputStream(OutputStream out, int size)
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BufferedOutputStream](/Java/BufferedOutputStream/)

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
