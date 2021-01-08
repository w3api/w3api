---
title: XmlElementDecl
permalink: Java/XmlElementDecl
date: 2021-01-04
key: JavaJava.X.XmlElementDecl
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlElementDecl.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(METHOD) public @interface XmlElementDecl
~~~

## Elementos
* [defaultValue](/Java/XmlElementDecl/defaultValue)
* [namespace](/Java/XmlElementDecl/namespace)
* [scope](/Java/XmlElementDecl/scope)
* [substitutionHeadName](/Java/XmlElementDecl/substitutionHeadName)
* [substitutionHeadNamespace](/Java/XmlElementDecl/substitutionHeadNamespace)

## Ejemplo
~~~java
{{ site.data.Java.X.XmlElementDecl.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlElementDecl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
