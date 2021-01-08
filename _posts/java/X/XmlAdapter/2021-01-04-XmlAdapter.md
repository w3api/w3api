---
title: XmlAdapter
permalink: Java/XmlAdapter
date: 2021-01-04
key: JavaJava.X.XmlAdapter
category: java
tags: ['java se', 'javax.xml.bind.annotation.adapters', 'java.xml.bind', 'clase java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlAdapter.description }}

## Sintaxis
~~~java
public abstract class XmlAdapter<ValueType,BoundType> extends Object
~~~

## Constructores
* [XmlAdapter()](/Java/XmlAdapter/XmlAdapter/)

## Métodos
* [marshal()](/Java/XmlAdapter/marshal)
* [unmarshal()](/Java/XmlAdapter/unmarshal)

## Ejemplo
~~~java
{{ site.data.Java.X.XmlAdapter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlAdapter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
