---
title: MethodHandle.bindTo()
permalink: Java/MethodHandle/bindTo
date: 2021-01-11
key: JavaJava.M.MethodHandle
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandle.metodos valor="bindTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle bindTo(Object x)
~~~

## Parámetros
* **Object x**,  {% include w3api/param_description.html metodo=_dato parametro="Object x" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/)

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
