---
title: StringConcatFactory.makeConcatWithConstants()
permalink: /Java/StringConcatFactory/makeConcatWithConstants/
date: 2021-01-11
key: Java.S.StringConcatFactory
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringConcatFactory.metodos valor="makeConcatWithConstants" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CallSite makeConcatWithConstants(MethodHandles.Lookup lookup, String name, MethodType concatType, String recipe, Object... constants) throws StringConcatException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String recipe**,  {% include w3api/param_description.html metodo=_dato parametro="String recipe" %}
* **MethodHandles.Lookup lookup**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandles.Lookup lookup" %}
* **MethodType concatType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType concatType" %}
* **Object... constants**,  {% include w3api/param_description.html metodo=_dato parametro="Object... constants" %}

## Excepciones
[StringConcatException](/Java/StringConcatException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[StringConcatFactory](/Java/StringConcatFactory/)

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
