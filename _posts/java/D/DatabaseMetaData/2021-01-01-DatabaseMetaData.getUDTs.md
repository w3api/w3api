---
title: DatabaseMetaData.getUDTs()
permalink: /Java/DatabaseMetaData/getUDTs/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
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
* **String typeNamePattern**,  {% include w3api/param_description.html metodo=_dato parametro="String typeNamePattern" %}
* **String schemaPattern**,  {% include w3api/param_description.html metodo=_dato parametro="String schemaPattern" %}
* **int[] types**,  {% include w3api/param_description.html metodo=_dato parametro="int[] types" %}
* **String catalog**,  {% include w3api/param_description.html metodo=_dato parametro="String catalog" %}

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
