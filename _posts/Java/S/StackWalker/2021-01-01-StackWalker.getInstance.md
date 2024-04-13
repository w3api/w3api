---
title: StackWalker.getInstance()
permalink: /Java/StackWalker/getInstance/
date: 2021-01-11
key: Java.S.StackWalker
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackWalker.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static StackWalker getInstance()
public static StackWalker getInstance(StackWalker.Option option)
public static StackWalker getInstance(Set<StackWalker.Option> options)
public static StackWalker getInstance(Set<StackWalker.Option> options, int estimateDepth)
~~~

## Parámetros
* **StackWalker.Option option**,  {% include w3api/param_description.html metodo=_dato parametro="StackWalker.Option option" %}
* **int estimateDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int estimateDepth" %}
* **Set&lt;StackWalker.Option&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="Set<StackWalker.Option> options" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StackWalker](/Java/StackWalker/)

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
