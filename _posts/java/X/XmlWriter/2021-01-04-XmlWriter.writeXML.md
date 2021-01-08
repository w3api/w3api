---
title: XmlWriter.writeXML()
permalink: Java/XmlWriter/writeXML
date: 2021-01-04
key: JavaJava.X.XmlWriter
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XmlWriter.metodos valor="writeXML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeXML(WebRowSet caller, Writer writer) throws SQLException
~~~

## Parámetros
* **WebRowSet caller**,  {% include w3api/param_description.html metodo=_data parametro="WebRowSet caller" %}
* **Writer writer**,  {% include w3api/param_description.html metodo=_data parametro="Writer writer" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[XmlWriter](/Java/XmlWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XmlWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
