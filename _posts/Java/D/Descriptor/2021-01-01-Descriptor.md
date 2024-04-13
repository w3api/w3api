---
title: Descriptor
permalink: /Java/Descriptor/
date: 2021-01-11
key: Java.D.Descriptor
category: Java
tags: ['java se', 'javax.management', 'java.management', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.Descriptor.description }}

## Sintaxis
~~~java
public interface Descriptor extends Serializable, Cloneable
~~~

## Métodos
* [clone()](/Java/Descriptor/clone/)
* [equals()](/Java/Descriptor/equals/)
* [getFieldNames()](/Java/Descriptor/getFieldNames/)
* [getFields()](/Java/Descriptor/getFields/)
* [getFieldValue()](/Java/Descriptor/getFieldValue/)
* [getFieldValues()](/Java/Descriptor/getFieldValues/)
* [hashCode()](/Java/Descriptor/hashCode/)
* [isValid()](/Java/Descriptor/isValid/)
* [removeField()](/Java/Descriptor/removeField/)
* [setField()](/Java/Descriptor/setField/)
* [setFields()](/Java/Descriptor/setFields/)

## Ejemplo
~~~java
{{ site.data.Java.D.Descriptor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.Descriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
