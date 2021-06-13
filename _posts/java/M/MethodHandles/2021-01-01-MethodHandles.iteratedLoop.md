---
title: MethodHandles.iteratedLoop()
permalink: /Java/MethodHandles/iteratedLoop/
date: 2021-01-11
key: Java.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="iteratedLoop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle iteratedLoop(MethodHandle iterator, MethodHandle init, MethodHandle body)
~~~

## Parámetros
* **MethodHandle body**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle body" %}
* **MethodHandle iterator**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle iterator" %}
* **MethodHandle init**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle init" %}

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
