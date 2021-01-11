---
title: XmlElementRef
permalink: Java/XmlElementRef
date: 2021-01-11
key: JavaJava.X.XmlElementRef
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlElementRef.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,METHOD}) public @interface XmlElementRef
~~~

## Elementos
* [name](/Java/XmlElementRef/name)
* [namespace](/Java/XmlElementRef/namespace)
* [required](/Java/XmlElementRef/required)
* [type](/Java/XmlElementRef/type)

## Ejemplo
~~~java
{{ site.data.Java.X.XmlElementRef.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlElementRef.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
