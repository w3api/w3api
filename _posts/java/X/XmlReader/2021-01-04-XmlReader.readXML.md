---
title: XmlReader.readXML()
permalink: Java/XmlReader/readXML
date: 2021-01-04
key: JavaJava.X.XmlReader
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XmlReader.metodos valor="readXML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readXML(WebRowSet caller, Reader reader) throws SQLException
~~~

## Parámetros
* **WebRowSet caller**,  {% include w3api/param_description.html metodo=_data parametro="WebRowSet caller" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[XmlReader](/Java/XmlReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
