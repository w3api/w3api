---
title: MethodHandles.byteArrayViewVarHandle()
permalink: Java/MethodHandles/byteArrayViewVarHandle
date: 2021-01-11
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="byteArrayViewVarHandle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static VarHandle byteArrayViewVarHandle(Class<?> viewArrayClass, ByteOrder byteOrder) throws IllegalArgumentException
~~~

## Parámetros
* **Class&lt;?&gt; viewArrayClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> viewArrayClass" %}
* **ByteOrder byteOrder**,  {% include w3api/param_description.html metodo=_dato parametro="ByteOrder byteOrder" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

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
