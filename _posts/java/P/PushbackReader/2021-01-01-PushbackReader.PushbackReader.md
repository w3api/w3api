---
title: PushbackReader.PushbackReader()
permalink: /Java/PushbackReader/PushbackReader/
date: 2021-01-11
key: Java.P.PushbackReader
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PushbackReader.constructores valor="PushbackReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PushbackReader(Reader in)
public PushbackReader(Reader in, int size)
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **Reader in**,  {% include w3api/param_description.html metodo=_dato parametro="Reader in" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PushbackReader](/Java/PushbackReader/)

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
