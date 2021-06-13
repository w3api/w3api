---
title: MethodHandleInfo
permalink: Java/MethodHandleInfo
date: 2021-01-11
key: JavaJava.M.MethodHandleInfo
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MethodHandleInfo.description }}

## Sintaxis
~~~java
public interface MethodHandleInfo
~~~

## Campos
* [REF_getField](/Java/MethodHandleInfo/REF_getField)
* [REF_getStatic](/Java/MethodHandleInfo/REF_getStatic)
* [REF_invokeInterface](/Java/MethodHandleInfo/REF_invokeInterface)
* [REF_invokeSpecial](/Java/MethodHandleInfo/REF_invokeSpecial)
* [REF_invokeStatic](/Java/MethodHandleInfo/REF_invokeStatic)
* [REF_invokeVirtual](/Java/MethodHandleInfo/REF_invokeVirtual)
* [REF_newInvokeSpecial](/Java/MethodHandleInfo/REF_newInvokeSpecial)
* [REF_putField](/Java/MethodHandleInfo/REF_putField)
* [REF_putStatic](/Java/MethodHandleInfo/REF_putStatic)

## Métodos
* [getDeclaringClass()](/Java/MethodHandleInfo/getDeclaringClass)
* [getMethodType()](/Java/MethodHandleInfo/getMethodType)
* [getModifiers()](/Java/MethodHandleInfo/getModifiers)
* [getName()](/Java/MethodHandleInfo/getName)
* [getReferenceKind()](/Java/MethodHandleInfo/getReferenceKind)
* [isVarArgs()](/Java/MethodHandleInfo/isVarArgs)
* [referenceKindToString()](/Java/MethodHandleInfo/referenceKindToString)
* [reflectAs()](/Java/MethodHandleInfo/reflectAs)
* [toString()](/Java/MethodHandleInfo/toString)

## Ejemplo
~~~java
{{ site.data.Java.M.MethodHandleInfo.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodHandleInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
