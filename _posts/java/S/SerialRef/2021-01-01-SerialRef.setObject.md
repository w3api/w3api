---
title: SerialRef.setObject()
permalink: Java/SerialRef/setObject
date: 2021-01-11
key: JavaJava.S.SerialRef
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialRef.metodos valor="setObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setObject(Object obj) throws SerialException
~~~

## Parámetros
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}

## Excepciones
[SerialException](/Java/SerialException/)

## Clase Padre
[SerialRef](/Java/SerialRef/)

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
