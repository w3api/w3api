---
title: ParameterMetaData
permalink: Java/ParameterMetaData
date: 2021-01-04
key: JavaJava.P.ParameterMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.ParameterMetaData.description }}

## Sintaxis
~~~java
public interface ParameterMetaData extends Wrapper
~~~

## Campos
* [parameterModeIn](/Java/ParameterMetaData/parameterModeIn)
* [parameterModeInOut](/Java/ParameterMetaData/parameterModeInOut)
* [parameterModeOut](/Java/ParameterMetaData/parameterModeOut)
* [parameterModeUnknown](/Java/ParameterMetaData/parameterModeUnknown)
* [parameterNoNulls](/Java/ParameterMetaData/parameterNoNulls)
* [parameterNullable](/Java/ParameterMetaData/parameterNullable)
* [parameterNullableUnknown](/Java/ParameterMetaData/parameterNullableUnknown)

## Métodos
* [getParameterClassName()](/Java/ParameterMetaData/getParameterClassName)
* [getParameterCount()](/Java/ParameterMetaData/getParameterCount)
* [getParameterMode()](/Java/ParameterMetaData/getParameterMode)
* [getParameterType()](/Java/ParameterMetaData/getParameterType)
* [getParameterTypeName()](/Java/ParameterMetaData/getParameterTypeName)
* [getPrecision()](/Java/ParameterMetaData/getPrecision)
* [getScale()](/Java/ParameterMetaData/getScale)
* [isNullable()](/Java/ParameterMetaData/isNullable)
* [isSigned()](/Java/ParameterMetaData/isSigned)

## Ejemplo
~~~java
{{ site.data.Java.P.ParameterMetaData.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ParameterMetaData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
