---
title: CharsetEncoder.canEncode()
permalink: /Java/CharsetEncoder/canEncode/
date: 2021-01-11
key: Java.C.CharsetEncoder
category: Java
tags: ['java se', 'java.nio.charset', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharsetEncoder.metodos valor="canEncode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean canEncode(char c)
public boolean canEncode(CharSequence cs)
~~~

## Parámetros
* **CharSequence cs**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence cs" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[CharsetEncoder](/Java/CharsetEncoder/)

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
