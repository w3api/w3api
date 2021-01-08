---
title: MethodHandles.throwException()
permalink: Java/MethodHandles/throwException
date: 2021-01-04
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="throwException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle throwException(Class<?> returnType, Class<? extends Throwable> exType)
~~~

## Parámetros
* **Class&lt;?&gt; returnType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> returnType" %}
* **Class&lt;? extends Throwable&gt; exType**,  {% include w3api/param_description.html metodo=_data parametro="Class<? extends Throwable> exType" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles](/Java/MethodHandles/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandles.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
