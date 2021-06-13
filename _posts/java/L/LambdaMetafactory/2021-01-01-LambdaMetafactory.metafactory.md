---
title: LambdaMetafactory.metafactory()
permalink: Java/LambdaMetafactory/metafactory
date: 2021-01-11
key: Java.L.LambdaMetafactory
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LambdaMetafactory.metodos valor="metafactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CallSite metafactory(MethodHandles.Lookup caller, String invokedName, MethodType invokedType, MethodType samMethodType, MethodHandle implMethod, MethodType instantiatedMethodType) throws LambdaConversionException
~~~

## Parámetros
* **MethodType samMethodType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType samMethodType" %}
* **MethodType invokedType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType invokedType" %}
* **String invokedName**,  {% include w3api/param_description.html metodo=_dato parametro="String invokedName" %}
* **MethodType instantiatedMethodType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType instantiatedMethodType" %}
* **MethodHandles.Lookup caller**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandles.Lookup caller" %}
* **MethodHandle implMethod**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle implMethod" %}

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
