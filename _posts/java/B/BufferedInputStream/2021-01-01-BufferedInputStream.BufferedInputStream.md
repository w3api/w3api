---
title: BufferedInputStream.BufferedInputStream()
permalink: /Java/BufferedInputStream/BufferedInputStream/
date: 2021-01-11
key: JavaJava.B.BufferedInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedInputStream.constructores valor="BufferedInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedInputStream(InputStream in)
public BufferedInputStream(InputStream in, int size)
~~~

## Parámetros
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BufferedInputStream](/Java/BufferedInputStream/)

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
