---
title: MethodHandles.dropArgumentsToMatch()
permalink: Java/MethodHandles/dropArgumentsToMatch
date: 2021-01-11
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="dropArgumentsToMatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle dropArgumentsToMatch(MethodHandle target, int skip, List<Class<?>> newTypes, int pos)
~~~

## Parámetros
* **int skip**,  {% include w3api/param_description.html metodo=_dato parametro="int skip" %}
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle target" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}
* **List&lt;Class&lt;?&gt;&gt; newTypes**,  {% include w3api/param_description.html metodo=_dato parametro="List<Class<?>> newTypes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles](/Java/MethodHandles/)

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
