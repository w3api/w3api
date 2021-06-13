---
title: XmlElementRefs
permalink: /Java/XmlElementRefs/
date: 2021-01-11
key: Java.X.XmlElementRefs
category: Java
tags: ['java se', 'javax.xml.bind.annotation', 'java.xml.bind', 'anotacion java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.X.XmlElementRefs.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,METHOD}) public @interface XmlElementRefs
~~~

## Ejemplo
~~~java
{{ site.data.Java.X.XmlElementRefs.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlElementRefs.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
