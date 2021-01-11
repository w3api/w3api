---
title: XmlReader.readXML()
permalink: Java/XmlReader-javax-sql-rowset-spi/readXML
date: 2021-01-11
key: JavaJava.X.XmlReader-javax-sql-rowset-spi
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XmlReader-javax-sql-rowset-spi.metodos valor="readXML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readXML(WebRowSet caller, Reader reader) throws SQLException
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **WebRowSet caller**,  {% include w3api/param_description.html metodo=_dato parametro="WebRowSet caller" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[XmlReader](/Java/XmlReader-javax-sql-rowset-spi/)

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
