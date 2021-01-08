---
title: MethodHandle.asCollector()
permalink: Java/MethodHandle/asCollector
date: 2021-01-04
key: JavaJava.M.MethodHandle
category: java
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
* **int arrayLength**,  {% include w3api/param_description.html metodo=_data parametro="int arrayLength" %}
* **Class&lt;?&gt; arrayType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> arrayType" %}
* **int collectArgPos**,  {% include w3api/param_description.html metodo=_data parametro="int collectArgPos" %}

## Excepciones
[WrongMethodTypeException](/Java/WrongMethodTypeException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodHandle](/Java/MethodHandle/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
