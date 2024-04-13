---
title: MethodHandle.asCollector()
permalink: /Java/MethodHandle/asCollector/
date: 2021-01-11
key: Java.M.MethodHandle
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandle.metodos valor="asCollector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle asCollector(int collectArgPos, Class<?> arrayType, int arrayLength)
public MethodHandle asCollector(Class<?> arrayType, int arrayLength)
~~~

## Parámetros
* **int collectArgPos**,  {% include w3api/param_description.html metodo=_dato parametro="int collectArgPos" %}
* **Class&lt;?&gt; arrayType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> arrayType" %}
* **int arrayLength**,  {% include w3api/param_description.html metodo=_dato parametro="int arrayLength" %}

## Excepciones
[WrongMethodTypeException](/Java/WrongMethodTypeException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandle](/Java/MethodHandle/)

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
