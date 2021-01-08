---
title: WebRowSet.readXml()
permalink: Java/WebRowSet/readXml
date: 2021-01-04
key: JavaJava.W.WebRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebRowSet.metodos valor="readXml" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readXml(InputStream iStream) throws SQLException, IOException
void readXml(Reader reader) throws SQLException
~~~

## Parámetros
* **InputStream iStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream iStream" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

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
{%- for _ldc in site.data.Java.W.WebRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
