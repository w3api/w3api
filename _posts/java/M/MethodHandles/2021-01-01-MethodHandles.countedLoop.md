---
title: MethodHandles.countedLoop()
permalink: Java/MethodHandles/countedLoop
date: 2021-01-11
key: JavaJava.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="countedLoop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle countedLoop(MethodHandle iterations, MethodHandle init, MethodHandle body)
public static MethodHandle countedLoop(MethodHandle start, MethodHandle end, MethodHandle init, MethodHandle body)
~~~

## Parámetros
* **MethodHandle body**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle body" %}
* **MethodHandle start**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle start" %}
* **MethodHandle iterations**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle iterations" %}
* **MethodHandle end**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle end" %}
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
