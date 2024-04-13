---
title: LocalObject._invoke()
permalink: /Java/LocalObject/_invoke/
date: 2021-01-11
key: Java.L.LocalObject
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalObject.metodos valor="_invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputStream _invoke(OutputStream output) throws ApplicationException, RemarshalException
~~~

## Parámetros
* **OutputStream output**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream output" %}

## Excepciones
[RemarshalException](/Java/RemarshalException/), [ApplicationException](/Java/ApplicationException/)

## Clase Padre
[LocalObject](/Java/LocalObject/)

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
