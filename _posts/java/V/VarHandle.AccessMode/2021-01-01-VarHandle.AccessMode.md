---
title: VarHandle.AccessMode
permalink: Java/VarHandle/AccessMode
date: 2021-01-11
key: JavaJava.V.VarHandle.AccessMode
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'enumerado java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.VarHandle.AccessMode.description }}

## Sintaxis
~~~java
public static enum VarHandle.AccessMode extends Enum<VarHandle.AccessMode>
~~~

## Enumerados
* [COMPARE_AND_EXCHANGE](/Java/VarHandle/AccessMode/COMPARE_AND_EXCHANGE)
* [COMPARE_AND_EXCHANGE_ACQUIRE](/Java/VarHandle/AccessMode/COMPARE_AND_EXCHANGE_ACQUIRE)
* [COMPARE_AND_EXCHANGE_RELEASE](/Java/VarHandle/AccessMode/COMPARE_AND_EXCHANGE_RELEASE)
* [COMPARE_AND_SET](/Java/VarHandle/AccessMode/COMPARE_AND_SET)
* [GET](/Java/VarHandle/AccessMode/GET)
* [GET_ACQUIRE](/Java/VarHandle/AccessMode/GET_ACQUIRE)
* [GET_AND_ADD](/Java/VarHandle/AccessMode/GET_AND_ADD)
* [GET_AND_ADD_ACQUIRE](/Java/VarHandle/AccessMode/GET_AND_ADD_ACQUIRE)
* [GET_AND_ADD_RELEASE](/Java/VarHandle/AccessMode/GET_AND_ADD_RELEASE)
* [GET_AND_BITWISE_AND](/Java/VarHandle/AccessMode/GET_AND_BITWISE_AND)
* [GET_AND_BITWISE_AND_ACQUIRE](/Java/VarHandle/AccessMode/GET_AND_BITWISE_AND_ACQUIRE)
* [GET_AND_BITWISE_AND_RELEASE](/Java/VarHandle/AccessMode/GET_AND_BITWISE_AND_RELEASE)
* [GET_AND_BITWISE_OR](/Java/VarHandle/AccessMode/GET_AND_BITWISE_OR)
* [GET_AND_BITWISE_OR_ACQUIRE](/Java/VarHandle/AccessMode/GET_AND_BITWISE_OR_ACQUIRE)
* [GET_AND_BITWISE_OR_RELEASE](/Java/VarHandle/AccessMode/GET_AND_BITWISE_OR_RELEASE)
* [GET_AND_BITWISE_XOR](/Java/VarHandle/AccessMode/GET_AND_BITWISE_XOR)
* [GET_AND_BITWISE_XOR_ACQUIRE](/Java/VarHandle/AccessMode/GET_AND_BITWISE_XOR_ACQUIRE)
* [GET_AND_BITWISE_XOR_RELEASE](/Java/VarHandle/AccessMode/GET_AND_BITWISE_XOR_RELEASE)
* [GET_AND_SET](/Java/VarHandle/AccessMode/GET_AND_SET)
* [GET_AND_SET_ACQUIRE](/Java/VarHandle/AccessMode/GET_AND_SET_ACQUIRE)
* [GET_AND_SET_RELEASE](/Java/VarHandle/AccessMode/GET_AND_SET_RELEASE)
* [GET_OPAQUE](/Java/VarHandle/AccessMode/GET_OPAQUE)
* [GET_VOLATILE](/Java/VarHandle/AccessMode/GET_VOLATILE)
* [SET](/Java/VarHandle/AccessMode/SET)
* [SET_OPAQUE](/Java/VarHandle/AccessMode/SET_OPAQUE)
* [SET_RELEASE](/Java/VarHandle/AccessMode/SET_RELEASE)
* [SET_VOLATILE](/Java/VarHandle/AccessMode/SET_VOLATILE)
* [WEAK_COMPARE_AND_SET](/Java/VarHandle/AccessMode/WEAK_COMPARE_AND_SET)
* [WEAK_COMPARE_AND_SET_ACQUIRE](/Java/VarHandle/AccessMode/WEAK_COMPARE_AND_SET_ACQUIRE)
* [WEAK_COMPARE_AND_SET_PLAIN](/Java/VarHandle/AccessMode/WEAK_COMPARE_AND_SET_PLAIN)
* [WEAK_COMPARE_AND_SET_RELEASE](/Java/VarHandle/AccessMode/WEAK_COMPARE_AND_SET_RELEASE)

## Métodos
* [methodName()](/Java/VarHandle/AccessMode/methodName)
* [valueFromMethodName()](/Java/VarHandle/AccessMode/valueFromMethodName)
* [valueOf()](/Java/VarHandle/AccessMode/valueOf)
* [values()](/Java/VarHandle/AccessMode/values)

## Ejemplo
~~~java
{{ site.data.Java.V.VarHandle.AccessMode.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VarHandle.AccessMode.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
