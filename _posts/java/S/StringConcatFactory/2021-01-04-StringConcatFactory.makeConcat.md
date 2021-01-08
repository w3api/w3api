---
title: StringConcatFactory.makeConcat()
permalink: Java/StringConcatFactory/makeConcat
date: 2021-01-04
key: JavaJava.S.StringConcatFactory
category: java
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
* **MethodType concatType**,  {% include w3api/param_description.html metodo=_data parametro="MethodType concatType" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **MethodHandles.Lookup lookup**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandles.Lookup lookup" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [StringConcatException](/Java/StringConcatException/)

## Clase Padre
[StringConcatFactory](/Java/StringConcatFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringConcatFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
