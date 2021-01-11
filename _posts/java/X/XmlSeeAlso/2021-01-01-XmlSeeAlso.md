---
title: XmlSeeAlso
permalink: Java/XmlSeeAlso
date: 2021-01-11
key: JavaJava.X.XmlSeeAlso
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlSeeAlso.description }}

## Sintaxis
~~~java
@Target(TYPE) @Retention(RUNTIME) public @interface XmlSeeAlso
~~~

## Ejemplo
~~~java
{{ site.data.Java.X.XmlSeeAlso.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlSeeAlso.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
