---
title: LSSerializer.writeToURI()
permalink: Java/LSSerializer/writeToURI
date: 2021-01-04
key: JavaJava.L.LSSerializer
category: java
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
* **Node nodeArg**,  {% include w3api/param_description.html metodo=_data parametro="Node nodeArg" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

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
{%- for _ldc in site.data.Java.L.LSSerializer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
