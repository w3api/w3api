---
title: XmlTransient
permalink: Java/XmlTransient
date: 2021-01-11
key: JavaJava.X.XmlTransient
category: java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlTransient.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,METHOD,TYPE}) public @interface XmlTransient
~~~

## Ejemplo
~~~java
{{ site.data.Java.X.XmlTransient.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlTransient.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
