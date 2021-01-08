---
title: DataSource.setLoginTimeout()
permalink: Java/DataSource-javax-sql/setLoginTimeout
date: 2021-01-04
key: JavaJava.D.DataSource-javax-sql
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataSource-javax-sql.metodos valor="setLoginTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setLoginTimeout(int seconds) throws SQLException
~~~

## Parámetros
* **int seconds**,  {% include w3api/param_description.html metodo=_data parametro="int seconds" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[DataSource](/Java/DataSource-javax-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataSource-javax-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
