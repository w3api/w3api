---
title: MethodHandles.Lookup.findVarHandle()
permalink: /Java/MethodHandles/Lookup/findVarHandle/
date: 2021-01-11
key: Java.M.MethodHandles.Lookup
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.Lookup.metodos valor="findVarHandle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VarHandle findVarHandle(Class<?> recv, String name, Class<?> type) throws NoSuchFieldException, IllegalAccessException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Class&lt;?&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> type" %}
* **Class&lt;?&gt; recv**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> recv" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalAccessException](/Java/IllegalAccessException/), [NoSuchFieldException](/Java/NoSuchFieldException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodHandles.Lookup](/Java/MethodHandles/Lookup/)

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
