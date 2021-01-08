---
title: StandardNamespace
permalink: Java/StandardNamespace
date: 2021-01-04
key: JavaJava.S.StandardNamespace
category: java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'enumerado java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StandardNamespace.description }}

## Sintaxis
~~~java
public enum StandardNamespace extends Enum<StandardNamespace> implements Namespace
~~~

## Enumerados
* [ELEMENT](/Java/StandardNamespace/ELEMENT)
* [METHOD](/Java/StandardNamespace/METHOD)
* [PROPERTY](/Java/StandardNamespace/PROPERTY)

## Métodos
* [findFirst()](/Java/StandardNamespace/findFirst)
* [valueOf()](/Java/StandardNamespace/valueOf)
* [values()](/Java/StandardNamespace/values)

## Ejemplo
~~~java
{{ site.data.Java.S.StandardNamespace.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardNamespace.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
