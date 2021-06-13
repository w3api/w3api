---
title: MethodHandle.asVarargsCollector()
permalink: Java/MethodHandle/asVarargsCollector
date: 2021-01-11
key: JavaJava.M.MethodHandle
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandle.metodos valor="asVarargsCollector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle asVarargsCollector(Class<?> arrayType)
~~~

## Parámetros
* **Class&lt;?&gt; arrayType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> arrayType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
