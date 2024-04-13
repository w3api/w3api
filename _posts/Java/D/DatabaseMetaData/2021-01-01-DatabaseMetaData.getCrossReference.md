---
title: DatabaseMetaData.getCrossReference()
permalink: /Java/DatabaseMetaData/getCrossReference/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
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
* **String foreignSchema**,  {% include w3api/param_description.html metodo=_dato parametro="String foreignSchema" %}
* **String parentSchema**,  {% include w3api/param_description.html metodo=_dato parametro="String parentSchema" %}
* **String foreignCatalog**,  {% include w3api/param_description.html metodo=_dato parametro="String foreignCatalog" %}
* **String foreignTable**,  {% include w3api/param_description.html metodo=_dato parametro="String foreignTable" %}
* **String parentTable**,  {% include w3api/param_description.html metodo=_dato parametro="String parentTable" %}
* **String parentCatalog**,  {% include w3api/param_description.html metodo=_dato parametro="String parentCatalog" %}

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
