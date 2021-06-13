---
title: ReferenceType
permalink: Java/ReferenceType-com-sun-jdi
date: 2021-01-11
key: Java.R.ReferenceType-com-sun-jdi
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReferenceType-com-sun-jdi.description }}

## Sintaxis
~~~java
public interface ReferenceType extends Type, Comparable<ReferenceType>, Accessible
~~~

## Métodos
* [allFields()](/Java/ReferenceType-com-sun-jdi/allFields)
* [allLineLocations()](/Java/ReferenceType-com-sun-jdi/allLineLocations)
* [allMethods()](/Java/ReferenceType-com-sun-jdi/allMethods)
* [availableStrata()](/Java/ReferenceType-com-sun-jdi/availableStrata)
* [classLoader()](/Java/ReferenceType-com-sun-jdi/classLoader)
* [classObject()](/Java/ReferenceType-com-sun-jdi/classObject)
* [constantPool()](/Java/ReferenceType-com-sun-jdi/constantPool)
* [constantPoolCount()](/Java/ReferenceType-com-sun-jdi/constantPoolCount)
* [defaultStratum()](/Java/ReferenceType-com-sun-jdi/defaultStratum)
* [equals()](/Java/ReferenceType-com-sun-jdi/equals)
* [failedToInitialize()](/Java/ReferenceType-com-sun-jdi/failedToInitialize)
* [fieldByName()](/Java/ReferenceType-com-sun-jdi/fieldByName)
* [fields()](/Java/ReferenceType-com-sun-jdi/fields)
* [genericSignature()](/Java/ReferenceType-com-sun-jdi/genericSignature)
* [getValue()](/Java/ReferenceType-com-sun-jdi/getValue)
* [getValues()](/Java/ReferenceType-com-sun-jdi/getValues)
* [hashCode()](/Java/ReferenceType-com-sun-jdi/hashCode)
* [instances()](/Java/ReferenceType-com-sun-jdi/instances)
* [isAbstract()](/Java/ReferenceType-com-sun-jdi/isAbstract)
* [isFinal()](/Java/ReferenceType-com-sun-jdi/isFinal)
* [isInitialized()](/Java/ReferenceType-com-sun-jdi/isInitialized)
* [isPrepared()](/Java/ReferenceType-com-sun-jdi/isPrepared)
* [isStatic()](/Java/ReferenceType-com-sun-jdi/isStatic)
* [isVerified()](/Java/ReferenceType-com-sun-jdi/isVerified)
* [locationsOfLine()](/Java/ReferenceType-com-sun-jdi/locationsOfLine)
* [majorVersion()](/Java/ReferenceType-com-sun-jdi/majorVersion)
* [methods()](/Java/ReferenceType-com-sun-jdi/methods)
* [methodsByName()](/Java/ReferenceType-com-sun-jdi/methodsByName)
* [minorVersion()](/Java/ReferenceType-com-sun-jdi/minorVersion)
* [module()](/Java/ReferenceType-com-sun-jdi/module)
* [name()](/Java/ReferenceType-com-sun-jdi/name)
* [nestedTypes()](/Java/ReferenceType-com-sun-jdi/nestedTypes)
* [sourceDebugExtension()](/Java/ReferenceType-com-sun-jdi/sourceDebugExtension)
* [sourceName()](/Java/ReferenceType-com-sun-jdi/sourceName)
* [sourceNames()](/Java/ReferenceType-com-sun-jdi/sourceNames)
* [sourcePaths()](/Java/ReferenceType-com-sun-jdi/sourcePaths)
* [visibleFields()](/Java/ReferenceType-com-sun-jdi/visibleFields)
* [visibleMethods()](/Java/ReferenceType-com-sun-jdi/visibleMethods)

## Ejemplo
~~~java
{{ site.data.Java.R.ReferenceType-com-sun-jdi.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReferenceType-com-sun-jdi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
