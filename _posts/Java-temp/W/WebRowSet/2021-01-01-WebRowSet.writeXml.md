---
title: WebRowSet.writeXml()
permalink: /Java/WebRowSet/writeXml/
date: 2021-01-11
key: Java.W.WebRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebRowSet.metodos valor="writeXml" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeXml(OutputStream oStream) throws SQLException, IOException
void writeXml(Writer writer) throws SQLException
void writeXml(ResultSet rs, OutputStream oStream) throws SQLException, IOException
void writeXml(ResultSet rs, Writer writer) throws SQLException
~~~

## Parámetros
* **ResultSet rs**,  {% include w3api/param_description.html metodo=_dato parametro="ResultSet rs" %}
* **Writer writer**,  {% include w3api/param_description.html metodo=_dato parametro="Writer writer" %}
* **OutputStream oStream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream oStream" %}

## Excepciones
[SQLException](/Java/SQLException/), [IOException](/Java/IOException/)

## Clase Padre
[WebRowSet](/Java/WebRowSet/)

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
