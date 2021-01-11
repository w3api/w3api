---
title: MethodHandles.Lookup.bind()
permalink: Java/MethodHandles/Lookup/bind
date: 2021-01-11
key: JavaJava.M.MethodHandles.Lookup
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle bind(Object receiver, String name, MethodType type) throws NoSuchMethodException, IllegalAccessException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **MethodType type**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType type" %}
* **Object receiver**,  {% include w3api/param_description.html metodo=_dato parametro="Object receiver" %}

## Excepciones
[NoSuchMethodException](/Java/NoSuchMethodException/), [SecurityException](/Java/SecurityException/), [IllegalAccessException](/Java/IllegalAccessException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles.Lookup](/Java/MethodHandles/Lookup/)

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
