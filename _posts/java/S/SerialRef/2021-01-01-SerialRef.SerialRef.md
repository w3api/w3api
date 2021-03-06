---
title: SerialRef.SerialRef()
permalink: /Java/SerialRef/SerialRef/
date: 2021-01-11
key: Java.S.SerialRef
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialRef.constructores valor="SerialRef" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SerialRef(Ref ref) throws SerialException, SQLException
~~~

## Parámetros
* **Ref ref**,  {% include w3api/param_description.html metodo=_dato parametro="Ref ref" %}

## Excepciones
[SQLException](/Java/SQLException/), [SerialException](/Java/SerialException/)

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
