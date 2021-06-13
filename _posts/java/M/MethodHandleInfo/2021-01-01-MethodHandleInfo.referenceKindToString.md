---
title: MethodHandleInfo.referenceKindToString()
permalink: Java/MethodHandleInfo/referenceKindToString
date: 2021-01-11
key: JavaJava.M.MethodHandleInfo
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandleInfo.metodos valor="referenceKindToString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static String referenceKindToString(int referenceKind)
~~~

## Parámetros
* **int referenceKind**,  {% include w3api/param_description.html metodo=_dato parametro="int referenceKind" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodHandleInfo](/Java/MethodHandleInfo/)

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
