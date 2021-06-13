---
title: PushbackInputStream.PushbackInputStream()
permalink: /Java/PushbackInputStream/PushbackInputStream/
date: 2021-01-11
key: Java.P.PushbackInputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PushbackInputStream.constructores valor="PushbackInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PushbackInputStream(InputStream in)
public PushbackInputStream(InputStream in, int size)
~~~

## Parámetros
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PushbackInputStream](/Java/PushbackInputStream/)

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
