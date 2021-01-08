---
title: XmlElements
permalink: Java/XmlElements
date: 2021-01-04
key: JavaJava.X.XmlElements
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlElements.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,METHOD}) public @interface XmlElements
~~~

## Ejemplo
~~~java
{{ site.data.Java.X.XmlElements.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlElements.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
