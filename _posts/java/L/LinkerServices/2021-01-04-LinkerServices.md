---
title: LinkerServices
permalink: Java/LinkerServices
date: 2021-01-04
key: JavaJava.L.LinkerServices
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LinkerServices.description }}

## Sintaxis
~~~java
public interface LinkerServices
~~~

## Métodos
* [asType()](/Java/LinkerServices/asType)
* [asTypeLosslessReturn()](/Java/LinkerServices/asTypeLosslessReturn)
* [canConvert()](/Java/LinkerServices/canConvert)
* [compareConversion()](/Java/LinkerServices/compareConversion)
* [filterInternalObjects()](/Java/LinkerServices/filterInternalObjects)
* [getGuardedInvocation()](/Java/LinkerServices/getGuardedInvocation)
* [getTypeConverter()](/Java/LinkerServices/getTypeConverter)
* [getWithLookup()](/Java/LinkerServices/getWithLookup)

## Ejemplo
~~~java
{{ site.data.Java.L.LinkerServices.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkerServices.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
