---
title: MethodType.methodType()
permalink: Java/MethodType/methodType
date: 2021-01-11
key: JavaJava.M.MethodType
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodType.metodos valor="methodType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodType methodType(Class<?> rtype)
public static MethodType methodType(Class<?> rtype, Class<?> ptype0)
public static MethodType methodType(Class<?> rtype, Class<?>[] ptypes)
public static MethodType methodType(Class<?> rtype, Class<?> ptype0, Class<?>... ptypes)
public static MethodType methodType(Class<?> rtype, MethodType ptypes)
public static MethodType methodType(Class<?> rtype, List<Class<?>> ptypes)
~~~

## Parámetros
* **Class&lt;?&gt; ptype0**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> ptype0" %}
* **Class&lt;?&gt;... ptypes**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>... ptypes" %}
* **Class&lt;?&gt;[] ptypes**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>[] ptypes" %}
* **Class&lt;?&gt; rtype**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> rtype" %}
* **List&lt;Class&lt;?&gt;&gt; ptypes**,  {% include w3api/param_description.html metodo=_dato parametro="List<Class<?>> ptypes" %}
* **MethodType ptypes**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType ptypes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodType](/Java/MethodType/)

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
