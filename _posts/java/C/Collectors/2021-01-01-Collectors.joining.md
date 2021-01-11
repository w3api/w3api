---
title: Collectors.joining()
permalink: Java/Collectors/joining
date: 2021-01-11
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="joining" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Collector<CharSequence,?,String> joining()
public static Collector<CharSequence,?,String> joining(CharSequence delimiter)
public static Collector<CharSequence,?,String> joining(CharSequence delimiter, CharSequence prefix, CharSequence suffix)
~~~

## Parámetros
* **CharSequence suffix**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence suffix" %}
* **CharSequence delimiter**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence delimiter" %}
* **CharSequence prefix**,  {% include w3api/param_description.html metodo=_dato parametro="CharSequence prefix" %}

## Clase Padre
[Collectors](/Java/Collectors/)

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
