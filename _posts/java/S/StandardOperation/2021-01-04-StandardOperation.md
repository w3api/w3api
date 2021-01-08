---
title: StandardOperation
permalink: Java/StandardOperation
date: 2021-01-04
key: JavaJava.S.StandardOperation
category: java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'enumerado java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StandardOperation.description }}

## Sintaxis
~~~java
public enum StandardOperation extends Enum<StandardOperation> implements Operation
~~~

## Enumerados
* [CALL](/Java/StandardOperation/CALL)
* [GET](/Java/StandardOperation/GET)
* [NEW](/Java/StandardOperation/NEW)
* [REMOVE](/Java/StandardOperation/REMOVE)
* [SET](/Java/StandardOperation/SET)

## Métodos
* [valueOf()](/Java/StandardOperation/valueOf)
* [values()](/Java/StandardOperation/values)

## Ejemplo
~~~java
{{ site.data.Java.S.StandardOperation.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardOperation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
