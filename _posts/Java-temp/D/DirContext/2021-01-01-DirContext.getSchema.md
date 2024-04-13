---
title: DirContext.getSchema()
permalink: /Java/DirContext/getSchema/
date: 2021-01-11
key: Java.D.DirContext
category: Java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirContext.metodos valor="getSchema" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DirContext getSchema(String name) throws NamingException
DirContext getSchema(Name name) throws NamingException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}

## Excepciones
[OperationNotSupportedException](/Java/OperationNotSupportedException/), [NamingException](/Java/NamingException/)

## Clase Padre
[DirContext](/Java/DirContext/)

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
