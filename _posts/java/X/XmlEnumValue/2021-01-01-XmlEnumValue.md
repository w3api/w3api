---
title: XmlEnumValue
permalink: Java/XmlEnumValue
date: 2021-01-11
key: JavaJava.X.XmlEnumValue
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlEnumValue.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(FIELD) public @interface XmlEnumValue
~~~

## Ejemplo
~~~java
{{ site.data.Java.X.XmlEnumValue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlEnumValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
