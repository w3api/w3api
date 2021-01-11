---
title: DatabaseMetaData.getAttributes()
permalink: Java/DatabaseMetaData/getAttributes
date: 2021-01-11
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getAttributes(String catalog, String schemaPattern, String typeNamePattern, String attributeNamePattern) throws SQLException
~~~

## Parámetros
* **String typeNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String typeNamePattern" %}
* **String schemaPattern**,  {% include w3api/param_description.html metodo=_dato parametro="String schemaPattern" %}
* **String catalog**,  {% include w3api/param_description.html metodo=_dato parametro="String catalog" %}
* **String attributeNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String attributeNamePattern" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
