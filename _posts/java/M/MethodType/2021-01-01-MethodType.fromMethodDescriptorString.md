---
title: MethodType.fromMethodDescriptorString()
permalink: Java/MethodType/fromMethodDescriptorString
date: 2021-01-11
key: JavaJava.M.MethodType
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodType.metodos valor="fromMethodDescriptorString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodType fromMethodDescriptorString(String descriptor, ClassLoader loader) throws IllegalArgumentException, TypeNotPresentException
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **String descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="String descriptor" %}

## Excepciones
[TypeNotPresentException](/Java/TypeNotPresentException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
