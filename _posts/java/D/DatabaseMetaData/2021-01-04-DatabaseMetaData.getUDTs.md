---
title: DatabaseMetaData.getUDTs()
permalink: Java/DatabaseMetaData/getUDTs
date: 2021-01-04
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getUDTs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getUDTs(String catalog, String schemaPattern, String typeNamePattern, int[] types) throws SQLException
~~~

## Parámetros
* **String typeNamePattern**,  {% include w3api/param_description.html metodo=_data parametro="String typeNamePattern" %}
* **int[] types**,  {% include w3api/param_description.html metodo=_data parametro="int[] types" %}
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
