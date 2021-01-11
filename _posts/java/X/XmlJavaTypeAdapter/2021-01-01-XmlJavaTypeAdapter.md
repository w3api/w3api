---
title: XmlJavaTypeAdapter
permalink: Java/XmlJavaTypeAdapter
date: 2021-01-11
key: JavaJava.X.XmlJavaTypeAdapter
category: java
tags: ['java se', 'javax.xml.bind.annotation.adapters', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlJavaTypeAdapter.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({PACKAGE,FIELD,METHOD,TYPE,PARAMETER}) public @interface XmlJavaTypeAdapter
~~~

## Elementos
* [type](/Java/XmlJavaTypeAdapter/type)

## Ejemplo
~~~java
{{ site.data.Java.X.XmlJavaTypeAdapter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlJavaTypeAdapter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
