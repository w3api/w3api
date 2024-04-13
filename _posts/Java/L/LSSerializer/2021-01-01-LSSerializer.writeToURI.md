---
title: LSSerializer.writeToURI()
permalink: /Java/LSSerializer/writeToURI/
date: 2021-01-11
key: Java.L.LSSerializer
category: Java
tags: ['java se', 'org.w3c.dom.ls', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LSSerializer.metodos valor="writeToURI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean writeToURI(Node nodeArg, String uri) throws LSException
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
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
