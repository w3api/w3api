---
title: MethodHandles.Lookup.findStaticVarHandle()
permalink: Java/MethodHandles/Lookup/findStaticVarHandle
date: 2021-01-04
key: JavaJava.M.MethodHandles.Lookup
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="findStaticVarHandle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VarHandle findStaticVarHandle(Class<?> decl, String name, Class<?> type) throws NoSuchFieldException, IllegalAccessException
~~~

## Parámetros
* **Class&lt;?&gt; decl**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> decl" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Class&lt;?&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> type" %}

## Excepciones
[NoSuchFieldException](/Java/NoSuchFieldException/), [SecurityException](/Java/SecurityException/), [IllegalAccessException](/Java/IllegalAccessException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles.Lookup](/Java/MethodHandles/Lookup/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandles.Lookup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
