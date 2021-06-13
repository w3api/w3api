---
title: LSSerializer.write()
permalink: /Java/LSSerializer/write/
date: 2021-01-11
key: Java.L.LSSerializer
category: java
tags: ['java se', 'org.w3c.dom.ls', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LSSerializer.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean write(Node nodeArg, LSOutput destination) throws LSException
~~~

## Parámetros
* **LSOutput destination**,  {% include w3api/param_description.html metodo=_dato parametro="LSOutput destination" %}
* **Node nodeArg**,  {% include w3api/param_description.html metodo=_dato parametro="Node nodeArg" %}

## Excepciones
[LSException](/Java/LSException/)

## Clase Padre
[LSSerializer](/Java/LSSerializer/)

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
