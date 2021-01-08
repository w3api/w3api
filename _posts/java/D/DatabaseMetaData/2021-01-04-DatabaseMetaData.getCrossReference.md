---
title: DatabaseMetaData.getCrossReference()
permalink: Java/DatabaseMetaData/getCrossReference
date: 2021-01-04
key: JavaJava.D.DatabaseMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="getCrossReference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet getCrossReference(String parentCatalog, String parentSchema, String parentTable, String foreignCatalog, String foreignSchema, String foreignTable) throws SQLException
~~~

## Parámetros
* **String parentSchema**,  {% include w3api/param_description.html metodo=_data parametro="String parentSchema" %}
* **String foreignCatalog**,  {% include w3api/param_description.html metodo=_data parametro="String foreignCatalog" %}
* **String foreignTable**,  {% include w3api/param_description.html metodo=_data parametro="String foreignTable" %}
* **String parentCatalog**,  {% include w3api/param_description.html metodo=_data parametro="String parentCatalog" %}
* **String parentTable**,  {% include w3api/param_description.html metodo=_data parametro="String parentTable" %}
* **String foreignSchema**,  {% include w3api/param_description.html metodo=_data parametro="String foreignSchema" %}

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
