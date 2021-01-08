---
title: MethodType.methodType()
permalink: Java/MethodType/methodType
date: 2021-01-04
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
* **Class&lt;?&gt; rtype**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> rtype" %}
* **List&lt;Class&lt;?&gt;&gt; ptypes**,  {% include w3api/param_description.html metodo=_data parametro="List<Class<?>> ptypes" %}
* **Class&lt;?&gt;[] ptypes**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>[] ptypes" %}
* **Class&lt;?&gt; ptype0**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> ptype0" %}
* **Class&lt;?&gt;... ptypes**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>... ptypes" %}
* **MethodType ptypes**,  {% include w3api/param_description.html metodo=_data parametro="MethodType ptypes" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodType](/Java/MethodType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
