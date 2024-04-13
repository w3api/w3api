---
title: LambdaMetafactory.altMetafactory()
permalink: /Java/LambdaMetafactory/altMetafactory/
date: 2021-01-11
key: Java.L.LambdaMetafactory
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LambdaMetafactory.metodos valor="altMetafactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CallSite altMetafactory(MethodHandles.Lookup caller, String invokedName, MethodType invokedType, Object... args) throws LambdaConversionException
~~~

## Parámetros
* **Object... args**,  {% include w3api/param_description.html metodo=_dato parametro="Object... args" %}
* **MethodType invokedType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType invokedType" %}
* **String invokedName**,  {% include w3api/param_description.html metodo=_dato parametro="String invokedName" %}
* **MethodHandles.Lookup caller**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandles.Lookup caller" %}

## Excepciones
[LambdaConversionException](/Java/LambdaConversionException/)

## Clase Padre
[LambdaMetafactory](/Java/LambdaMetafactory/)

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
