---
title: XPathResult.snapshotItem()
permalink: /Java/XPathResult/snapshotItem/
date: 2021-01-11
key: Java.X.XPathResult
category: Java
tags: ['java se', 'org.w3c.dom.xpath', 'jdk.xml.dom', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathResult.metodos valor="snapshotItem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Node snapshotItem(int index) throws XPathException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[XPathException](/Java/XPathException/)

## Clase Padre
[XPathResult](/Java/XPathResult/)

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
