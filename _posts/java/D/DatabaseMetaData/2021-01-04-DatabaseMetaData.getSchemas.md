---
title: DatabaseMetaData.getSchemas()
permalink: Java/DatabaseMetaData/getSchemas
date: 2021-01-04
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getSchemas" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getSchemas() throws SQLException
ResultSet getSchemas(String catalog, String schemaPattern) throws SQLException
~~~

## Parámetros
* **String catalog**,  {% include w3api/param_description.html metodo=_data parametro="String catalog" %}
* **String schemaPattern**,  {% include w3api/param_description.html metodo=_data parametro="String schemaPattern" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[DatabaseMetaData](/Java/DatabaseMetaData/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatabaseMetaData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
