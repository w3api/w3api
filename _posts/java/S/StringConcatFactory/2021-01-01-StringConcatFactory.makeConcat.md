---
title: StringConcatFactory.makeConcat()
permalink: /Java/StringConcatFactory/makeConcat/
date: 2021-01-11
key: Java.S.StringConcatFactory
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringConcatFactory.metodos valor="makeConcat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CallSite makeConcat(MethodHandles.Lookup lookup, String name, MethodType concatType) throws StringConcatException
~~~

## Parámetros
* **MethodHandles.Lookup lookup**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandles.Lookup lookup" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **MethodType concatType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType concatType" %}

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
