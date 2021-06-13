---
title: ParameterMetaData.getParameterTypeName()
permalink: /Java/ParameterMetaData/getParameterTypeName/
date: 2021-01-11
key: Java.P.ParameterMetaData
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParameterMetaData.metodos valor="getParameterTypeName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getParameterTypeName(int param) throws SQLException
~~~

## Parámetros
* **int param**,  {% include w3api/param_description.html metodo=_dato parametro="int param" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[ParameterMetaData](/Java/ParameterMetaData/)

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
