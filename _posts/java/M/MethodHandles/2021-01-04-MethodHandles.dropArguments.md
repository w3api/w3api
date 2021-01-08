---
title: MethodHandles.dropArguments()
permalink: Java/MethodHandles/dropArguments
date: 2021-01-04
key: JavaJava.M.MethodHandles
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="dropArguments" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle dropArguments(MethodHandle target, int pos, Class<?>... valueTypes)
public static MethodHandle dropArguments(MethodHandle target, int pos, List<Class<?>> valueTypes)
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Class&lt;?&gt;... valueTypes**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>... valueTypes" %}
* **List&lt;Class&lt;?&gt;&gt; valueTypes**,  {% include w3api/param_description.html metodo=_data parametro="List<Class<?>> valueTypes" %}
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle target" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
