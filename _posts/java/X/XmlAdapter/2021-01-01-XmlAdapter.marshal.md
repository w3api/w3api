---
title: XmlAdapter.marshal()
permalink: /Java/XmlAdapter/marshal/
date: 2021-01-11
key: Java.X.XmlAdapter
category: Java
tags: ['java se', 'javax.xml.bind.annotation.adapters', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XmlAdapter.metodos valor="marshal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ValueType marshal(BoundType v) throws Exception
~~~

## Parámetros
* **BoundType v**,  {% include w3api/param_description.html metodo=_dato parametro="BoundType v" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[XmlAdapter](/Java/XmlAdapter/)

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
