---
title: XmlElementWrapper
permalink: Java/XmlElementWrapper
date: 2021-01-04
key: JavaJava.X.XmlElementWrapper
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlElementWrapper.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,METHOD}) public @interface XmlElementWrapper
~~~

## Elementos
* [name](/Java/XmlElementWrapper/name)
* [namespace](/Java/XmlElementWrapper/namespace)
* [nillable](/Java/XmlElementWrapper/nillable)
* [required](/Java/XmlElementWrapper/required)

## Ejemplo
~~~java
{{ site.data.Java.X.XmlElementWrapper.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlElementWrapper.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
