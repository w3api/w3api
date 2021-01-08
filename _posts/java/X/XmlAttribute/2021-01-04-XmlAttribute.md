---
title: XmlAttribute
permalink: Java/XmlAttribute
date: 2021-01-04
key: JavaJava.X.XmlAttribute
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlAttribute.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,METHOD}) public @interface XmlAttribute
~~~

## Elementos
* [name](/Java/XmlAttribute/name)
* [namespace](/Java/XmlAttribute/namespace)
* [required](/Java/XmlAttribute/required)

## Ejemplo
~~~java
{{ site.data.Java.X.XmlAttribute.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlAttribute.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
