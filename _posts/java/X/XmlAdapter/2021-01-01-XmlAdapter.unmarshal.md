---
title: XmlAdapter.unmarshal()
permalink: /Java/XmlAdapter/unmarshal/
date: 2021-01-11
key: Java.X.XmlAdapter
category: Java
tags: ['java se', 'javax.xml.bind.annotation.adapters', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XmlAdapter.metodos valor="unmarshal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract BoundType unmarshal(ValueType v) throws Exception
~~~

## Parámetros
* **ValueType v**,  {% include w3api/param_description.html metodo=_dato parametro="ValueType v" %}

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
