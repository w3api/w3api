---
title: MethodHandle.invokeWithArguments()
permalink: Java/MethodHandle/invokeWithArguments
date: 2021-01-04
key: JavaJava.M.MethodHandle
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandle.metodos valor="invokeWithArguments" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object invokeWithArguments(Object... arguments) throws Throwable
public Object invokeWithArguments(List<?> arguments) throws Throwable
~~~

## Parámetros
* **List&lt;?&gt; arguments**,  {% include w3api/param_description.html metodo=_data parametro="List<?> arguments" %}
* **Object... arguments**,  {% include w3api/param_description.html metodo=_data parametro="Object... arguments" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [ClassCastException](/Java/ClassCastException/), [WrongMethodTypeException](/Java/WrongMethodTypeException/)

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
