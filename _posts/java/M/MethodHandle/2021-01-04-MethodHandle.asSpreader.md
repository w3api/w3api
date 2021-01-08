---
title: MethodHandle.asSpreader()
permalink: Java/MethodHandle/asSpreader
date: 2021-01-04
key: JavaJava.M.MethodHandle
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandle.metodos valor="asSpreader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle asSpreader(int spreadArgPos, Class<?> arrayType, int arrayLength)
public MethodHandle asSpreader(Class<?> arrayType, int arrayLength)
~~~

## Parámetros
* **int arrayLength**,  {% include w3api/param_description.html metodo=_data parametro="int arrayLength" %}
* **int spreadArgPos**,  {% include w3api/param_description.html metodo=_data parametro="int spreadArgPos" %}
* **Class&lt;?&gt; arrayType**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> arrayType" %}

## Excepciones
[WrongMethodTypeException](/Java/WrongMethodTypeException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
