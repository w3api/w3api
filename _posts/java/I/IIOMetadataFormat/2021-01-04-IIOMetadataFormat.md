---
title: IIOMetadataFormat
permalink: Java/IIOMetadataFormat
date: 2021-01-04
key: JavaJava.I.IIOMetadataFormat
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IIOMetadataFormat.description }}

## Sintaxis
~~~java
public interface IIOMetadataFormat
~~~

## Campos
* [CHILD_POLICY_ALL](/Java/IIOMetadataFormat/CHILD_POLICY_ALL)
* [CHILD_POLICY_CHOICE](/Java/IIOMetadataFormat/CHILD_POLICY_CHOICE)
* [CHILD_POLICY_EMPTY](/Java/IIOMetadataFormat/CHILD_POLICY_EMPTY)
* [CHILD_POLICY_MAX](/Java/IIOMetadataFormat/CHILD_POLICY_MAX)
* [CHILD_POLICY_REPEAT](/Java/IIOMetadataFormat/CHILD_POLICY_REPEAT)
* [CHILD_POLICY_SEQUENCE](/Java/IIOMetadataFormat/CHILD_POLICY_SEQUENCE)
* [CHILD_POLICY_SOME](/Java/IIOMetadataFormat/CHILD_POLICY_SOME)
* [DATATYPE_BOOLEAN](/Java/IIOMetadataFormat/DATATYPE_BOOLEAN)
* [DATATYPE_DOUBLE](/Java/IIOMetadataFormat/DATATYPE_DOUBLE)
* [DATATYPE_FLOAT](/Java/IIOMetadataFormat/DATATYPE_FLOAT)
* [DATATYPE_INTEGER](/Java/IIOMetadataFormat/DATATYPE_INTEGER)
* [DATATYPE_STRING](/Java/IIOMetadataFormat/DATATYPE_STRING)
* [VALUE_ARBITRARY](/Java/IIOMetadataFormat/VALUE_ARBITRARY)
* [VALUE_ENUMERATION](/Java/IIOMetadataFormat/VALUE_ENUMERATION)
* [VALUE_LIST](/Java/IIOMetadataFormat/VALUE_LIST)
* [VALUE_NONE](/Java/IIOMetadataFormat/VALUE_NONE)
* [VALUE_RANGE](/Java/IIOMetadataFormat/VALUE_RANGE)
* [VALUE_RANGE_MAX_INCLUSIVE](/Java/IIOMetadataFormat/VALUE_RANGE_MAX_INCLUSIVE)
* [VALUE_RANGE_MAX_INCLUSIVE_MASK](/Java/IIOMetadataFormat/VALUE_RANGE_MAX_INCLUSIVE_MASK)
* [VALUE_RANGE_MIN_INCLUSIVE](/Java/IIOMetadataFormat/VALUE_RANGE_MIN_INCLUSIVE)
* [VALUE_RANGE_MIN_INCLUSIVE_MASK](/Java/IIOMetadataFormat/VALUE_RANGE_MIN_INCLUSIVE_MASK)
* [VALUE_RANGE_MIN_MAX_INCLUSIVE](/Java/IIOMetadataFormat/VALUE_RANGE_MIN_MAX_INCLUSIVE)

## Métodos
* [canNodeAppear()](/Java/IIOMetadataFormat/canNodeAppear)
* [getAttributeDataType()](/Java/IIOMetadataFormat/getAttributeDataType)
* [getAttributeDefaultValue()](/Java/IIOMetadataFormat/getAttributeDefaultValue)
* [getAttributeDescription()](/Java/IIOMetadataFormat/getAttributeDescription)
* [getAttributeEnumerations()](/Java/IIOMetadataFormat/getAttributeEnumerations)
* [getAttributeListMaxLength()](/Java/IIOMetadataFormat/getAttributeListMaxLength)
* [getAttributeListMinLength()](/Java/IIOMetadataFormat/getAttributeListMinLength)
* [getAttributeMaxValue()](/Java/IIOMetadataFormat/getAttributeMaxValue)
* [getAttributeMinValue()](/Java/IIOMetadataFormat/getAttributeMinValue)
* [getAttributeNames()](/Java/IIOMetadataFormat/getAttributeNames)
* [getAttributeValueType()](/Java/IIOMetadataFormat/getAttributeValueType)
* [getChildNames()](/Java/IIOMetadataFormat/getChildNames)
* [getChildPolicy()](/Java/IIOMetadataFormat/getChildPolicy)
* [getElementDescription()](/Java/IIOMetadataFormat/getElementDescription)
* [getElementMaxChildren()](/Java/IIOMetadataFormat/getElementMaxChildren)
* [getElementMinChildren()](/Java/IIOMetadataFormat/getElementMinChildren)
* [getObjectArrayMaxLength()](/Java/IIOMetadataFormat/getObjectArrayMaxLength)
* [getObjectArrayMinLength()](/Java/IIOMetadataFormat/getObjectArrayMinLength)
* [getObjectClass()](/Java/IIOMetadataFormat/getObjectClass)
* [getObjectDefaultValue()](/Java/IIOMetadataFormat/getObjectDefaultValue)
* [getObjectEnumerations()](/Java/IIOMetadataFormat/getObjectEnumerations)
* [getObjectMaxValue()](/Java/IIOMetadataFormat/getObjectMaxValue)
* [getObjectMinValue()](/Java/IIOMetadataFormat/getObjectMinValue)
* [getObjectValueType()](/Java/IIOMetadataFormat/getObjectValueType)
* [getRootName()](/Java/IIOMetadataFormat/getRootName)
* [isAttributeRequired()](/Java/IIOMetadataFormat/isAttributeRequired)

## Ejemplo
~~~java
{{ site.data.Java.I.IIOMetadataFormat.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOMetadataFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
