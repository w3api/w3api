---
title: MethodHandle.bindTo()
permalink: Java/MethodHandle/bindTo
date: 2021-01-04
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
* **Object x**,  {% include w3api/param_description.html metodo=_data parametro="Object x" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
