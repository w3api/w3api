---
title: XmlSchema
permalink: Java/XmlSchema
date: 2021-01-04
key: JavaJava.X.XmlSchema
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlSchema.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(PACKAGE) public @interface XmlSchema
~~~

## Elementos
* [attributeFormDefault](/Java/XmlSchema/attributeFormDefault)
* [elementFormDefault](/Java/XmlSchema/elementFormDefault)
* [location](/Java/XmlSchema/location)
* [namespace](/Java/XmlSchema/namespace)
* [xmlns](/Java/XmlSchema/xmlns)

## Ejemplo
~~~java
{{ site.data.Java.X.XmlSchema.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlSchema.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
