---
title: DefaultHandler2
permalink: /Java/DefaultHandler2/
date: 2021-01-11
key: Java.D.DefaultHandler2
category: Java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'clase java', 'Java 1.5', 'SAX 2.0 (extensions Java 1.1 alpha)']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DefaultHandler2.description }}

## Sintaxis
~~~java
public class DefaultHandler2 extends DefaultHandler implements LexicalHandler, DeclHandler, EntityResolver2
~~~

## Constructores
* [DefaultHandler2()](/Java/DefaultHandler2/DefaultHandler2/)

## Métodos
* [getExternalSubset()](/Java/DefaultHandler2/getExternalSubset)
* [resolveEntity()](/Java/DefaultHandler2/resolveEntity)

## Ejemplo
~~~java
{{ site.data.Java.D.DefaultHandler2.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultHandler2.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
