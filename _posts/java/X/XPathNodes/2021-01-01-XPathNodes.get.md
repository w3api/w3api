---
title: XPathNodes.get()
permalink: Java/XPathNodes/get
date: 2021-01-11
key: JavaJava.X.XPathNodes
category: java
tags: ['java se', 'javax.xml.xpath', 'java.xml', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathNodes.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Node get(int index) throws XPathException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[XPathException](/Java/XPathException/)

## Clase Padre
[XPathNodes](/Java/XPathNodes/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
